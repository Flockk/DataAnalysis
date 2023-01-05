"""
Реализуйте класс House, который содержит три атрибута:
- количество этажей (например, 10),
- цвет (белый),
- наличие балконов (да),
Все три атрибута должны инициализироваться при создании
экземпляра класса (то есть передаваться в init).
Также добавьте описание класса (документацию) и
создайте несколько экземпляров класса для теста.
"""


class House:
    """House description"""

    def __init__(self, count_floors, color, has_balcony):
        self.count_floors = count_floors
        self.color = color
        self.has_balcony = has_balcony


if __name__ == "__main__":
    first_house = House(2, 'green', 'no')
    second_house = House(5, 'red', 'yes')
    third_house = House(9, 'white', 'yes')
    print("The first house:"
          "\nCount of floors:", first_house.count_floors,
          "\nColor:", first_house.color,
          "\nThe presence of a balcony:", first_house.has_balcony)

    print("\nThe second house:"
          "\nCount of floors:", second_house.count_floors,
          "\nColor:", second_house.color,
          "\nThe presence of a balcony:", second_house.has_balcony)

    print("\nThe third house:"
          "\nCount of floors:", third_house.count_floors,
          "\nColor:", third_house.color,
          "\nThe presence of a balcony:", third_house.has_balcony)
