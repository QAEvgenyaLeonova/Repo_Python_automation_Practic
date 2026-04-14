# Файл: main.py
from animals import Dog, Cat, Duck
from zoo import zoo_concert

# Создаём разных животных
dog = Dog("Бобик")
cat = Cat("Мурзик")
duck = Duck("Дональд")

# Собираем их в один список
zoo_animals = [dog, cat, duck]

# Запускаем концерт — демонстрируем полиморфизм!
zoo_concert(zoo_animals)
