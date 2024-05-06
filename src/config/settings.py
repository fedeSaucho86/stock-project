from dotenv import load_dotenv
import os
import datetime

load_dotenv()  # take environment variables from .env.
CONFIG = {
    'public': os.getenv('public'),
    'private': os.getenv('private'),
    'token': os.getenv('token'),
    'chat_id': os.getenv('chat_id'),
    'instruments': [ ['GGAL', 'Acciones', datetime.datetime(2024, 4, 10)],
                ['AL30', 'BONOS', datetime.datetime(2024, 3, 26)],
                ['SAMI', 'Acciones', datetime.datetime(2024, 4, 12)],
                ['BHIP', 'Acciones',datetime.datetime(2024, 5, 3)],
             ]
}


