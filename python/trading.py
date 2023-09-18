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
            cost = asset.value * quantity
            if cost <= self.balance:
                self.assets[asset] += quantity
                self.balance -= cost
            else:
                print("Недостаточно средств для покупки")
        else:
            print("Проверьте правильность заполненных данных")

    def sale_asset(self, asset, quantity):
        if asset in self.assets and quantity > 0:
            if self.assets[asset] >= quantity:
                self.assets[asset] -= quantity
                self.balance += asset.value * quantity
            else:
                print("Недостаточно активов для продажи")
        else:
            print("Проверьте правильность заполненных данных")

    def portfolio_value(self):
        value = Decimal(0)
        for asset, quantity in self.assets.items():
            value += asset.value * quantity
        return value

# Пример симуляции
if __name__ == "__main__":
    
    # Начальный баланс клиента
    balance = random.randint(50_000, 1_000_000)
    portfolio = Portfolio(balance)

    # Покупка активов
    portfolio.buy_asset(AssetPrice.LKOH, random.randint(7, 15))
    portfolio.buy_asset(AssetPrice.SBER, random.randint(50, 100))
    
    # Продажа активов
    portfolio.sale_asset(AssetPrice.LKOH, random.randint(5, 10))
    portfolio.sale_asset(AssetPrice.SBER, random.randint(10, 50))
    
    # Получение стоимости портфеля и баланса
    print(f"Текущая стоимость портфеля: {portfolio.portfolio_value()} рублей")
    print(f"Текущий баланс клиента: {portfolio.balance} рублей")