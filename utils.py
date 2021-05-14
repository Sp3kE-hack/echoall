from aiogram import types
from config import db
from datetime import datetime, timedelta
import config


async def echo_all(message: types.Message):
    for x in db.keys():
        if x.decode("utf-8").startswith("u"):
            x = x[1:]
            try:
                await message.copy_to(int(x))
            except:  # i will fix that later
                del db[x]


def register(func):
    async def wrapper(message: types.Message):
        uid = "u" + str(message.from_user.id)
        if bytes(uid, "ascii") not in db.keys():
            db[uid] = "new"
            db["count"] = int(db["count"]) + 1
        await func(message)

    return wrapper


async def is_allowed(message: types.Message):
    uid = "u" + str(message.from_user.id)
    if db[uid].decode("utf-8") == "new":
        db[uid] = datetime.now().strftime(config.TIME_FORMAT)
        return True, None
    elif (datetime.now() - datetime.strptime(db[uid].decode("utf-8"), config.TIME_FORMAT)) > timedelta(hours=config.TIME):
        db[uid] = datetime.now().strftime(config.TIME_FORMAT)
        return True, None
    else:
        a = (datetime.strptime(db[uid].decode("utf-8"), config.TIME_FORMAT) - datetime.now()).seconds
        hours, remainder = divmod(a, 3600)
        minutes, seconds = divmod(remainder, 60)
        return False, config.strings["already"].format(
            config.EXIT_TIME_FORMAT.format(int(hours), int(minutes), int(seconds))
        )
