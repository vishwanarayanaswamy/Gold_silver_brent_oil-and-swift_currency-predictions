import yfinance as yf
from datetime import datetime


def get_live_price(symbol):
    try:

        ticker = yf.Ticker(symbol)

        data = ticker.history(period="1d")

        if data.empty:
            return None

        return round(float(data["Close"].iloc[-1]), 2)

    except Exception:
        return None


def get_market_data():

    now = datetime.now().strftime("%d-%m-%Y %H:%M")

    return {

        "Gold": {
            "price": get_live_price("GC=F"),
            "updated": now
        },

        "Silver": {
            "price": get_live_price("SI=F"),
            "updated": now
        },

        "Brent Oil": {
            "price": get_live_price("BZ=F"),
            "updated": now
        }

    }