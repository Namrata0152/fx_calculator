exchange_rates = {
    'AUDUSD': 0.8371, 'CADUSD': 0.8711, 'USDCNY': 6.1715,
    'EURUSD': 1.2315, 'GBPUSD': 1.5683, 'NZDUSD': 0.7750,
    'USDJPY': 119.95, 'EURCZK': 27.6028, 'EURDKK': 7.4405,
    'EURNOK': 8.6651
}

precision = {
    'AUD': 2, 'CAD': 2, 'CNY': 2, 'CZK': 2, 'DKK': 2,
    'EUR': 2, 'GBP': 2, 'JPY': 0, 'NOK': 2, 'NZD': 2, 'USD': 2
}

cross_via = {
    ('AUD', 'JPY'): 'USD', ('NOK', 'USD'): 'EUR'
}

def get_rate(from_currency, to_currency):
    pair = from_currency + to_currency
    if pair in exchange_rates:
        return exchange_rates[pair]
    inverted_pair = to_currency + from_currency
    if inverted_pair in exchange_rates:
        return 1 / exchange_rates[inverted_pair]
    if (from_currency, to_currency) in cross_via:
        via_currency = cross_via[(from_currency, to_currency)]
        rate1 = get_rate(from_currency, via_currency)
        rate2 = get_rate(via_currency, to_currency)
        return rate1 * rate2
    print(f"Unable to find rate for {from_currency}/{to_currency}")
    return None

def format_amount(amount, currency):
    return f"{amount:.{precision[currency]}f} {currency}"

def convert_currency(amount, from_currency, to_currency):
    rate = get_rate(from_currency, to_currency)
    if rate is None:
        return None
    converted_amount = amount * rate
    return format_amount(converted_amount, to_currency)

def main():
    print("Welcome to the FX Calculator")
    while True:
        try:
            from_currency = input("From (currency): ").strip().upper()
            amount = float(input(f"Amount in {from_currency}: ").strip())
            to_currency = input("To (currency): ").strip().upper()
            result = convert_currency(amount, from_currency, to_currency)
            if result:
                print(f"Converted amount: {result}")
            else:
                print("Conversion failed.")
        except ValueError:
            print("Invalid input. Please enter the correct values.")
        except KeyboardInterrupt:
            print("\nExiting the FX Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
