from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


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



buttins = ["Ofis","Ombor","Do'kon"]

filial = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
for buttin in buttins:
    filial.insert(KeyboardButton(text=buttin))
filial.insert(KeyboardButton(text="Bosh menu"))


ofis = ["Hr","SMM","Kassir","Bugalter"]

ofisButtin = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
for x in ofis:
    ofisButtin.insert(KeyboardButton(text=x))
ofisButtin.insert(KeyboardButton(text="Bosh menu"))


ombor = ["Yuklovchi","Tayyorlovchi","Haydovchi"]

omborButtin = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
for x in ombor:
    omborButtin.insert(KeyboardButton(text=x))
omborButtin.insert(KeyboardButton(text="Bosh menu"))


dokon = ["Sotuvchi"]

dokonbuttin = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
for x in dokon:
    dokonbuttin.insert(KeyboardButton(text=x))
dokonbuttin.insert(KeyboardButton(text="Bosh menu"))



