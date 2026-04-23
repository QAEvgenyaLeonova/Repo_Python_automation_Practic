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