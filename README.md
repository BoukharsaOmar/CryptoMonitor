# CryptoMonitor

CryptoMonitor is a Python-based tool designed to monitor and identify rising cryptocurrencies based on their 24-hour price change percentage. It fetches data from the CoinGecko API, processes the data to find cryptocurrencies that have increased in value by a specified threshold, and sends alerts for those that meet the criteria.

## Features

- Fetches real-time cryptocurrency data from the CoinGecko API.
- Identifies cryptocurrencies that have risen above a specified threshold in the last 24 hours.
- Sends alerts for rising cryptocurrencies.

## Installation

To get started with CryptoMonitor, follow these steps:

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/CryptoMonitor.git
   cd CryptoMonitor

2. Set Up a Virtual Environment (Optional but Recommended):

    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux

3. Install Required Packages:

    pip install requests pandas

## Usage

1. Run the Script:

Navigate to the directory where you saved the script and run it:

    python crypto_monitor.py

2. Customize the Threshold:

By default, the script identifies cryptocurrencies that have risen by 10% or more in the last 24 hours. You can customize this threshold by modifying the identify_rising_cryptos function in the script.

## Example Output

The script will print alerts for cryptocurrencies that meet the criteria. Example output:

    Crypto Bitcoin (btc) is rising: 12.5% in the last 24 hours.
    Crypto Ethereum (eth) is rising: 15.2% in the last 24 hours.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Data provided by CoinGecko.
