'''ШПОРА для запуска тестов'''

''''**Полезные команды**
- `pytest` — запуск тестов.
- `pytest -v` — запуск тестов с подробным выводом в консоль.
- `pytest filename.py` — запуск тестов из файла.
- `pytest filename.py::Class::function`
- `--collect-only` — вывод только списка тестов.
- `-k` — запуск по имени теста.
- `-s` — вывод всего, что печатаете в `print`.
- `--ff`, `--failed-first` — запуск первыми тех тестов, которые упали в прошлый запуск.
- `pytest -h` — полный список команд.'''

'''[pytest]
addopts = -v -s
python_classes = *Suites *Test
python_files = check_*
python_functions = assert_*'''

'''@pytest.mark.skip(reason='починить тест позже')
def test_sum_positive_nums():        
    calculator = Calculator()       
    res = calculator.sum(4, 5) 
    assert res == 9 
    

@pytest.mark.xfail - говорит о том что мы специально повредили тест и это не ошибка
+ можно указать @pytest.mark.xfail(strict = True) точно упадет или нет?'''

'''своя маркировка pytest -m positive_test
@pytest.mark.positive_test
def test_avg_positive():
    calculator = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator.avg(numbers)
    assert res == 5'''

''' pytest --markers'''

'''parametriz

@pytest.mark.parametriz('num1, num2, result', [(4, 5, 9)])
def test_sum_positive_nums(num1, num2, result):       
    calculator = Calculator()                     
    res = calculator.sum(num1, num2)                
    assert res == result  '''



























