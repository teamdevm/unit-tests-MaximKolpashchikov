import requests

class Converter:
    def get_exchange_rate(self, currency: str) -> float:
        # Метод возвращает курс указанной валюты
        # url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        if (currency == 'USD'):
            return 100
        elif (currency == 'EUR'):
            return 300
        elif (currency == 'GBR'):
            return 200

    def convert_bitcoins(self, currency: str, coins: int) -> float:
        # Метод возвращает сколько стоит в указанной валюте заданное количество биткоинов
        return self.get_exchange_rate(currency) * coins