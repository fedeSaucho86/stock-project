from src.services.balance import Balance
from src.services.notification import Notification
from src.services.ppi_connection import LogIn
import asyncio


class Logic():

    def __init__(self,) -> None:
        login= LogIn()
        self.ppi = login.get_client()
        self.account = login.getting_account_number()
        print(self.account)

    async def send(self, txt: str):
        notify = Notification()
        await notify.send_message(txt) 

    def get_logic(self,):
        balance = Balance(self.account, self.ppi)
        asyncio.run(self.send(balance.get_balance()))
        balance.get_balance_and_positions()
        balance.get_historical_market_data()