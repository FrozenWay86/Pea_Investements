def calculate_performance(stock, current_price):
    #Calcul de la plus-value latente et du rendement
    buy_value = stock['buy_price'] * stock['quantity']
    current_value = current_price * stock['quantity']
    profit_loss = current_value - buy_value
    rendement = (profit_loss / buy_value) * 100

    return profit_loss, rendement

def total_value(portfolio, prices):
    #Calcul de la valeur totale du portefeuille
    total = 0
    for stock in portfolio:
        current_price = prices.get(stock['name'], 0)
        if current_price:
            total += current_price * stock['quantity']
    return total
