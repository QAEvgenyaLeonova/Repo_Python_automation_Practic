# Файл: bank_account.py

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        # Приватный атрибут (скрыт от прямого доступа)
        self.__balance = initial_balance

    # Геттер — метод для безопасного получения баланса
    def get_balance(self):
        return self.__balance

    # Сеттер — метод для изменения баланса с проверкой
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение: +{amount} руб.")
        else:
            print("Сумма должна быть положительной!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снятие: -{amount} руб.")
        else:
            print("Недостаточно средств или неверная сумма!")
