from datetime import datetime

class Balance():

    def __init__(self, account:str, ppi) -> None:
        self.account= account
        self.ppi = ppi

    def get_balance(self,):
        # Getting available balance
        print("\nGetting available balance of %s" % self.account)
        balances = self.ppi.account.get_available_balance(self.account)
        for balance in balances:
            print("Currency %s - Settlement %s - Amount %s %s" % (
                balance['name'], balance['settlement'], balance['symbol'], balance['amount']))
        balance_str = '\n'.join([f"Currency {b['name']} - Settlement {b['settlement']} - Amount {b['symbol']} {b['amount']}" for b in balances])
        return balance_str

    def get_balance_and_positions(self,):
        # Getting balance and positions
        print("\nGetting balance and positions of %s" % self.account)
        balances_positions = self.ppi.account.get_balance_and_positions(self.account)
        for balance in balances_positions["groupedAvailability"]:
            for currency in balance['availability']:
                print("Currency %s Settlement %s Amount %s %s" % (
                    currency['name'], currency['settlement'], currency['symbol'], currency['amount']))
        for instruments in balances_positions["groupedInstruments"]:
            print("Instrument %s " % instruments['name'])
            for instrument in instruments['instruments']:
                print("Ticker %s Price %s Amount %s" % (
                    instrument['ticker'], instrument['price'], instrument['amount']))
                           
    def get_current_price(self, ticker:str, inst:str):
        print("\nSearching MarketData: %s" % ticker)
        start_date = datetime.now()  # Replace this line with the correct datetime object creation
        end_date = datetime.now()  # Replace this line with the correct datetime object creation
        market_data = self.ppi.marketdata.current(ticker, inst , "A-48HS")
        return market_data['price'] 

    def get_market_data(self, ticker:str, type:str, start_date:str):
        print("\nSearching MarketData")
        end_date = datetime.now()  # Replace this line with the correct datetime object creation
        market_data = self.ppi.marketdata.search(ticker, type, "A-48HS", start_date, end_date)
        price_list = []
        for ins in market_data:
            price_list.append(ins['price'])
        return price_list
            