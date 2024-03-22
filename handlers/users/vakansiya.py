from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from aiogram.types import InputFile
import logging

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.inlinekey import til,booksMenu
from keyboards.default.userkey import boshmenu

from aiogram.types import ReplyKeyboardRemove
from reportlab.lib.utils import ImageReader
from aiogram.types import ContentType

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboards.default.stateKey import studentkey,sogliqkey,phonkey,yuborishkey
from keyboards.default.userkey import bolim_Buttins,ofis_Buttins,ombor_Buttins,dokon_Buttins

from handlers.users.hr import create_image_with_greeting



@dp.message_handler(text="🏢 Kompaniya haqida")
async def kompaniya(message:types.Message):
    photo_file = InputFile(path_or_bytesio="/home/container/handlers/users/file/imgs/kompaniya.jpg")
    await message.reply_photo(
        photo_file, caption="""Bizning kompaniyamiz 2009-yildan beri oshxona anjomlari va kichik
        turdagi maishiy texnikalar savdosi bilan xaridorlarga xizmat korsatib keladi.
        Aynan 2016-yildan boshlab “albino” korxonasi sifatida faoliyat korsatib kelmoqda.
        Hozirgi kunda kompaniyamizda 8 ta savdo nuqtasi va yirik omborlari mavjud. 
        Jamoamizda ayni damda 70 dan ortiq hodimlar faoliyat yurutib kelmoqda. """
    )



@dp.message_handler(text="Bosh menu",state='*')
async def stateend(message:types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)

    await state.finish()
    await message.answer("Bosh menu",reply_markup=boshmenu)
    


class Vakansiya(StatesGroup):
    bolim = State()
    lavozim = State()
    name = State()
    date = State()
    phon = State()
    addres = State()
    student = State()
    sudlangan = State()
    img = State()
    sogliq = State()
    yuborish = State()





@dp.message_handler(text="💼 Bo'sh ish o'rinlari")
async def startState(message: types.Message):
    await message.answer("Bo'limni tanlang!",reply_markup=bolim_Buttins())
    await Vakansiya.bolim.set()


@dp.message_handler(state=Vakansiya.bolim)
async def answer_city(message: types.Message, state: FSMContext):
    if message.text == "Ofis":
        bolim = message.text

        await state.update_data(
            {"bolim": bolim}
        )

        await message.answer("Lavozimni tanlang!",reply_markup=ofis_Buttins())

        await Vakansiya.next()
    elif message.text == "Ombor":
        bolim = message.text

        await state.update_data(
            {"bolim": bolim}
        )

        await message.answer("Lavozimni tanlang!",reply_markup=ombor_Buttins())

        await Vakansiya.next()
    elif message.text == "Do'kon":
        bolim = message.text

        await state.update_data(
            {"bolim": bolim}
        )

        await message.answer("Lavozimni tanlang!",reply_markup=dokon_Buttins())

        await Vakansiya.next()
    else:
        await message.answer("Nomalum buyruq!")


@dp.message_handler(state=Vakansiya.lavozim)
async def answer_city(message: types.Message, state: FSMContext):
    lavozim = message.text

    await state.update_data(
        {"lavozim": lavozim}
    )

    await message.answer("To'liq ismingizni yozing!",reply_markup=ReplyKeyboardRemove())

  
    await Vakansiya.next()


@dp.message_handler(state=Vakansiya.name)
async def answer_city(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )

    await message.answer("To'g'ilgan yilingiz!  Misol:07.07.1999")

    await Vakansiya.next()


@dp.message_handler(state=Vakansiya.date)
async def answer_city(message: types.Message, state: FSMContext):
    date = message.text

    await state.update_data(
        {"date": date}
    )

    await message.answer("Telefon nomeringiz!",reply_markup=phonkey)

    # await PersonalData.email.set()
    await Vakansiya.next()


@dp.message_handler(state=Vakansiya.phon,content_types=types.ContentTypes.CONTACT)
async def answer_city(message: types.Message, state: FSMContext):
    phon = message.contact.phone_number

    await state.update_data(
        {"phon": phon}
    )

    await message.answer("Yashash manzilingiz! Misol: Qashqadaryo viloyati",reply_markup=ReplyKeyboardRemove())

    # await PersonalData.email.set()
    await Vakansiya.next()




@dp.message_handler(state=Vakansiya.addres)
async def answer_city(message: types.Message, state: FSMContext):
    addres = message.text

    await state.update_data(
        {"addres": addres}
    )

    await message.answer("Siz studentmisz!",reply_markup=studentkey)

    # await PersonalData.email.set()
    await Vakansiya.next()



@dp.message_handler(state=Vakansiya.student)
async def answer_city(message: types.Message, state: FSMContext):
    student = message.text

    await state.update_data(
        {"student": student}
    )

    await message.answer("Sudlanganmisz!")

    # await PersonalData.email.set()
    await Vakansiya.next()


@dp.message_handler(state=Vakansiya.sudlangan)
async def answer_city(message: types.Message, state: FSMContext):
    sudlangan = message.text

    await state.update_data(
        {"sudlangan": sudlangan}
    )

    await message.answer("Shaxsiy rasmingizni yuboring!",reply_markup=ReplyKeyboardRemove())

    # await PersonalData.email.set()
    await Vakansiya.next()




@dp.message_handler(content_types=ContentType.ANY,state=Vakansiya.img)
async def answer_img(message: types.Message, state: FSMContext):
    if message.content_type == ContentType.PHOTO:
        photo = message.photo[-1]
        file_id = photo.file_id
        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path

    # Rasmni faylga yuklash
        await bot.download_file(file_path, f"handlers/users/file/imgs/{message.from_user.id}.jpg")
        #await message.photo[-1].download()
        await message.answer("Sog'ligingizda hammasi joyidam!",reply_markup=sogliqkey)
        await Vakansiya.next()
    else:
        await message.answer("Rasm yuboring!!")




@dp.message_handler(state=Vakansiya.sogliq)
async def answer_city(message: types.Message, state: FSMContext):
    sogliq = message.text

    await state.update_data(
        {"sogliq": sogliq}
    )

    data = await state.get_data()
    bolim = data.get("bolim")
    lavozim = data.get("lavozim")
    name = data.get("name")
    date = data.get("date")
    phon = data.get("phon")
    addres = data.get("addres")
    student = data.get("student")
    sudlangan = data.get("sudlangan")
    sogliq = data.get("sogliq")


    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Bo'lim - {bolim}\n"
    msg += f"Lavozim - {lavozim}\n"
    msg += f"Ism: - {name}\n"
    msg += f"tug'ilgan sana: - {date}\n"
    msg += f"Telefon nomer: - {phon}\n"
    msg += f"Manzil: - {addres}\n"
    msg += f"Talabamisz: - {student}\n"
    msg += f"Sudlanganmisz: - {sudlangan}\n"
    msg += f"Sog'ligingiz: - {sogliq}\n\n"
    msg += f"Ma'lumotlaringiz to'g'rimi!"

    await message.answer(msg,reply_markup=yuborishkey)


    malumotlar = [bolim,lavozim,name,date,phon,addres,student,sudlangan,sogliq]


    #await bot.send_message(chat_id=1363350178,text=malumotlar)

    img = f"/home/container/handlers/users/file/imgs/{message.from_user.id}.jpg"
    file = f"/home/container/handlers/users/file/files/{message.from_user.id}.pdf"
    
    
    create_image_with_greeting(file,img,malumotlar)

    await Vakansiya.next()



@dp.message_handler(state=Vakansiya.yuborish)
async def yuborish(message: types.Message,state: FSMContext):
    if message.text == "Yuborish":
        await message.answer("Yuborildi!!!",reply_markup=boshmenu)
        await state.finish()
        files = f"C:/home/container/handlers/users/file/files/{message.from_user.id}.pdf"
        with open(files, "rb") as file:
        # Document jo'natish
            await bot.send_document(chat_id=message.from_user.id, document=file)
        with open(files, "rb") as file:
        # Document jo'natish
            await bot.send_document(chat_id=ADMINS[0], document=file)
    elif message.text == "Rad etish":
        await message.answer("Rad etildi",reply_markup=boshmenu)
        await state.finish()
        await message.answer("Malumotlar yuborilmadi!")

    


