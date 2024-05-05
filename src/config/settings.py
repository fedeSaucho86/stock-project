from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

CONFIG = {
    'public': os.getenv('public'),
    'private': os.getenv('private'),
    'token': os.getenv('token'),
    'chat_id': os.getenv('chat_id')
}


