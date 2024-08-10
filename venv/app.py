from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trade', methods=['POST'])
def trade():
    symbol = request.form.get('symbol')
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(url).json()
    price = response.get(symbol, {}).get('usd', 'Bilinmiyor')
    return f"{symbol.upper()} fiyatı: ${price}"

if __name__ == '__main__':
    app.run(debug=True)
