# Файл: vehicles.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Абстрактный класс — «чертёж» для всех видов транспорта."""

    @abstractmethod
    def start_engine(self):
        """Абстрактный метод — должен быть реализован в каждом дочернем классе.
        Описывает, как запускается двигатель, но не содержит реализации."""
        pass

    @abstractmethod
    def get_fuel_type(self):
        """Ещё один абстрактный метод — каждый транспорт должен указать тип топлива."""
        pass

class Car(Vehicle):
    def start_engine(self):
        print("🚗 Автомобиль завёлся с характерным звуком двигателя!")

    def get_fuel_type(self):
        return "бензин"

class Bike(Vehicle):
    def start_engine(self):
        print("🏍️ Мотоцикл завёлся с громким рёвом!")

    def get_fuel_type(self):
        return "бензин"

class ElectricScooter(Vehicle):
    def start_engine(self):
        print("☁️ Электросамокат включился бесшумно!")

    def get_fuel_type(self):
        return "электричество"
