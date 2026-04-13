# Файл: main.py
# Импортируем класс из файла bank_account.py
from bank_account import BankAccount

# Создаём счёт
account = BankAccount("Иван Иванов", 1000)

# Пытаемся получить баланс через геттер (правильно)
print(f"Баланс: {account.get_balance()} руб.")  # Вывод: Баланс: 1000 руб.

# Попытка прямого доступа к приватному атрибуту (ошибка)
try:
    print(account.__balance)  # Вызовет AttributeError
except AttributeError:
    print("Ошибка: нельзя напрямую получить __balance!")

# Операции с балансом через методы (правильно)
account.deposit(500)      # Пополнение: +500 руб.
account.withdraw(200)     # Снятие: -200 руб.
print(f"Итоговый баланс: {account.get_balance()} руб.")  # Итоговый баланс: 1300 руб.

# Попытка внести отрицательную сумму (проверка работает)
account.deposit(-100)   # Сумма должна быть положительной!
