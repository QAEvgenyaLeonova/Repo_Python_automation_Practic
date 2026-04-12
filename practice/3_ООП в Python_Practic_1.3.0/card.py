class Card():
    number = '2222 3333 5555 6666'
    validDate = '01/99'
    holder = 'unknown'

    def __init__(self, number, validDate, holder):
        self.holder = holder
        self.number = number
        self.validDate = validDate

    def pay(self, amount):
        print('с карты', self.number, 'списали', amount)
