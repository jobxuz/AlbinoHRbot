from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import db


boshmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏢 Kompaniya haqida"),
        ],
        [
            KeyboardButton(text="💼 Bo'sh ish o'rinlari"),
        ]
    ],
    resize_keyboard=True
)



#buttins = ["Ofis","Ombor","Do'kon"]
#buttins = db.select_all_bolim()

def bolim_Buttins():
    filial = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    for buttin in db.select_all_bolim():
        filial.insert(KeyboardButton(text=buttin[0]))
    filial.insert(KeyboardButton(text="Bosh menu"))

    return filial


#ofis = ["Hr","SMM","Kassir","Bugalter"]


def ofis_Buttins():
    ofisButtin = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    for x in db.select_all_ofis():
        ofisButtin.insert(KeyboardButton(text=x[0]))
    ofisButtin.insert(KeyboardButton(text="Bosh menu"))

    return ofisButtin


#ombor = ["Yuklovchi","Tayyorlovchi","Haydovchi"]

def ombor_Buttins():
    omborButtin = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    for x in db.select_all_ombor():
        omborButtin.insert(KeyboardButton(text=x[0]))
    omborButtin.insert(KeyboardButton(text="Bosh menu"))

    return omborButtin


#dokon = ["Sotuvchi"]

def dokon_Buttins():
    dokonbuttin = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    for x in db.select_all_dokon():
        dokonbuttin.insert(KeyboardButton(text=x[0]))
    dokonbuttin.insert(KeyboardButton(text="Bosh menu"))

    return dokonbuttin



