import asyncio
from idlelib.undo import Command

from aiogram import Bot, Dispatcher, F

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from pyexpat.errors import messages

from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()
photo_list = ['cat.jpeg', 'Cat1.jpeg', 'Cat2.webp']
@dp.message(Command('photo'))
async def send_random_photo(message: Message):
    rand_photo = random.choice(photo_list)
    await message.answer_photo(photo=rand_photo, caption='Это зачетный кошак!')



@dp.message(F.photo)
async def react_photo(message: Message):
    photo_list = ['cat.jpeg', 'Cat1.jpeg', 'Cat2.webp']
    rand_answ = random.choice(photo_list)
    await message.answer(rand_answ)




@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('')




@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')

@dp.message(CommandStart)
async def start(message: Message):
    await  message.answer('Приветики! Я бот!')



async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())