from dotenv import load_dotenv
import os
import datetime

load_dotenv()  # take environment variables from .env.
CONFIG = {
    'public': os.getenv('public'),
    'private': os.getenv('private'),
    'token': os.getenv('token'),
    'chat_id': os.getenv('chat_id'),
    'instruments': [ ['GGAL',3279, 'Acciones', datetime.datetime(2024, 4, 23)],
                ['AL30',59000, 'BONOS', datetime.datetime(2024, 4, 23)],
                ['SAMI',790, 'Acciones', datetime.datetime(2024, 4, 23)],
                ['BHIP',414.50, 'Acciones',datetime.datetime(2024, 4, 23)],
             ]
}


