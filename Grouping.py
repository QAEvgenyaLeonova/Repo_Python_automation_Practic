import pytest
'''Если тестов много, вы можете захотеть создать тестовый класс. pytest облегчает создание классов с множеством тестов:'''

class TestClass: #тестовый класс. TEST писать обязательно!!!
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')#hasattr(object, attribute_name) — встроенная функция Python, которая проверяет, есть ли у объекта указанный атрибут (свойство или метод).

    # Ожидаем, что при попытке доступа к x.check возникнет AttributeError
def test_attribute_error_expected(self):
    x = 'hello'
    with pytest.raises(ArithmeticError):
        _ = x.check


    def test_three(self):
        x = 'hello'.upper()
        assert hasattr(x, 'upper')#hasattr(object, attribute_name) — встроенная функция Python, которая проверяет, есть ли у объекта указанный атрибут (свойство или метод).





import unittest

class TestHasattr(unittest.TestCase):

    def test_string_has_upper_method(self):
        x = 'hello'
        # Тест проходит: у строк есть метод upper
        assert hasattr(x, 'upper')

    def test_custom_object_has_check_attribute(self):
        class MyClass:
            check = True

        x = MyClass()
        # Тест проходит: у MyClass есть атрибут check
        assert hasattr(x, 'check')

    def test_string_does_not_have_check_attribute(self):
        x = 'hello'
        # Тест проходит: у строк нет атрибута check
        assert not hasattr(x, 'check')

if __name__ == '__main__':
    unittest.main()
