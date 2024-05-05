from src.services.ppi_connection import LogIn
from src.services.notification import Notification
from src.services.logic import Logic
import asyncio

if __name__ == "__main__":
    logic = Logic()
    logic.run_stop_loss()

 
