## CryptoMonitor

CryptoMonitor is a Python-based tool designed to monitor and identify rising cryptocurrencies based on their 24-hour price change percentage. It fetches data from the CoinGecko API, processes the data to find cryptocurrencies that have increased in value by a specified threshold, and provides a web interface to display the results.

## Features

- Fetches real-time cryptocurrency data from the CoinGecko API.
- Identifies cryptocurrencies that have risen above a specified threshold in the     last 24 hours.
- Provides a web interface to display rising cryptocurrencies.

## Installation
To get started with CryptoMonitor, follow these steps:

1. Clone the Repository:

      git clone https://github.com/boukharsaomar/CryptoMonitor.git
      cd CryptoMonitor

2. Set Up a Virtual Environment (Optional but Recommended):

      python -m venv venv
      venv\Scripts\activate  # On Windows
      source venv/bin/activate  # On macOS/Linux

3. Install Required Packages:

      pip install -r requirements.txt

## Usage
1. Run the Flask Application:

Navigate to the directory where you saved the script and run it:

      python app.py
      
2. Access the Web Interface:

Open your web browser and go to http://127.0.0.1:5000 to view the rising cryptocurrencies.

## Example Output
The web interface will display a table of cryptocurrencies that meet the criteria. Example output:

      Name	   Symbol	Current Price (USD)	24h Change (%)
      Bitcoin	btc	   50000	               12.5
      Ethereum	eth	   4000	               15.2

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Data provided by CoinGecko.
