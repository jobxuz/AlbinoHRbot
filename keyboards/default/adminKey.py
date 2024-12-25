from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


admincommands = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="admin panel"),
            KeyboardButton(text="hr")
        ],
        
    ],
    resize_keyboard=True
)

adminusers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="users"),
        ],
        [
            KeyboardButton(text="reklama"),
        ],
        [
            KeyboardButton(text="bo'lim qo'shish"),
            KeyboardButton(text="delete bo'lim"),
            KeyboardButton(text="mavjud bo'limlar")
        ],
        [
            KeyboardButton(text="ofis qo'shish"),
            KeyboardButton(text="delete ofis"),
            KeyboardButton(text="mavjud ofislar")
        ],
        [
            KeyboardButton(text="ombor qo'shish"),
            KeyboardButton(text="delete ombor"),
            KeyboardButton(text="mavjud omborlar")
        ],
        [
            KeyboardButton(text="do'kon qo'shish"),
            KeyboardButton(text="delete do'kon"),
            KeyboardButton(text="mavjud do'konlar")
        ],
        [
            KeyboardButton(text="admin qo'shish"),
            KeyboardButton(text="delete admin"),
            KeyboardButton(text="mavjud adminlar")
        ],
        [
            KeyboardButton(text="back")
        ],
    ],
    resize_keyboard=True
)

