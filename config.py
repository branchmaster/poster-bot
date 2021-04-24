from os import getenv

from peewee import SqliteDatabase
from dotenv import load_dotenv


load_dotenv()
TG_TOKEN = getenv('TOKEN')

DB = SqliteDatabase('users.db')
