from card import Card

class User:
    age = 0

    def __init__(self, name: str):
        print('Я создался')
        self.username = name

    def sayName(self) -> None:
        '''Печатает имя пользователя'''
        print('Меня зовут ' , self.username)

    def sayAge(self) -> None:
        '''Печатает возраст пользователя'''
        print(self.age)

    def setAge(self, newAge: int) -> None:
        '''Перепечатывает имя пользователя'''
        self.age = newAge

    def addCard(self, card: Card) -> None:
        '''Добавляет пользавателю карту'''
        self.card = card

    def getCard(self) -> Card:
        '''Возвращает пользавателю карту'''
        return self.card





























