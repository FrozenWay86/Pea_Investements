import yfinance as yf

def get_current_price(symbol):
    #Retourne le prix actuel d'une action
    stock = yf.Ticker(symbol)
    price = stock.history(period="1d")['Close'][0]
    return price
