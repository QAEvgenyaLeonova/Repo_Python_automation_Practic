# Файл: zoo.py

from animals import Animal, Dog, Cat, Duck

def zoo_concert(animals_list):
    """
    Функция, демонстрирующая полиморфизм:
    принимает список животных и заставляет каждое издать звук.
    Не важно, кто это — собака, кошка или утка.
    Главное, чтобы у объекта был метод make_sound().
    """
    print("=== КОНЦЕРТ В ЗООПАРКЕ ===")
    for animal in animals_list:
        animal.make_sound()  # один вызов — разное поведение!
