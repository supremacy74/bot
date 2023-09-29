import asyncio

from aiogram import Bot, Dispatcher

from app.handlers import router

async def main():
    bot = Bot(token='6430860074:AAFr_V6W9Y46-lfblMygYEqY4MLrxlqI37I')

    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())

        print('Bot is running')
    except KeyboardInterrupt:
        print('Something went wrong')

