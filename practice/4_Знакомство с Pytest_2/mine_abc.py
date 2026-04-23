import pytest #Импортируем библиотеку Pytest, чтобы использовать её возможности: запуск тестов, декораторы, проверки и т. д.

from string_processor import StringProcessor #Импортируем класс StringProcessor из файла string_processor.py.Этот класс содержит метод process(), который мы будем тестировать.

@pytest.mark.parametrize(  #test_process_positive три раза — по одному для каждой пары из списка.
    'input_text, expected_output', #ввод_текста, ожидаемый_ вывод /  имена параметров, которые будут передаваться в тестовую функцию.
    [
        ("hello", "Hello."),             #Первая пара: вход "hello" → ожидаемый выход "Hello.".
        ("Hello", "Hello."),             #Вторая пара: вход "Hello" → ожидаемый выход "Hello." (первая буква уже большая).
        ("hello world", "Hello world."),  #Третья пара: вход "hello world" → ожидаемый выход "Hello world." (многословная строка).
    ],
)
def test_process_positive(input_text, expected_output):#def test_process_positive(...) — объявляем тестовую функцию. Она получает два параметра: input_text (что подаём на вход) и expected_output (что ожидаем на выходе).
    processor = StringProcessor() #processor = StringProcessor() — создаём экземпляр класса StringProcessor
    assert processor.process(input_text) == expected_output # — проверяем, что результат работы метода process() совпадает с ожидаемым значением.Если совпадает — тест проходит.Если не совпадает — тест падает с ошибкой AssertionError

@pytest.mark.parametrize(
    'input_text, expected_output',
    [('', '.'), ('    ', '    .')],#Первый случай: вход "" (пустая строка) → ожидаемый выход ".".Второй случай: вход "    " (четыре пробела) → ожидаемый выход "    ." (пробелы + точка).
)
def test_process_negative(input_text, expected_output): #апускает функцию test_process_negative два раза.
    processor = StringProcessor() #Создаём экземпляр StringProcessor
    assert processor.process(input_text) == expected_output #Проверяем, что результат process() равен expected_output.

