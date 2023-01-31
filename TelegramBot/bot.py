import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'TOKEN_BOT'

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


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
    address = await dp.message_handler()
    await message.answer("Адрес добавлен успешно!")
    pass


# Команда /list
@dp.message_handler(commands=['list'])
async def cmd_list(message: types.Message):
    await message.answer("Последние 10 добавленных мест:")
    pass


# Команда /reset
@dp.message_handler(commands=['reset'])
async def cmd_reset(message: types.Message):
    await message.answer("Все добавленные адреса были удалены.")
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
