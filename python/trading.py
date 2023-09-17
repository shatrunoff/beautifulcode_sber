from decimal import Decimal
from enum import Enum
import random

class AssetPrice(Enum):
    # Котировальный список активов.
    LKOH = Decimal(5896)
    SBER = Decimal(250)

class Portfolio:
    def __init__(self, balance):
        self.assets = {asset: 0 for asset in AssetPrice}
        self.balance = Decimal(balance)

    def buy_asset(self, asset, quantity):
        if asset in self.assets and quantity > 0:
            total_cost = asset.value * quantity
            if total_cost <= self.balance:
                self.assets[asset] += quantity
                self.balance -= total_cost
            else:
                print("Недостаточно средств для покупки")

    def sale_asset(self, asset, quantity):
        if asset in self.assets and quantity > 0:
            if self.assets[asset] >= quantity:
                self.assets[asset] -= quantity
                self.balance += asset.value * quantity
            else:
                print("Недостаточно активов для продажи")

    def portfolio_value(self):
        value = Decimal(0)
        for asset, quantity in self.assets.items():
            value += asset.value * quantity
        return value

# Пример симуляции
if __name__ == "__main__":
    
    # Начальный баланс клиента
    balance = 100000  
    portfolio = Portfolio(balance)

    # Покупка активов
    portfolio.buy_asset(AssetPrice.LKOH, 5)
    portfolio.buy_asset(AssetPrice.SBER, 10)
    
    # Продажа активов
    portfolio.sale_asset(AssetPrice.LKOH, 2)
    portfolio.sale_asset(AssetPrice.SBER, 5)
    
    # Получение стоимости портфеля и баланса
    print(f"Текущая стоимость портфеля: {portfolio.portfolio_value()} рублей")
    print(f"Текущий баланс клиента: {portfolio.balance} рублей")