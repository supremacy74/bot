from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

reply = {
    'main': [
        [
            KeyboardButton(text='Каталог'),
            KeyboardButton(text='Корзина'),
            KeyboardButton(text='Профиль')
        ],
        [
            KeyboardButton(text='Помощь'),
            KeyboardButton(text='Контакты')
        ]
    ],
    'catalog': [
        [
            KeyboardButton(text='Назад'),
            KeyboardButton(text='Овощи'),
            KeyboardButton(text='Ягоды'),
            KeyboardButton(text='Фрукты'),
        ],
        [
            KeyboardButton(text='Добрый'),
            KeyboardButton(text='Посад. материал')
        ]
    ]
}

main = ReplyKeyboardMarkup(keyboard=reply['main'], resize_keyboard=True)
catalog = ReplyKeyboardMarkup(keyboard=reply['catalog'], resize_keyboard=True)
