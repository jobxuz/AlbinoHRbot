from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 uz',callback_data='uz'),
            InlineKeyboardButton(text='🇺🇸 eng',callback_data='en'),
            InlineKeyboardButton(text='🇷🇺 ru',callback_data='ru')
        ],
    ]
)


rek = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='✅ Ha',callback_data='ha'),
        InlineKeyboardButton(text="❌ Yo'q",callback_data="yuq")
    ],
    ]
)




books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Mukammal Dasturlash. JavaScript": "js_book",
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=value))
