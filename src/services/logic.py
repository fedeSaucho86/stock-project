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
        print (round(((actual_price - target_price) / target_price) * 100, 2))
        return round(((actual_price - target_price) / target_price) * 100, 2)
    
    def max_price(self,price_list):
        return max(price_list)
    
    def change_format(self,percent_list):
        result = ["Investment variation:"]
        for item in percent_list:
            value = item[2]
            if value > 0:
                formatted_value = f'*{value:.2f}%* _(+{value:.2f}%)_'
            else:
                formatted_value = f'*{value:.2f}%* _({value:.2f}%)_'
            result.append(f'{item[0]}: {formatted_value}')
        return '\n'.join(result)

    def run_stop_loss(self,):
        balance = Balance(self.account, self.ppi)
        percent_list =[]
        info_list = ["Historical information:"]
        info_list.append(["Ticker", "StartPrice", "EndPrice","%Change",  "Date"])
        for instrument in CONFIG['instruments']:
            price_list = balance.get_market_data(instrument[0], instrument[1], instrument[2])
            max_price = self.max_price(price_list)
            print(f"Max value of {instrument[0]}:  {max_price}")
            percentile = self.calculate_percent_change(price_list[-1], max_price)
            percent_list.append([instrument[0],max_price,percentile])
            info_list.append([instrument[0], price_list[0], price_list[-1], 
                              self.calculate_percent_change(price_list[-1], price_list[0]),
                              instrument[2].strftime("%Y-%m-%d")])
        msg = self.change_format(percent_list)
        asyncio.run(self.send(msg))
        msg = '\n'.join([' | '.join(map(str, item)) for item in info_list[1:]])
        asyncio.run(self.send(msg)) 