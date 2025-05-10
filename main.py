import logging
import os
import requests
import yfinance as yf
import ta
import ccxt
import pandas as pd

from core.exchange import CryptoExchange
from core.telegrambot import TelegramBot
from core.tradeexcutor import TradeExecutor

API_KEY = 'YOUR_COINAPI_KEY'
BASE_URL = 'https://rest.coinapi.io/v1/'

def get_market_data(symbol, period='1MIN'):
    headers = {'X-CoinAPI-Key': API_KEY}
    url = f"{BASE_URL}ohlcv/{symbol}/latest?period_id={period}"
    response = requests.get(url, headers=headers)
    return response.json()

def generate_signal(data):
    df = pd.DataFrame(data)
    df['time_period_start'] = pd.to_datetime(df['time_period_start'])
    df.set_index('time_period_start', inplace=True)

    # Calculate indicators
    df['sma'] = ta.trend.sma_indicator(df['price_close'], window=20)
    df['rsi'] = ta.momentum.rsi(df['price_close'], window=14)

    # Generate signals
    if df['sma'].iloc[-1] > df['sma'].iloc[-2] and df['rsi'].iloc[-1] < 30:
        return 'Buy'
    elif df['sma'].iloc[-1] < df['sma'].iloc[-2] and df['rsi'].iloc[-1] > 70:
        return 'Sell'
    else:
        return 'Hold'

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    c_dir = os.path.dirname(__file__)
    with open(os.path.join(c_dir, "config/secrets.txt")) as key_file:
        api_key, secret, telegram_tkn, user_id = key_file.read().splitlines()

    ccxt_ex = ccxt.bitfinex()
    ccxt_ex.apiKey = api_key
    ccxt_ex.secret = secret

    exchange = CryptoExchange(ccxt_ex)
    trade_executor = TradeExecutor(exchange)
    telegram_bot = TelegramBot(telegram_tkn, user_id, trade_executor)

    market_data = get_market_data('BITSTAMP_SPOT_BTC_USD')
    signal = generate_signal(market_data)
    logging.info(f"Trading Signal: {signal}")

    telegram_bot.start_bot()