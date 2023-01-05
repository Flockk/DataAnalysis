"""
Реализуйте класс Event, который отвечает за событие в календаре.
Экземпляр класса имеет два атрибута: описание события и дату события.
Внутри класса реализуйте метод, который конвертирует строку в объект класса Event.
Метод получает на вход строку вида ‘description * dd-mm-yyyy’.
"""


class Event:
    """Описание события"""

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        """Информация о событии"""
        return f'Description: {self.description}\nDate:{self.date}'

    @classmethod
    def str_to_obj(cls, string):
        """Конвертация строки в объект класса Event"""
        description, event_date = string.split('*')
        return cls(description, event_date)


new_event = Event.str_to_obj('Meeting with friends * 12-11-2001')
print(new_event)
