from src.services.balance import Balance
from src.services.notification import Notification
from src.services.ppi_connection import LogIn
import asyncio
from src.config.settings import CONFIG
import datetime

class Logic():

    def __init__(self,) -> None:
        login= LogIn()
        self.ppi = login.get_client()
        self.account = login.getting_account_number()

    async def send(self, txt: str):
        notify = Notification()
        await notify.send_message(txt) 

    def calculate_percent_change(self, actual_price, target_price):
        print(actual_price, target_price)
        return round(((actual_price - target_price) / target_price) * 100, 2)
    
    def change_format(self,percent_list):
        result = ["Investment variation:"]
        for item in percent_list:
            value = item[1]
            if value > 0:
                formatted_value = f'*{value:.2f}%* _(+{value:.2f}%)_'
            else:
                formatted_value = f'*{value:.2f}%* _({value:.2f}%)_'
            result.append(f'{item[0]}: {formatted_value}')
        return '\n'.join(result)

    def run_stop_loss(self,):
        balance = Balance(self.account, self.ppi)
        #asyncio.run(self.send(balance.get_balance()))
        #balance.get_balance_and_positions()
        percent_list =[]
        for instrument in CONFIG['instruments']:
            actual_price = balance.get_current_price(instrument[0], instrument[2])
            percentile = self.calculate_percent_change(actual_price, instrument[1])
            percent_list.append([instrument[0],percentile])
        msg = self.change_format(percent_list)
        asyncio.run(self.send(msg))