

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