from unittest import result

# 1 файл сalculator
class Calculator:

    def sum(self, a, b):
        result = a + b
        return result

    def sub(self,a, b):
        result = a - b
        return result

    def mul(self,a, b):
        return a * b

    def div(self,a, b):
        if (b == 0):
            raise ArithmeticError('На ноль делить нельзя')
        return a / b

    def pow(self,a, b = 2):
        return a ** b
    #print(2, 4)
    #print(2) - по умолчаниею будет 2


    #[1, 2, 3, 4]
    def avg(self,nums):
        if (len(nums) == 0):
            return 0
        s = 0
        for num in nums:
            s = self.sum(s, num)

        length = len(nums)
        return self.div(s, length)

# 2 файл сalculator

'''Почему такой способ проверок неудобен?

Потому что одна ошибка (один проваленный тест) скрывает статус всех следующих проверок. Если в проекте тысяча тестов, то одна ошибка
может заблокировать проверку остальных сотен тестов.'''

from calculator import Calculator

calculator = Calculator()

#Проверка сложения положительных чисел
res = calculator.sum(4, 5)
assert res == 9

#Проверка сложения отрицательных чисел
res = calculator.sum(-6, -10)
assert res == -16

#Проверка сложения отрицательного и положительного чисел
res = calculator.sum(-6, 6)
assert  res == 0

#Проверка сложения десятичных дробей
res = calculator.sum(5.6, 4.3)
res = round(res, 1)
assert res == 9.9

#Проверка сложения числа и нуля
res = calculator.sum(10, 0)
assert res == 10

#Проверка сложения числа и нуля
res = calculator.div(10, 2)
assert res == 5

#Проверка деления на ноль
res = calculator.div(10, 0)
assert res == None

#Проверка нахождения среднего арифметического
numbers = []
res = calculator.avg(numbers)
assert res == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
res = calculator.avg(numbers)
print(res)
assert res == 5

'''Разбор вашего примера
У вас список: [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]

Считаем сумму всех чисел:
1+2+3+4+5+6+7+8+9+5=50

Считаем количество чисел в списке:
В списке 10 чисел.

Делим сумму на количество:
50÷10=5

Итог: среднее арифметическое = 5.'''


# 3 файл сalculator

'''Создание теста
В предыдущем степе мы поняли, что тестирование каждого метода класса — дело трудоемкое и долгое.
Поэтому сейчас мы создадим более удобный вариант для проверки методов.'''

import pytest
from calculator import Calculator

calculator = Calculator()

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    assert res == 9.9

def test_sum_zero_nams():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10

def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)


def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0

def test_avg_positive():
    calculator = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator.avg(numbers)
    assert res == 5



#4.Файл Декоратор и Маркеровка
import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.xfail #Я ожидаю, что этот тест провалится
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

@pytest.mark.skip(reason= 'Починить тест позже')#reason="..." — почему ожидается провал (лучше для отчётов);
def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

@pytest.mark.xfail(strict = True)#«Я точно знаю, почему этот тест должен провалиться. У меня есть причина!»
#@pytest.mark.xfail(strict=False) «Я не уверен, почему этот тест может провалиться, но хочу проверить — вдруг не сработает?»
def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 1

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    assert res == 9.9

def test_sum_zero_nams():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10

#pytest -m positive_test
@pytest.mark.positive_test #создали собственную маркировку
def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)


def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0

def test_avg_positive():
    calculator = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator.avg(numbers)
    assert res == 5


#5 Файл (упрощение)

import pytest
from calculator import Calculator

calculator = Calculator()            #Создание экземпляра класса, #  глобальный экземпляр

@pytest.mark.parametrize('num1, num2, result', [(4, 5, 9), (-6, -10, -16), (-6, 6, 0), (5.61, 4.29, 9.9), (10, 0, 10)])
def test_sum_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result

@pytest.mark.positive_test
def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ZeroDivisionError):
        calculator.div(10, 0)

@pytest.mark.parametrize('nums, expected', [([], 0),([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5)])
def test_avg_list(nums, expected):
    calculator = Calculator()
    res = calculator.avg(nums)
    assert res == expected


'''ПРАКТИКА'''
class StringProcessor:# строка процессора
    @staticmethod
    def process(text: str) -> str:
        if not text:
            return '.'
        processed_text = text[0].upper() + text[1:]
        if not processed_text.endswith('.'):
            processed_text += '.'
        return processed_text

import pytest
from string_processor import StringP

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello."),
        ("Hello", "Hello."),
        ("hello world", "Hello world."),
    ],
)
def test_process_positive(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("", "."), ("    ", "    .")],
)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output




















