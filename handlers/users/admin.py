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

class Bolim_delete(StatesGroup):
    bolim = State()


class Ofis(StatesGroup):
    message = State()

class Ofis_delete(StatesGroup):
    bolim = State()


class Ombor(StatesGroup):
    message = State()

class Ombor_delete(StatesGroup):
    message = State()

class Dokon(StatesGroup):
    message = State()

class Dokon_delete(StatesGroup):
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



    db.add_bolim(name=habar)

    bolimlar = db.select_all_bolim()

    await message.answer(text=f"Bo'lim qo'shildi!!! \n {bolimlar}")

    await state.finish()


@dp.message_handler(text="delete bolim", user_id=ADMINS)
async def bolim_delete(message: types.Message):

    await message.answer("Bo'lim nomini yozing!")
    await Bolim_delete.bolim.set()


@dp.message_handler(state=Bolim_delete.bolim)
async def bolimdelete(message: types.Message,state: FSMContext):
    habar = message.text



    db.delete_bolim(name=habar)

    bolimlar = db.select_all_bolim()

    await message.answer(text=f"Bo'lim o'chirildi!!! \n {bolimlar}")

    await state.finish()





@dp.message_handler(text="ofis qoshish", user_id=ADMINS)
async def bolim(message: types.Message):

    await message.answer("Bo'lim nomini yozing!")
    await Ofis.message.set()


@dp.message_handler(state=Ofis.message)
async def ofisqoshish(message: types.Message,state: FSMContext):
    habar = message.text



    db.add_ofis(name=habar)

    bolimlar = db.select_all_ofis()

    await message.answer(text=f"Bo'lim qo'shildi!!! \n {bolimlar}")

    await state.finish()


@dp.message_handler(text="delete ofis", user_id=ADMINS)
async def ofis_delete(message: types.Message):

    await message.answer("Ofis nomini yozing!")
    await Ofis_delete.bolim.set()


@dp.message_handler(state=Ofis_delete.bolim)
async def bolimdelete(message: types.Message,state: FSMContext):
    habar = message.text



    db.delete_ofis(name=habar)

    bolimlar = db.select_all_ofis()

    await message.answer(text=f"Ofis o'chirildi!!! \n {bolimlar}")

    await state.finish()

#--------------------------------------------------------------------------------------#




@dp.message_handler(text="ombor qoshish", user_id=ADMINS)
async def ombor(message: types.Message):

    await message.answer("Bo'lim nomini yozing!")
    await Ombor.message.set()


@dp.message_handler(state=Ombor.message)
async def omborqoshish(message: types.Message,state: FSMContext):
    habar = message.text



    db.add_ombor(name=habar)

    bolimlar = db.select_all_ombor()

    await message.answer(text=f"Bo'lim qo'shildi!!! \n {bolimlar}")

    await state.finish()


@dp.message_handler(text="delete ombor", user_id=ADMINS)
async def ombor_delete(message: types.Message):

    await message.answer("Ofis nomini yozing!")
    await Ombor_delete.message.set()


@dp.message_handler(state=Ombor_delete.message)
async def bolimdelete(message: types.Message,state: FSMContext):
    habar = message.text



    db.delete_ombor(name=habar)

    bolimlar = db.select_all_ombor()

    await message.answer(text=f"Ofis o'chirildi!!! \n {bolimlar}")

    await state.finish()

#--------------------------------------------------------------------------------------#



@dp.message_handler(text="dokon qoshish", user_id=ADMINS)
async def dokon(message: types.Message):

    await message.answer("Bo'lim nomini yozing!")
    await Dokon.message.set()


@dp.message_handler(state=Dokon.message)
async def dokonqoshish(message: types.Message,state: FSMContext):
    habar = message.text



    db.add_dokon(name=habar)

    bolimlar = db.select_all_dokon()

    await message.answer(text=f"Bo'lim qo'shildi!!! \n {bolimlar}")

    await state.finish()


@dp.message_handler(text="delete dokon", user_id=ADMINS)
async def dokon_delete(message: types.Message):

    await message.answer("Dokon nomini yozing!")
    await Dokon_delete.message.set()


@dp.message_handler(state=Dokon_delete.message)
async def bolimdelete(message: types.Message,state: FSMContext):
    habar = message.text



    db.delete_dokon(name=habar)

    bolimlar = db.select_all_dokon()

    await message.answer(text=f"Dokon o'chirildi!!! \n {bolimlar}")

    await state.finish()

#--------------------------------------------------------------------------------------#


