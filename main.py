from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6157596715:AAFaJ0TdMj2AbdOkENUymVmKAdaxmHzSIBU')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Web Page', web_app=WebAppInfo(url= 'https://www.xdao.app/137/dao/0x75a8e509644f5508118a07093C028C4a84aC0863')))
    await message.answer('Hello world! Please! Press the button on the Keyboard ', reply_markup=markup)

executor.start_polling(dp)