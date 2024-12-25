import asyncio

from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import ContentType
#from data.config import ADMINS
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from keyboards.default.adminKey import adminusers,admincommands
from keyboards.inline.inlinekey import rek
from keyboards.default.userkey import boshmenu
#from handlers.users.adminlistdata import admins_list




ADMINS = db.select_all_admin_ids()


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


class Admins(StatesGroup):
    name = State()
    admin_id = State()


class Admin_delete(StatesGroup):
    name = State()




@dp.message_handler(text="/start", user_id=ADMINS)
async def get_all_users(message: types.Message):

    #await message.answer('admin panel',reply_markup=admincommands)
    await bot.send_message(chat_id=message.from_user.id,text='Siz adminsiz',reply_markup=admincommands)




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
    await bot.send_message(chat_id=message.from_user.id,text='Siz adminsiz',reply_markup=boshmenu)


@dp.message_handler(text="bo'lim qo'shish", user_id=ADMINS)
async def bolim(message: types.Message):

    await message.answer("Bo'lim nomini yozing!")
    await Bolim.message.set()


@dp.message_handler(state=Bolim.message)
async def bolimqoshish(message: types.Message,state: FSMContext):
    habar = message.text



    db.add_bolim(name=habar)

    #bolimlar = db.select_all_bolim()

    text  = f"Bo'lim qo'shildi!  Mavjud bo'limlar:\n\n"
    id = 1
    for i in db.select_all_bolim():
        text+=f"{id}) {i[0]}\n"
        id=id+1
    await message.answer(text)

    await state.finish()


@dp.message_handler(text="delete bo'lim", user_id=ADMINS)
async def bolim_delete(message: types.Message):

    await message.answer("Bo'lim nomini yozing!")
    await Bolim_delete.bolim.set()


@dp.message_handler(state=Bolim_delete.bolim)
async def bolimdelete(message: types.Message,state: FSMContext):
    habar = message.text



    db.delete_bolim(name=habar)

    #bolimlar = db.select_all_bolim()

    text  = f"Bo'lim o'chirildi!  Mavjud bo'limlar:\n\n"
    id = 1
    for i in db.select_all_bolim():
        text+=f"{id}) {i[0]}\n"
        id=id + 1
    await message.answer(text)


    await state.finish()





@dp.message_handler(text="ofis qo'shish", user_id=ADMINS)
async def bolim(message: types.Message):

    await message.answer("Ofisga qo'shmoqchi bo'lgan bo'sh ish o'rni nomini yozing!")
    await Ofis.message.set()


@dp.message_handler(state=Ofis.message)
async def ofisqoshish(message: types.Message,state: FSMContext):
    habar = message.text



    db.add_ofis(name=habar)

    text  = f"Ofisga yangi bo'sh ish o'rni qo'shildi! Mavjud bo'sh ish o'rinlari!\n\n"
    id = 1
    for i in db.select_all_ofis():
        text+=f"{id}) {i[0]}\n"
        id=id+1
    await message.answer(text)

    await state.finish()


@dp.message_handler(text="delete ofis", user_id=ADMINS)
async def ofis_delete(message: types.Message):

    await message.answer("Ofisda o'chirmoqchi bo'lgan bo'sh ish o'rni nomini yozing!")
    await Ofis_delete.bolim.set()


@dp.message_handler(state=Ofis_delete.bolim)
async def bolimdelete(message: types.Message,state: FSMContext):
    habar = message.text



    db.delete_ofis(name=habar)

    text  = f"Ofisdagi bitta bo'sh ish o'rni o'chirildi,  Mavjud bo'sh ish o'rinlari:\n\n"
    id = 1
    for i in db.select_all_ofis():
        text+=f"{id}) {i[0]}\n"
        id=id + 1
    await message.answer(text)

    await state.finish()

#--------------------------------------------------------------------------------------#




@dp.message_handler(text="ombor qo'shish", user_id=ADMINS)
async def ombor(message: types.Message):

    await message.answer("Omborga qo'shmoqchi bo'lgan bo'sh ish o'rni nomini yozing!")
    await Ombor.message.set()


@dp.message_handler(state=Ombor.message)
async def omborqoshish(message: types.Message,state: FSMContext):
    habar = message.text



    db.add_ombor(name=habar)

    text  = f"Omborga yangi bo'sh ish o'rni qo'shildi, Mavjud bo'sh ish o'rinlari:\n\n"
    id = 1
    for i in db.select_all_ombor():
        text+=f"{id}) {i[0]}\n"
        id=id+1
    await message.answer(text)

    await state.finish()


@dp.message_handler(text="delete ombor", user_id=ADMINS)
async def ombor_delete(message: types.Message):

    await message.answer("Omborda o'chirmoqchi bo'lgan bo'sh ish o'rni nomini yozing!")
    await Ombor_delete.message.set()


@dp.message_handler(state=Ombor_delete.message)
async def bolimdelete(message: types.Message,state: FSMContext):
    habar = message.text



    db.delete_ombor(name=habar)

    text  = f"Ombordagi bitta bo'sh ish o'rni o'chirildi,  Mavjud bo'sh ish o'rinlari:\n\n"
    id = 1
    for i in db.select_all_ombor():
        text+=f"{id}) {i[0]}\n"
        id=id + 1
    await message.answer(text)

    await state.finish()

#--------------------------------------------------------------------------------------#



@dp.message_handler(text="do'kon qo'shish", user_id=ADMINS)
async def dokon(message: types.Message):

    await message.answer("Do'konga qo'shmoqchi bo'lgan bo'sh ish o'rni nomini yozing!")
    await Dokon.message.set()


@dp.message_handler(state=Dokon.message)
async def dokonqoshish(message: types.Message,state: FSMContext):
    habar = message.text



    db.add_dokon(name=habar)

    text  = f"Do'konga yangi bo'sh ish o'rni qo'shildi!  Mavjud bo'limlar:\n\n"
    id = 1
    for i in db.select_all_dokon():
        text+=f"{id}) {i[0]}\n"
        id=id+1
    await message.answer(text)

    await state.finish()


@dp.message_handler(text="delete do'kon", user_id=ADMINS)
async def dokon_delete(message: types.Message):

    await message.answer("Do'konda o'chirmoqchi bo'lgan bo'sh ish o'rni nomini yozing")
    await Dokon_delete.message.set()


@dp.message_handler(state=Dokon_delete.message)
async def bolimdelete(message: types.Message,state: FSMContext):
    habar = message.text



    db.delete_dokon(name=habar)

    text  = f"Do'kondagi bitta bo'sh ish o'rni o'chirildi!  Mavjud bo'limlar:\n\n"
    id = 1
    for i in db.select_all_dokon():
        text+=f"{id}) {i[0]}\n"
        id=id+1
    await message.answer(text)

    await state.finish()

#--------------------------------------------------------------------------------------#

@dp.message_handler(text="mavjud bo'limlar", user_id=ADMINS)
async def bolim(message: types.Message):
    text  = f"Hozirda mavjud bo'limlar:\n\n"
    id = 1
    for i in db.select_all_bolim():
        text+=f"{id}) {i[0]}\n"
        id=id+1
    await message.answer(text)

    

@dp.message_handler(text="mavjud ofislar", user_id=ADMINS)
async def bolim(message: types.Message):
    text  = f"Hozirda mavjud ofislar:\n\n"
    id = 1
    for i in db.select_all_ofis():
        text+=f"{id}) {i[0]}\n"
        id=id+1
    await message.answer(text)



@dp.message_handler(text="mavjud omborlar", user_id=ADMINS)
async def bolim(message: types.Message):
    text  = f"Hozirda mavjud omborlar:\n\n"
    id = 1
    for i in db.select_all_ombor():
        text+=f"{id}) {i[0]}\n"
        id=id+1
    await message.answer(text)




@dp.message_handler(text="mavjud do'konlar", user_id=ADMINS)
async def bolim(message: types.Message):
    text  = f"Hozirda mavjud do'konlar:\n\n"
    id = 1
    for i in db.select_all_dokon():
        text+=f"{id}) {i[0]}\n"
        id=id+1
    await message.answer(text)

#--------------------------------------------------------------------------------------#

@dp.message_handler(text="admin qo'shish", user_id=ADMINS)
async def bolim(message: types.Message):

    await message.answer("Yangi admin ismini kiriting")
    await Admins.name.set()



@dp.message_handler(state=Admins.name)
async def channel_name(message: types.Message,state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )
    
    await message.answer("Admin Id sini kiriting")
    await Admins.next()



@dp.message_handler(state=Admins.admin_id)
async def channel_id(message: types.Message,state: FSMContext):
    admin_id = int(message.text)


    data = await state.get_data()
    name = data.get("name")


    try:
        db.add_admin(name, admin_id)
        await bot.send_message(chat_id=message.from_user.id,text="Admin qo'shildi")
    except Exception as e:
        await bot.send_message(chat_id=message.from_user.id,text=e)

    await state.finish()



@dp.message_handler(text="delete admin", user_id=ADMINS)
async def bolim_delete(message: types.Message):

    await message.answer("Admin ismini yozing!")
    await Admin_delete.name.set()


@dp.message_handler(state=Admin_delete.name)
async def bolimdelete(message: types.Message,state: FSMContext):
    name = message.text

    db.delete_admin(name=name)

    text  = f"Admin o'chirildi, Mavjud Adminlar\n\n"
    id = 1
    for i in db.select_all_admin():
        text+=f"{id}) {i[0]}\n"
        id=id + 1
    await message.answer(text)


    await state.finish()



@dp.message_handler(text="mavjud adminlar", user_id=ADMINS)
async def bolim(message: types.Message):
    text  = f"Hozirda mavjud adminlar:\n\n"
    id = 1
    for i in db.select_all_admin():
        text+=f"{id}) {i[0]} | {i[1]}\n"
        id=id+1
    await message.answer(text)