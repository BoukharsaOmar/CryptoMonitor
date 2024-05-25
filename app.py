from flask import Flask, render_template
import requests
import pandas as pd
from datetime import datetime

app = Flask(__name__)

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

@app.route('/')
def index():
    data = fetch_crypto_data()
    rising_cryptos = identify_rising_cryptos(data)
    return render_template('index.html', cryptos=rising_cryptos.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
