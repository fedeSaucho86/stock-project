from src.services.ppi_connection import LogIn
from src.services.notification import Notification
from src.services.logic import Logic
import asyncio


#async def send():
#    notify = Notification()
#    await notify.send_message("Hello, World!") 

if __name__ == "__main__":
    logic = Logic()
    logic.get_logic()

 
