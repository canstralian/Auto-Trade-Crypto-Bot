# Telegram Crypto Bot

A lightweight Telegram bot that allows you to monitor and interact with your cryptocurrency exchange account using the Telegram API and [ccxt](https://github.com/ccxt/ccxt). Built with Python, it supports basic commands like balance checking, placing orders, and retrieving market data.

---

## Features

- Telegram integration using `python-telegram-bot`
- Exchange interaction via `ccxt`
- Secure credential handling using a `secrets.txt` file
- Basic trading operations:
  - Check balance
  - Get ticker prices
  - Place market or limit orders (optional)
  - Get open orders or recent trades

---

## Getting Started

### 1. Create a Telegram Bot
- Message [**@BotFather**](https://t.me/BotFather)
- Create a new bot using `/newbot`
- Save the **Telegram Token** provided

### 2. Get Exchange API Keys
- Log into your preferred exchange (e.g. Binance, Kraken, Coinbase Pro)
- Create a new API key and secret pair
- Enable required permissions (e.g. "Read Balance", "Trade")

### 3. Install Dependencies

```bash
pip install python-telegram-bot ccxt

Optional: Create and activate a virtual environment before installation

4. Set Up Configuration

Create a folder named config/ and a file inside it called secrets.txt.

Example: config/secrets.txt

your_exchange_api_key
your_exchange_api_secret
your_telegram_bot_token
your_telegram_user_id

Replace the placeholders above with your actual credentials

5. Run the Bot

python main.py

If setup correctly, your bot will go online and begin responding to commands.

⸻

Example Commands

After starting your bot, try sending the following commands in your Telegram chat:
•   /start – Basic hello world
•   /balance – Show available balances
•   /price BTC/USDT – Get current market price
•   /buy BTC/USDT 0.001 – Place a market buy (optional)
•   /sell BTC/USDT 0.001 – Place a market sell (optional)

You can customize or expand commands in main.py

⸻

Security Notes
•   Never expose your secrets.txt or hard-code keys in the source.
•   Restrict bot access to your personal Telegram user ID.
•   Enable IP whitelisting or withdrawal restrictions on your exchange if possible.

⸻

Project Structure

.
├── config/
│   └── secrets.txt
├── main.py
├── requirements.txt
└── README.md


⸻

TODO / Future Features
•   Support for more exchanges
•   Order history with pagination
•   Price alerts and stop-limit orders
•   Portfolio visualization
•   Telegram bot admin panel

⸻

License

MIT License. See LICENSE file for more details.

⸻

Acknowledgments
•   python-telegram-bot
•   ccxt
•   Crypto APIs and Open Source Trading Bots inspiration