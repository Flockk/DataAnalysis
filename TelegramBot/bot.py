import logging
import sqlite3
import time
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'TOKEN_BOT'

# Переменные для хранения введенных данных
place_name = None
country = None
city = None
street = None
house_number = None
current_state = None

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Подключение к базе данных
conn = sqlite3.connect('addresses.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы, в которой будут храниться адреса
cursor.execute("""
    CREATE TABLE IF NOT EXISTS addresses (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        place_name TEXT NULL,
        country TEXT NULL,
        city TEXT NULL,
        street TEXT NULL,
        house_number INTEGER NOT NULL
    );
""")
conn.commit()


# Команда /start
@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Здравствуйте, {user_full_name}! Я ваш личный TouristBot! Я способен сохранять места для "
                        f"будущего посещения. Вот, что я умею делать:\n\n1) Используйте команду /add, чтобы добавить "
                        f"новое место в свой список. Я попрошу вас ввести адрес, и я сохраню его для вас.\n\n2) "
                        f"Используйте команду /list, чтобы просмотреть последние 10 мест, которые вы добавили в свой "
                        f"список.\n\n3) Используйте команду /reset, чтобы удалить все сохраненные места из вашего "
                        f"списка.")


# Команда /add
@dp.message_handler(commands=['add'])
async def cmd_add(message: types.Message):
    global current_state
    kb = [
        [
            types.KeyboardButton(text="Место"),
            types.KeyboardButton(text="Страна"),
            types.KeyboardButton(text="Город"),
            types.KeyboardButton(text="Улица"),
            types.KeyboardButton(text="Дом")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    current_state = None
    await message.answer("Введите информацию:", reply_markup=keyboard)


# Обработчик для всех кнопок
@dp.message_handler(lambda message: message.text in ["Место", "Страна", "Город", "Улица", "Дом"])
async def process_input(message: types.Message):
    global place_name, country, city, street, house_number, current_state

    kb = [
        [
            types.KeyboardButton(text="Место"),
            types.KeyboardButton(text="Страна"),
            types.KeyboardButton(text="Город"),
            types.KeyboardButton(text="Улица"),
            types.KeyboardButton(text="Дом")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    if message.text == "Место":
        current_state = "entering_place_name"
        await message.answer("Введите место:", reply_markup=keyboard)
    elif message.text == "Страна":
        current_state = "entering_country"
        await message.answer("Введите страну:", reply_markup=keyboard)
    elif message.text == "Город":
        current_state = "entering_city"
        await message.answer("Введите город:", reply_markup=keyboard)
    elif message.text == "Улица":
        current_state = "entering_street"
        await message.answer("Введите улицу:", reply_markup=keyboard)
    elif message.text == "Дом":
        current_state = "entering_house_number"
        await message.answer("Введите номер дома:", reply_markup=keyboard)


@dp.message_handler(lambda message: current_state == "entering_place_name")
async def process_place_name(message: types.Message):
    global place_name
    place_name = message.text
    await message.answer("Место сохранено.")


@dp.message_handler(lambda message: current_state == "entering_country")
async def process_country(message: types.Message):
    global country
    country = message.text
    await message.answer("Страна сохранена.")


@dp.message_handler(lambda message: current_state == "entering_city")
async def process_city(message: types.Message):
    global city
    city = message.text
    await message.answer("Город сохранен.")


@dp.message_handler(lambda message: current_state == "entering_street")
async def process_street(message: types.Message):
    global street
    street = message.text
    await message.answer("Улица сохранена.")


@dp.message_handler(lambda message: current_state == "entering_house_number")
async def process_house_number(message: types.Message):
    global house_number
    house_number = message.text
    await message.answer("Номер дома сохранен.")


# Команда /list
@dp.message_handler(commands=['list'])
async def cmd_done(message: types.Message):
    global place_name, country, city, street, house_number, current_state
    result = (
        f"Место: {place_name}\n"
        f"Страна: {country}\n"
        f"Город: {city}\n"
        f"Улица: {street}\n"
        f"Номер дома: {house_number}"
    )
    await message.answer(result)


# Команда /reset
@dp.message_handler(commands=['reset'])
async def cmd_reset(message: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
