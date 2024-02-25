from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



studentkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q"),
        ],
        [
            KeyboardButton(text="Bosh menu")
        ],
                
    ],
    resize_keyboard=True
)

sogliqkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sog'lig'imda muommo yo'q"),
            KeyboardButton(text="Sog'lig'imda muommo bor"),
        ],
        [
            KeyboardButton(text="Bosh menu")
        ],
                
    ],
    resize_keyboard=True
)


phonkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon nomer",request_contact=True),
        ],
        [
            KeyboardButton(text="Bosh menu")
        ],
          
    ],
    resize_keyboard=True
)


yuborishkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yuborish"),
            KeyboardButton(text="Rad etish")
        ],
        [
            KeyboardButton(text="Bosh menu")
        ],
          
    ],
    resize_keyboard=True
)