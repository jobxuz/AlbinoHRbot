import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

#from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.inlinekey import til
from keyboards.default.userkey import boshmenu



ADMINS = db.select_all_admin_ids()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.from_user.id
    username = message.from_user.username
    fulname = message.from_user.first_name
    date = str(message.date)
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(chat_id=chat_id,first_name=fulname,username=username,date=date)
        for admin in ADMINS:
            await bot.send_message(chat_id=admin,text=f" {message.from_user.first_name} bazaga qoshildi")
    except sqlite3.IntegrityError as err:
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=err)

    await message.answer('salom',reply_markup=boshmenu)

    user = db.select_user(chat_id=chat_id)

    # if user[4] == None:
    #     await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)
    # else:
    #     await message.answer('salom')
