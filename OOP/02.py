"""
Модифицируйте класс House и добавьте в него два метода:
1. Отображение информации об объекте класса. (можно использовать метод __str__)
2. Метод, который позволяет увеличивать количество этажей (уменьшать нельзя!)
"""


class House:
    """Описание дома"""

    def __init__(self, count_floors, color, has_balcony):
        self.count_floors = count_floors or []
        self.color = color
        self.has_balcony = has_balcony

    def __str__(self):
        """Информация о доме"""
        return f"\nКоличество этажей: {self.count_floors}" \
               f"\nЦвет: {self.color}" \
               f"\nНаличие балкона: {self.has_balcony}"

    def add_floor(self, floor: int):
        """Увеличение количества этажей"""
        self.count_floors += floor


if __name__ == "__main__":
    first_house = House(2, 'зелёный', 'нет')
    second_house = House(5, 'бежевый', 'да')
    third_house = House(9, 'белый', 'да')

    print('\tИнформация о домах:',
          f'\n\nПервый дом: {first_house}'
          f'\n\nВторой дом: {second_house}'
          f'\n\nТретий дом: {third_house}')

    print('\n\tУвеличение количества этажей:'
          f'\n\nБыло этажей в первом доме: {first_house.count_floors}',
          f'\nБыло этажей во втором доме: {second_house.count_floors}'
          f'\nБыло этажей в третьем доме: {third_house.count_floors}')

    first_house.add_floor(2)
    second_house.add_floor(5)
    third_house.add_floor(9)

    print(f'\nСтало этажей в первом доме: {first_house.count_floors}',
          f'\nСтало этажей во втором доме: {second_house.count_floors}'
          f'\nСтало этажей в третьем доме: {third_house.count_floors}')
