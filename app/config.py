from environs import Env

env = Env()

DATABASE_URL: str = env.str("DATABASE_URL")
HEROKU_APP_NAME: str = env.str("HEROKU_APP_NAME")
TELEGRAM_TOKEN: str = env.str("TELEGRAM_TOKEN")
PORT: int = env.int("PORT")
