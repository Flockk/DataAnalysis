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
    await message.answer("Здравствуйте! Я TouristBot!\nЯ способен сохранять места для будущего посещения.")


# Команда /help
@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await message.answer("Я могу повторить ваши сообщения!")


# Отправка сообщения пользователю
@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Здравствуйте!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
