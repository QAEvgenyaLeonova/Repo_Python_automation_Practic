'''ШПОРА для запуска тестов'''

''''**Полезные команды**
--python -m pytest -v -rA   Запускаем с подробным отчётом:
python -m pytest: «Python, посмотри вокруг, найди тесты и запусти их» — надёжно, работает почти всегда.
pytest: «Запусти тесты» — просто, но может не сработать, если Python не видит нужные файлы.
python -m pytest -v
-x	Остановка после первого упавшего теста	python -m pytest -x
--maxfail=2	Остановка после 2‑х упавших тестов	python -m pytest --maxfail=2
--tb=short	Сокращённый вывод ошибок	python -m pytest --tb=short
--tb=no	Не показывать трассировку ошибок	python -m pytest --tb=no
--durations=3	Показать 3 самых медленных теста	python -m pytest --durations=3
-rA	Полный отчёт в конце (все тесты: успешные, упавшие и т. д.)	python -m pytest -rA
-rs	Показать только пропущенные тесты	python -m pytest -rs
-rf	Показать только упавшие тесты	python -m pytest -rf
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


import pytest

#4. Простой пример теста.Создаём файл test_calculator.py
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_add_strings():
    assert add('hello ', "world") == 'hello world'

#5. Полезные опции командной строки - записала в файл: 4_Знакомство с Pytest_4.1.py
#6. Маркировка тестов (пропуск и ожидание падения)
@pytest.mark.skip(reason="Ещё не реализован")#@pytest.mark.skip — тест будет пропущен. В отчёте появится s
def test_subtract():
    assert subtract(5, 3) == 2

@pytest.mark.xfail #@pytest.mark.xfail — мы ожидаем, что тест упадёт. Если он упадёт — это нормально (отмечается x), если пройдёт — это сюрприз (X).
def test_divide_by_zero():
    assert divide(10, 0) == "Ошибка"
#Запускаем тест : python -m pytest -v -rA


#7. Фикстуры (fixtures) — для подготовки данных
#Фикстура — это функция, которая готовит данные для тестов.
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum_with_fixture(sample_data):
    assert sum(sample_data) == 15


#8. Отладка: как найти ошибку
#Если тест упал, можно запустить отладчик:
#python -m pytest --pdb

#9. Создание отчёта для CI (Jenkins и т. п.)
#Чтобы создать отчёт в формате XML (его понимают серверы непрерывной интеграции):
#bash
#python -m pytest --junitxml=report.xml

'''Полезные советы для начинающих
Имена тестов. Всегда начинайте названия функций‑тестов с test_. Например: test_calculate_sum(), test_user_login().
Структура папок. Храните тесты в папке tests/. Так pytest их автоматически найдёт.
Assert вместо print. Не пишите print(add(2,3)) и не проверяйте результат глазами. Используйте assert add(2,3) == 5.
Тестируйте крайние случаи. Проверяйте не только «обычные» данные, но и:
нули (add(0, 0));
отрицательные числа (add(-5, 3));
пустые строки или списки (если функция их принимает).
Не бойтесь ошибок. Если тест упал — это хорошо! Значит, вы нашли проблему до того, как её нашёл пользователь.
Краткий итог: 
Установите pytest: pip install pytest.
Положите код в mymodule.py, а тесты — в tests/test_mycode.py.
my_project/
├── my_module.py        # ваш код (функции, классы)
├── tests/             # папка с тестами
│   ├── __init__.py
│   └── test_mycode.py # файл с тестами
└── setup.py           # (опционально) файл настройки проекта
Пишите тесты: функции с именем test_..., внутри — assert.
Запускайте тесты командой pytest или pytest -v.
Читайте вывод: PASSED — всё хорошо, FAILED — нужно исправить код или тест.
Используйте pip install -e ., если работаете с большим проектом — это сэкономит время.'''


#Основные встроенные маркеры
#Маркеры — это «ярлыки» для тестов. Они помогают:
#пропускать тесты;
#запускать только определённые тесты;
#отмечать тесты с особым поведением.

#Пропускает тест  @pytest.mark.skip

@pytest.mark.skip(reason = 'Тест не готов')
def test_unfished_feature():
    assert 1 + 1 == 3

#Результат запуска: s



#2. @pytest.mark.skipif — пропустить при условии Пропускает тест, если условие истинно.
import sys
import pytest

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Требуется Python 3.8+")
def test_new_python_feature():
    assert True
#Если у вас Python ниже 3.8, тест будет пропущен.



#3. @pytest.mark.xfail — ожидаемый провал
#Помечает тест как «ожидаемо падающий». Если тест падает — это нормально, если проходит — это сюрприз.
import pytest

@pytest.mark.xfail(reason="Эта функция пока не работает")
def test_buggy_feature():
    assert False  # Тест упадёт, но это нормально



#4. @pytest.mark.parametrize — запуск с разными параметрами
#Позволяет запустить один тест несколько раз с разными данными.
import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (5, 25)
])
def test_square(input, expected):
    assert input ** 2 == expected



#Создание своих маркеров
#[pytest]
#addopts = --strict-markers
#markers =
#    slow: тесты, которые выполняются долго (не запускать с '-m "not slow"')
#    ui: тесты пользовательского интерфейса
#    api: тесты API

'''Что важно!!!
Маркеры — это как стикеры на тетрадях: можно пометить, что пропустить, что сложно, что срочно.
skip — «пропустить», xfail — «ожидаю, что упадёт», parametrize — «запустить много раз с разными числами».
Свои маркеры нужно зарегистрировать в pytest.ini.
Запускать тесты можно выборочно: pytest -m "название_маркера".
--strict-markers — ваш друг: он не даст ошибиться в названии маркера.'''







'''1. Виртуальное окружение и установка пакетов
Зачем: изолировать проект от системного Python.

Как сделать:
# Создаём виртуальное окружение
python -m venv myproject_env

# Активируем (Windows)
myproject_env\Scripts\activate
# Активируем (Mac/Linux)
source myproject_env/bin/activate

# Устанавливаем pytest
pip install pytest'''

'''2. Структура проекта
Вариант 1: тесты отдельно от кода (рекомендуется)

myproject/
├── setup.py
├── src/
│   └── mypkg/
│       ├── __init__.py
│       └── app.py
└── tests/
    ├── __init__.py
    └── test_app.py'''
#Плюсы: чистота кода, удобство тестирования установленной версии.
'''Вариант 2: тесты внутри пакета

myproject/
├── setup.py
└── mypkg/
    ├── __init__.py
    ├── app.py
    └── tests/
        ├── __init__.py
        └── test_app.py'''


'''3. Файл setup.py
Поместите в корень проекта:
Установите пакет в режиме редактирования:
pip install -e .
Это позволит менять код и сразу тестировать без переустановки.
Краткий итог
setup.py + pip install -e . =
ваш код становится пакетом, который можно импортировать;
изменения в коде сразу применяются без переустановки;
проект организован по стандартам Python — его легче поддерживать и распространять.'''



'''6. Пример рабочего процесса
Шаг 1. Создаём структуру проекта:
calculator/
├── setup.py
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── math_operations.py
└── tests/
    └── test_math_operations.py

Шаг 2. Код приложения (src/calculator/math_operations.py):
    def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
    
    
Шаг 3. Тесты (tests/test_math_operations.py):
from calculator.math_operations import add, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0


Шаг 4. Файл setup.py:
from setuptools import setup, find_packages

setup(
    name="calculator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)

Шаг 5. Запуск:
# В корне проекта
pip install -e .
pytest -v

'''

'''Ключевые правила:
Всегда используйте виртуальное окружение.
Храните тесты отдельно от кода (tests/).
Называйте тестовые файлы test_...py.
Начинайте функции‑тесты с test_.
Используйте assert для проверок.
Устанавливайте пакет в режиме -e при разработке.'''













