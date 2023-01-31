import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'TOKEN_BOT'

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
    await message.answer("Здравствуйте! Я ваш личный TouristBot! Я способен сохранять места для будущего посещения. "
                         "Вот, что я умею делать:\n\n1) Используйте команду /add, чтобы добавить новое место в свой "
                         "список. Я попрошу вас ввести адрес, и я сохраню его для вас.\n\n2) Используйте команду /list,"
                         "чтобы просмотреть последние 10 мест, которые вы добавили в свой список.\n\n3) Используйте "
                         "команду /reset, чтобы удалить все сохраненные места из вашего списка.")


# Команда /add
@dp.message_handler(commands=['add'])
async def cmd_add(message: types.Message):
    await message.answer("Пожалуйста, введите адрес, который вы хотите добавить:")
    pass


# Команда /list
@dp.message_handler(commands=['list'])
async def cmd_list(message: types.Message):
    await message.answer("Последние 10 добавленных мест:")
    pass


# Команда /reset
@dp.message_handler(commands=['reset'])
async def cmd_reset(message: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
