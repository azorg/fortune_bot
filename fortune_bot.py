#!/usr/bin/env python3
# -*- coding: utf8 -*-

from aiogram import Bot, Dispatcher, executor, types
import subprocess as sp

# токен, полученный от @BotFather
from secret_bot import API_TOKEN

# команды запуска
FORTUNE = "/usr/games/fortune"
UPTIME = "uptime -p"
SENSORS = "sensors -A"
CPUINFO = ["sh",  "-c",
           "cat /proc/cpuinfo | grep 'model name' | head -n1 | " + \
           "cut -d: -f2 | sed -r 's/  */ /g' | sed -r 's/^ *| *$//'"]
DISK = ["sh", "-c",
        "LC_ALL=C df -Phl -x tmpfs | grep -v '/dev$'"]
    
BOT = Bot(token=API_TOKEN)
DP = Dispatcher(BOT)

# обработка команды /start
@DP.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   # код работает асинхронно, а потому обязательно пишем await
   await message.reply(\
       "Привет!\n" + \
       "Я бот, который отвечает случайными афоризмами на русском языке.\n")

# обработка команды /help
@DP.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(\
       "Я бот, который отвечает случайными афоризмами на русском языке и БОЛЬШЕ НИЧЕГО!\n\n" +
       "Но есть несколько команд:\n" + \
       "/help - помощь;\n" + \
       "/sources - ссылка на исходные коды бота;\n" + \
       "/uptime - время работы сервера;\n" + \
       "/sens - показания датчиков (температура, обороты кулера и т.п.);\n" + \
       "/disk - размер дисков (в т.ч. использованное пространство) на 'сервере';\n" + \
       "/cpu - тип процессора на 'сервере';\n" + \
       "/donate - номер СБЕР карты для добровольных пожертвований.\n")

# обработка команды /sources
@DP.message_handler(commands=['sources'])
async def send_welcome(message: types.Message):
    await message.reply(\
        "Исходные тексты бота на Python доступны тут: " + \
        "https://github.com/azorg/fortune_bot\n")

# обработка команды /uptime
@DP.message_handler(commands=['uptime'])
async def send_welcome(message: types.Message):
    res = sp.run(UPTIME.split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
    await message.answer(res.stdout)

# обработка команды /sens
@DP.message_handler(commands=['sens'])
async def send_welcome(message: types.Message):
    res = sp.run(SENSORS.split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
    await message.answer(res.stdout)

# обработка команды /disks
@DP.message_handler(commands=['disk'])
async def send_welcome(message: types.Message):
    res = sp.run(DISK, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
    await message.answer(res.stdout)

# обработка команды /cpu
@DP.message_handler(commands=['cpu'])
async def send_welcome(message: types.Message):
    res = sp.run(CPUINFO, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
    await message.answer(res.stdout)

# обработка команды /doname
@DP.message_handler(commands=['donate'])
async def send_welcome(message: types.Message):
    await message.reply(\
        "Любые добровольные пожертвования принимаются в рублях " + \
        "на СБЕР карту 4817 7603 2192 0930\n")

# событие, которое запускается в ответ на любой текст, введённый пользователем.
@DP.message_handler()
async def echo(message: types.Message):
    # TODO: можно обработать то, что вводит пользователь, но пока просто вывод на stdout
    print(message)
    msg = ""
    if (len(message.text) > 3):
        msg = "Мне все равно, что Вы мне пишите.\n" + \
              "Вот Вам ещё один афоризм:\n\n"
    res = sp.run(FORTUNE.split(), stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
    await message.answer(msg + res.stdout)

def main():
    executor.start_polling(DP, skip_updates=True)

if __name__ == '__main__':
    main()

#*** end of "fortune_bot.py" file ***#

