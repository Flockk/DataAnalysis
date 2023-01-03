"""
Здесь информация делится на два словаря:
первый отвечает за коды (id) товаров,
второй — за списки количества товаров,
которые есть в наличии в магазине.
Напишите программу, которая рассчитывает,
на какую сумму лежит каждого товара
и выводит эту информацию на экран.
"""

ids = {
    't-shirt': '10',
    'sneakers': '20',
    'trousers': '30',
    'cap': '40',
    'jacket': '50'
}

store = {
    '10': [
        {'quantity': 50, 'price': 800},
        {'quantity': 70, 'price': 950},
    ],
    '20': [
        {'quantity': 6, 'price': 5000},
        {'quantity': 12, 'price': 6000},
        {'quantity': 18, 'price': 4500},
    ],
    '30': [
        {'quantity': 22, 'price': 1200},
        {'quantity': 50, 'price': 1150},
    ],
    '40': [
        {'quantity': 5, 'price': 600},
    ],
    '50': [
        {'quantity': 11, 'price': 15000},
    ]
}

total_quantity = 0
total_cost = 0

for item_name, item_code in ids.items():
    for item in store[item_code]:
        total_quantity += item['quantity']
        total_cost += item['quantity'] * item['price']
    print(f'{item_name} - {total_quantity} pieces, worth {total_cost} rub')
