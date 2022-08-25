from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

DATABASE = env.str('DATABASE')
DB_USER = env.str('DB_USER')
DB_PASSWORD = env.str('DB_PASSWORD')
DB_NAME = env.str('DB_NAME')
DB_PLUGIN = env.str('DB_PLUGIN')
DB_HOST = env.str('DB_HOST')
DB_PORT = env.str('DB_PORT')

DB_LINK = f'{DATABASE}+{DB_PLUGIN}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'