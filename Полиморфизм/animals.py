# Файл: animals.py

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} издаёт какой‑то звук...")

class Dog(Animal):
    def make_sound(self):  # переопределяем метод
        print(f"{self.name} говорит: Гав-гав!")

class Cat(Animal):
    def make_sound(self):  # переопределяем метод
        print(f"{self.name} говорит: Мяу!")

class Duck(Animal):
    def make_sound(self):  # переопределяем метод
        print(f"{self.name} говорит: Кря-кря!")
