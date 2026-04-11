from user import User
from card import Card

user1 = User('Alex')

user1.sayName()
user1.setAge(18)
user1.sayAge()
card = Card('2562 1235 4569 7856', '11/28', 'Alex F')
user1.addCard(card)
user1.getCard().pay(1000)



