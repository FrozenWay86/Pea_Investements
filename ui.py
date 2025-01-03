import tkinter as tk
from portfolio import Portfolio
from api_fetcher import get_current_price
from performance import calculate_performance, total_value

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Conseil en Investissement PEA")

        self.portfolio = Portfolio()

        # Interface pour ajouter une action
        self.name_label = tk.Label(root, text="Nom de l'action:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.quantity_label = tk.Label(root, text="Quantité:")
        self.quantity_label.grid(row=1, column=0)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=1, column=1)

        self.buy_price_label = tk.Label(root, text="Prix d'achat:")
        self.buy_price_label.grid(row=2, column=0)
        self.buy_price_entry = tk.Entry(root)
        self.buy_price_entry.grid(row=2, column=1)

        self.add_button = tk.Button(root, text="Ajouter Action", command=self.add_stock)
        self.add_button.grid(row=3, column=0, columnspan=2)

        # Affichage du portefeuille
        self.display_button = tk.Button(root, text="Afficher Portefeuille", command=self.display_portfolio)
        self.display_button.grid(row=4, column=0, columnspan=2)

    def add_stock(self):
        #Ajoute une action au portefeuille
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        buy_price = float(self.buy_price_entry.get())
        self.portfolio.add_stock(name, quantity, buy_price)

    def display_portfolio(self):
        #Affiche le portefeuille et les performances
        portfolio = self.portfolio.get_portfolio()
        prices = {stock['name']: get_current_price(stock['name']) for stock in portfolio}

        total = total_value(portfolio, prices)
        print(f"Valorisation Totale: {total}€")

        for stock in portfolio:
            current_price = prices.get(stock['name'], 0)
            if current_price:
                profit_loss, rendement = calculate_performance(stock, current_price)
                print(f"{stock['name']} - {stock['quantity']} titres - Plus/moins-value: {profit_loss:.2f}€ - Rendement: {rendement:.2f}%")

        print(f"Valorisation totale du portefeuille: {total:.2f}€")
