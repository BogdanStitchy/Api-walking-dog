import os
from typing import Literal

from dotenv import load_dotenv

load_dotenv("config/.env")

MODE: Literal["DEV", "TEST", "PROD"] = os.environ['MODE']
LOG_LEVEL = os.environ['LOG_LEVEL']

DRIVER_DB = "asyncpg"
DIALECT_DB = "postgresql"

LOGIN_DB = os.environ['LOGIN_DB']
PASSWORD_DB = os.environ['PASSWORD_DB']
NAME_DB = os.environ['NAME_DB']
HOST_DB = os.environ['HOST_DB']
PORT_DB = os.environ['PORT_DB']


TEST_LOGIN_DB = os.environ['TEST_LOGIN_DB']
TEST_PASSWORD_DB = os.environ['TEST_PASSWORD_DB']
TEST_NAME_DB = os.environ['TEST_NAME_DB']
TEST_HOST_DB = os.environ['TEST_HOST_DB']
TEST_PORT_DB = os.environ['TEST_PORT_DB']

HOST_REDIS = os.environ['HOST_REDIS']

DATABASE_URL = f"{DIALECT_DB}+{DRIVER_DB}://{LOGIN_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}"
TEST_DATABASE_URL = f"{DIALECT_DB}+{DRIVER_DB}://{TEST_LOGIN_DB}:{TEST_PASSWORD_DB}@{TEST_HOST_DB}:{TEST_PORT_DB}/{TEST_NAME_DB}"


