from setuptools import setup, find_packages

setup(
    name='fx_calculator',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fx_calculator = fx_calculator.converter:main'
        ]
    },
)
