from lsm import LSM
API_TOKEN = ""  # токен из botfather
DB_FILE = "db.ldb"  # название файла базы данных
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
EXIT_TIME_FORMAT = "{:02} часов {:02} минут {:02} секунд"
TIME = 12  # 12 часов
db = LSM(DB_FILE)
if bytes("count", "ascii") not in db.keys():
    db["count"] = 0
strings = {
    "start": f"Привет! Я буду отправлять твоё сообщение всем своим пользователям. Вы можете отправить только одно "
             f"анонимное сообщение раз в {TIME} часов",
    "send": "Хорошо, ваше сообщение будет отправлено {} пользователям!",
    "source": "Исходный код опубликован <a href='https://gitlab.com/tshipenchko/echoallbot'>тут</a>",
    "stat": "Всего пользователей в боте: {}",
    "wtf": "Неизвестная команда!",
    "already": "Вы уже отправляли сообщение, вернитесь пожалуста через {}"
}
