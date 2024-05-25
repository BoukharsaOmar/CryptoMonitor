import requests
import pandas as pd
from datetime import datetime  # Import the datetime module

def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return pd.DataFrame(data)

def identify_rising_cryptos(data, threshold=10):
    current_time = datetime.now()
    data['price_change_percentage_24h'] = data['price_change_percentage_24h'].astype(float)
    rising_cryptos = data[data['price_change_percentage_24h'] >= threshold]
    return rising_cryptos

def send_alerts(cryptos):
    for _, crypto in cryptos.iterrows():
        message = f"Crypto {crypto['name']} ({crypto['symbol']}) is rising: {crypto['price_change_percentage_24h']}% in the last 24 hours."
        print(message)  # Replace with actual alert mechanism

# Main workflow
data = fetch_crypto_data()
rising_cryptos = identify_rising_cryptos(data)
send_alerts(rising_cryptos)
