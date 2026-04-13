from animals import Animal

class Cat(Animal):# импортируем родительский класс
    def __init__(self, name, color):
        super().__init__(name, 'Кошка')# вызываем конструктор родителя
        self.color = color
# Переопределяем метод родителя
    def make_sound(self):#создай_звук
        print(f'{self.name} говорит: Мяу!')

# Добавляем новый метод
    def purr(self):#мурлыкать
        print(f'{self.name} мурлычет: мур - мур!')
