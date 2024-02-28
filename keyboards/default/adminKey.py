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
            KeyboardButton(text="bolim qoshish"),
            KeyboardButton(text="delete bolim")
        ],
        [
            KeyboardButton(text="ofis qoshish"),
            KeyboardButton(text="delete ofis")
        ],
        [
            KeyboardButton(text="ombor qoshish"),
            KeyboardButton(text="delete ombor")
        ],
        [
            KeyboardButton(text="dokon qoshish"),
            KeyboardButton(text="delete dokon")
        ],
        [
            KeyboardButton(text="back")
        ],
    ],
    resize_keyboard=True
)

