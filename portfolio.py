import json

class Portfolio:
    def __init__(self, filename="portfolio.json"):
        self.filename = filename
        self.portfolio = self.load_portfolio()

    def load_portfolio(self):
      #Charge les données du portefeuille depuis un fichier JSON
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_portfolio(self):
        #Sauvegarde les données du portefeuille dans un fichier JSON
        with open(self.filename, "w") as file:
            json.dump(self.portfolio, file, indent=4)

    def add_stock(self, name, quantity, buy_price):
        #Ajoute une action au portefeuille
        stock = {"name": name, "quantity": quantity, "buy_price": buy_price}
        self.portfolio.append(stock)
        self.save_portfolio()

    def get_portfolio(self):
        #Retourne le portefeuille sous forme de liste
        return self.portfolio
