import sqlite3

from aiogram import Router, F

from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

import app.keyboards as keyboards

router = Router()

conn = sqlite3.connect('database/database.db')

cursor = conn.cursor()

cursor.execute(""" SELECT * FROM categories """)

category_data = cursor.fetchall()

cursor.execute(""" SELECT * FROM products """)

product_data = cursor.fetchall()

conn.close()

product_list = []

for product in product_data:
    id, name, price, src, description, category_id = product
    product_dict = {
        'id': id,
        'name': name,
        'price': price,
        'src': src,
        'description': description,
        'category_id': category_id
    }
    product_list.append(product_dict)

def create_products_handler(category_id, category_name):
    @router.message(F.text == category_name)
    async def products(message: Message):
        for product in product_list:
            if category_id == product['category_id']:
                markup = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Купить', callback_data='some')],
                    [InlineKeyboardButton(text='В корзину', callback_data='some')]
                ])

                await message.answer_photo(photo=product["src"])
                await message.answer(f'{product["name"]}, {product["price"]} BYN', reply_markup=markup)

def create_product_handler(product_name):
    @router.message(F.text == product_name)
    async def product(message: Message):
        for product in product_list:
            if product_name == product['name']:
                # await message.answer_photo(photo=product["src"])
                await message.answer(f'{product["name"]}, {product["price"]} BYN\n\n{product["description"]}')
                

@router.message(lambda message: message.text == '/start' or message.text == 'Назад')
async def cmd_start(message: Message):
    await message.answer(f'Добро пожаловать, {message.from_user.username}! Здесь вы можете посмотреть на ассортимент товаров, оформить заказ или связаться с нами.', reply_markup=keyboards.main)

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию', reply_markup=keyboards.catalog)

@router.message(F.text == 'Профиль')
async def profile(message: Message):
    username = message.from_user.username
    
    conn = sqlite3.connect('database/database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

    existing_user = cursor.fetchone()

    print(existing_user)

    if existing_user:
        await message.answer(f"Ваш профиль:\nНомер телефона: {existing_user[2]}\nАдрес: {existing_user[3]}\nИмя: {existing_user[4]}")
    else:
        await message.answer("Профиль не найден.\n\nВведите данные в одном сообщении.\n\nВведите ваш номер телефона в международном формате, адрес и имя как в следующем примере:\n\n8005553535\nМосква, Ленина,\nИмя: ваше имя", reply_markup=keyboards.main)

    conn.close()


@router.message(lambda message: message.text and '\n' in message.text)
async def get_contact_info(message: Message):
    user_data = message.text.split('\n')
    if len(user_data) == 3:
        phone, address, name = user_data
        try:
            phone = int(phone)

            conn = sqlite3.connect('database/database.db')

            cursor = conn.cursor()

            cursor.execute('INSERT INTO users (username, phone, address, name) VALUES (?, ?, ?, ?)', (message.from_user.username, phone, address, name))
            conn.commit()

            await message.answer('Данные успешно добавлены в базу данных!')
        except ValueError:
            await message.answer('Ошибка: Номер телефона должен быть числом.')
        except Exception as e:
            await message.answer(f'Произошла ошибка: {str(e)}')
        finally:
            conn.close()
    else:
        await message.answer('Я попытался сохранить ваши контактные данные, но мне не удалось. Пожалуйста, введите данные в правильном формате: номер телефона, адрес, имя. Каждое на новой строке.')

for id, name in category_data:
    products_handler = create_products_handler(id, name)

for id, name, price, src, description, category_id in product_data:
    product_handler = create_product_handler(name)
            
