import config
import logging
import utils

from aiogram import Bot, Dispatcher, executor, types

db = config.db
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
@utils.register
async def send_welcome(message: types.Message):
    await message.reply(config.strings["start"])


@dp.message_handler(commands=['source'])
@utils.register
async def send_source(message: types.Message):
    await message.reply(config.strings["source"])


@dp.message_handler(commands=['stats'])
@utils.register
async def send_source(message: types.Message):
    await message.reply(config.strings["stat"].format(int(db["count"])))


@dp.message_handler(commands=[''])
@utils.register
async def wtf(message: types.Message):
    await message.reply(config.strings["wtf"])


@dp.message_handler()
@utils.register
async def echo_all(message: types.Message):
    allow, text = await utils.is_allowed(message)
    if allow:
        doing = utils.echo_all(message)
        await message.reply(config.strings["send"].format(int(db["count"])))
        await doing
    else:
        await message.reply(text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
