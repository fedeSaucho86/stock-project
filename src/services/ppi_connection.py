# Imports 
from ppi_client.api.constants import ACCOUNTDATA_TYPE_ACCOUNT_NOTIFICATION, ACCOUNTDATA_TYPE_PUSH_NOTIFICATION, \
    ACCOUNTDATA_TYPE_ORDER_NOTIFICATION
from ppi_client.models.account_movements import AccountMovements
from ppi_client.models.bank_account_request import BankAccountRequest
from ppi_client.models.foreign_bank_account_request import ForeignBankAccountRequest, ForeignBankAccountRequestDTO
from ppi_client.models.cancel_bank_account_request import CancelBankAccountRequest
from ppi_client.models.order import Order
from ppi_client.ppi import PPI
from ppi_client.models.order_budget import OrderBudget
from ppi_client.models.order_confirm import OrderConfirm
from ppi_client.models.disclaimer import Disclaimer
from ppi_client.models.investing_profile import InvestingProfile
from ppi_client.models.investing_profile_answer import InvestingProfileAnswer
from ppi_client.models.instrument import Instrument
from datetime import datetime, timedelta
from ppi_client.models.estimate_bonds import EstimateBonds
import asyncio
import json
import traceback
import os
from src.config.settings import CONFIG

class LogIn():
    def __init__(self,) -> None:
        """
        Initialize the LogIn object by setting up the PPI client with sandbox mode disabled and logging into the account using the public and private keys from the CONFIG settings.
        """
        self.ppi = PPI(sandbox=False)
        self.ppi.account.login_api(CONFIG['public'], CONFIG['private'])
       

    def get_client(self) -> PPI:
        """Return PPI client"""
        return self.ppi
    
    def getting_account_number(self,):
        """
        Retrieves the account number of the user.

        This function retrieves the account information of the user by calling the `get_accounts` method of the `self.ppi.account` object. It then iterates through the list of account numbers and prints each account. Finally, it extracts the account number from the first account in the list and prints it.
        """
        # Getting accounts information
        print("Getting accounts information")
        account_numbers = self.ppi.account.get_accounts()
        account_number = account_numbers[0]['accountNumber']
        return account_number
