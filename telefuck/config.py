from environs import Env
from typing import Optional

env = Env()

PRODUCTION: bool = env.bool("PRODUCTION", False)
HEROKU_APP_NAME: Optional[str] = env.str("HEROKU_APP_NAME", None)
TELEGRAM_TOKEN: str = env.str("TELEGRAM_TOKEN")
PORT: int = env.int("PORT", 80)
