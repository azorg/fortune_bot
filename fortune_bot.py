#!/usr/bin/env python3
# -*- coding: utf8 -*-

from aiogram import Bot, Dispatcher, executor, types
import subprocess as sp

# токен, полученный от @BotFather
from secret_bot import API_TOKEN

# команда запуска fortune
CMD = "/usr/games/fortune"
    
BOT = Bot(token=API_TOKEN)
DP = Dispatcher(BOT)

# обработка команды /start
@DP.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   # код работает асинхронно, а потому обязательно пишем await
   await message.reply(\
       "Привет!\n" + \
       "Я бот, который овечает случайными афоризмами на русском языке\n")

# обработка команды /help
@DP.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
   await message.reply(\
       "Я бот, который овечает случайными афоризмами на русском языке и БОЛЬШЕ НИЧЕГО!\n" + \
       "Исходные тексты доступны: https://github.com/azorg/fortune_bot/\n")

# событие, которое запускается в ответ на любой текст, введённый пользователем.
@DP.message_handler()
async def echo(message: types.Message):
   # TODO: можно обработать то, что вводит пользователь, но пока просто печать
   msg = ""
   if (len(message.text) > 2):
      msg = "Мне все равно, что Вы мне пишите.\n" + \
            "Вот вам просто еще одна шуточка:\n"
   print(message)
   res = sp.run(CMD.split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
   await message.answer(msg + res.stdout)

def main():
    executor.start_polling(DP, skip_updates=True)

if __name__ == '__main__':
    main()

#*** end of "fortune_bot.py" file ***#

