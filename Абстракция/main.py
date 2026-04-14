# Файл: main.py
from vehicles import Car, Bike, ElectricScooter
from garage import service_vehicle

# Создаём разные виды транспорта
car = Car()
bike = Bike()
scooter = ElectricScooter()

# Передаём их в функцию обслуживания
# Функция работает с абстракцией Vehicle, а не с конкретными типами
service_vehicle(car)
service_vehicle(bike)
service_vehicle(scooter)
