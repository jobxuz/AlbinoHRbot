import asyncio

from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import ContentType
from data.config import ADMINS
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from keyboards.default.adminKey import adminusers,admincommands
from keyboards.inline.inlinekey import rek
from keyboards.default.userkey import boshmenu


class Reklama(StatesGroup):
    message = State()

class Bolim(StatesGroup):
    message = State()



@dp.message_handler(text="/start", user_id=ADMINS)
async def get_all_users(message: types.Message):

    #await message.answer('admin panel',reply_markup=admincommands)
    await bot.send_message(chat_id=ADMINS[0],text='Siz adminsiz',reply_markup=admincommands)




@dp.message_handler(text="admin panel", user_id=ADMINS)
async def get_all_users(message: types.Message):

    await message.answer('admin panel',reply_markup=adminusers)




@dp.message_handler(text="users", user_id=ADMINS)
async def get_all_users(message: types.Message):
    count = db.count_users()
    users = db.select_all_users()
    text = f"instabot || Foydalanuvchilar soni: {count[0]}\n\n"
    for user in users:
        text+= f"{user[0]}). || {user[2]} || @{user[3]}\n"
    await message.answer(text)


@dp.message_handler(text="back", user_id=ADMINS)
async def back_button(message: types.Message):

    await message.answer('Bosh menyu',reply_markup=admincommands)


@dp.message_handler(text="reklama",user_id=ADMINS)
async def bot_start(message: types.Message):
    await message.answer("reklama yuboring")
    await Reklama.message.set()


@dp.message_handler(content_types=ContentType.ANY,state=Reklama.message)
async def answer_fullname(message: types.Message, state: FSMContext):
    habar = message.text

    await state.update_data(
        {"habar": habar}
    )
    data = await state.get_data()
    reklama = data.get("habar")

    msg = reklama
    users = db.select_all_users()
    for user in users:
        user_id = user[1]
        try:
            await message.send_copy(chat_id=user_id)
            await asyncio.sleep(0.05)
        except Exception as e:
            await bot.send_message(chat_id=ADMINS[0],text=f"{e}")
    await bot.send_message(chat_id=ADMINS[0],text=f"Reklama yuborildi! ✅")
    await state.finish()



@dp.message_handler(text="hr", user_id=ADMINS)
async def hr(message: types.Message):

    #await message.answer('admin panel',reply_markup=admincommands)
    await bot.send_message(chat_id=ADMINS[0],text='Siz adminsiz',reply_markup=boshmenu)


@dp.message_handler(text="bolim qoshish", user_id=ADMINS)
async def bolim(message: types.Message):

    await message.answer("Bo'lim nomini yozing!")
    await Bolim.message.set()


@dp.message_handler(state=Bolim.message)
async def bolimqoshish(message: types.Message,state: FSMContext):
    habar = message.text

    # await state.update_data(
    #     {"habar": habar}
    # )
    # data = await state.get_data()
    # name_bolim = data.get("habar")


    db.add_bolim(name=habar)

    bolimlar = db.select_all_bolim()

    await message.answer(text=f"Bo'lim qo'shildi!!! \n {bolimlar}")

    await state.finish()
