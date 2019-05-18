from extra_modules.currency_converter import convert_currency


class Price:
    def __init__(self, price, currency='USD'):
        self.price = float(price)
        self.currency = currency

    def currency_coefficient(self, new_currency):
        return convert_currency(self.currency, new_currency, 1)

    def currency_converter(self, new_currency):
        return convert_currency(self.currency, new_currency, self.price)