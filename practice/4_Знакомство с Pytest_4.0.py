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

from calculator import Calculator

calculator = Calculator()

# + -
# - -
# - +
# . .
# n 0

print('start')
res = calculator.sum(4, 5)
assert res == 9

res = calculator.sum(-6, -10)
assert res == -16

res = calculator.sum(-6, 6)
assert res == 0

res = calculator.sum(5.6, 4.3)
res = round(res, 1)
print(res)
assert res == 9.9

res = calculator.sum(10, 0)
assert res == 10

res = calculator.div(10, 2)
assert res == 5

numbers = []
res = calculator.avg(numbers)
assert res == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
res = calculator.avg(numbers)
print(res)
assert res == 5

res = calculator.div(10, 0)
assert res == None

print('finish')


# 3 файл сalculator
import pytest
from calculator import Calculator

calculator = Calculator()            #Создание экземпляра класса, #  глобальный экземпляр

def test_sum_positive_nums():        #Определение тестовой функции
    calculator = Calculator()        # локальный экземпляр внутри теста
    res = calculator.sum(4, 5) #Вызов метода sum:
    assert res == 9                  #Проверка результата с помощью assert

def test_sum_negativ_nums():        #Определение тестовой функции
    calculator = Calculator()        # локальный экземпляр внутри теста
    res = calculator.sum(-6, -10)  #Вызов метода sum:
    assert res == -16                #Проверка результата с помощью assert

def test_sum_positive_and_negativ_nums():        #Определение тестовой функции
    calculator = Calculator()        # локальный экземпляр внутри теста
    res = calculator.sum(-6, 6) #Вызов метода sum:
    assert res == 0

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    assert res == 9.9

def test_sun_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0)
    assert res == 10

def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ZeroDivisionError):
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

#файл(упрощение)

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























