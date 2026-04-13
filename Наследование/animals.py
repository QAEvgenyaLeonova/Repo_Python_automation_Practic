class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):#создай_звук, метод, который будет переопределён в дочерних классах
        print(f'{self.name} издаёт какой то звук...')

    def eat(self):#кушать ,  общий метод
        print(f'{self.name} ест.')