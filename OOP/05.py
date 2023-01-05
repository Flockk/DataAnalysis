"""
Даны два типа автомобилей - легковой и грузовой.
У каждого из этих автомобилей есть свой производитель,
и каждый может сделать три действия: сообщить своего производителя,
ехать и остановиться. Реализуйте классы легкового и грузового автомобилей.
Для этого выделите общие атрибуты и методы в отдельный класс «Автомобиль» и используйте наследование.
"""


class Car:
    """Описание автомобиля"""

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
        self.speed = 0

    def get_manufacturer(self):
        """Вывод производителя автомобиля"""
        return self.manufacturer

    def go(self, speed):
        """Вывод скорости автомобиля"""
        self.speed = speed
        return self.speed

    def stop(self):
        """Вывод сообщения об остановке"""
        self.speed = 0
        return "Автомобиль совершил остановку!"


class PassengerCar(Car):
    """Описание легкового автомобиля"""

    def __init__(self, manufacturer, horsepower):
        self.horsepower = horsepower
        super().__init__(manufacturer)

    def jump(self):
        """Вывод сообщения об подпрыгивании автомобиля"""
        return "Легковой автомобиль подпрыгнул на кочке!"


class Truck(Car):
    """Описание грузового автомобиля"""

    def __init__(self, manufacturer):
        self.fullness = 0
        super().__init__(manufacturer)

    def load(self, weight):
        """Погрузка груза в автомобиль"""
        self.fullness += weight
        return self.fullness

    def unload(self, weight):
        """Выгрузка груза из автомобиля"""
        self.fullness -= weight
        return self.fullness


if __name__ == '__main__':
    passenger_car = PassengerCar('Reno', 240)
    truck = Truck('Volvo')

    print(f'Марка легкового автомобиля: {passenger_car.get_manufacturer()}'
          f'\nСкорость легкового автомобиля составляет {passenger_car.go(120)} км / ч'
          f'\n{passenger_car.jump()}'
          f'\n{passenger_car.stop()}')

    print(f'\nМарка грузового автомобиля: {truck.get_manufacturer()}'
          f'\nСкорость грузового автомобиля составляет {truck.go(80)} км / ч'
          f'\nЗагружено в грузовой автомобиль: {truck.load(50)}т'
          f'\n{truck.stop()}'
          f'\nВыгружено из грузового автомобиля: {truck.unload(25)}т')
