from telegram import Bot
from src.config.settings import CONFIG
import asyncio

class Notification():

    def __init__(self,):
        """Initialize the Notification class."""
        self.bot = Bot(token=CONFIG['token'])
        self.chat_id = CONFIG['chat_id']


# Define una corutina para enviar el mensaje
    async def send_message(self, text: str):
        """
        Sends a message to the specified chat using the Telegram bot.

        Args:
            text (str): The text of the message to be sent.

        Returns:
            None
        """
        await self.bot.send_message(chat_id=self.chat_id, text=text)
