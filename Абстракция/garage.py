from vehicles import  Vehicle

def service_vehicle(vehicle):#служебное транспортное средство
    """
    Функция для обслуживания транспорта.
    Принимает ЛЮБОЙ объект, который является Vehicle (соответствует контракту).
    Не важно, что это — машина, мотоцикл или самокат.
    Главное, чтобы у него были методы start_engine() и get_fuel_type().
    """
    print('\n--- Начинаем обслуживание транспорта ---')
    vehicle.start_engine()
    fuel = vehicle.get_fuel_type()
    print(f'Тип топлива: {fuel}')
    print('Обслужвание завершено!\n')