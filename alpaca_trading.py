#!/usr/bin/env python3
from live_api_keys import end_point, key, secret_key

# , paper
# from api_keys import key, secret_key, paper
print(key)
print(secret_key)

# import alpaca

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

print("before")
trading_client = TradingClient(
    api_key=key,
    secret_key=secret_key,
    url_override=end_point,
)
print("trading_client", trading_client)

# Get our account information.
account = trading_client.get_account()
account_config = trading_client.get_account_configurations()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print("Account is currently restricted from trading.")

# Check how much money we can use to open new positions.
# print('${} is available as buying power.'.format(account.buying_power))
print("${} is available as buying power.".format(account))

# Options level
print("options_approved_level: ", account.options_approved_level)
print("options_trading_level: ", account.options_trading_level)
print("options_buying_power: ", account.options_buying_power)
# account_config.max_options_trading_level = 2
# trading_client.set_account_configurations(account_config)

# Options level
print("after")
print("options_approved_level: ", account.options_approved_level)
print("options_trading_level: ", account.options_trading_level)
print("options_buying_power: ", account.options_buying_power)
#### We use paper environment for this example ####
paper = True  # Please do not modify this. This example is for paper trading only.
####

# Below are the variables for development this documents
# Please do not change these variables
trade_api_url = None
trade_api_wss = None
data_api_url = None
stream_data_wss = None

import json
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import alpaca

# from alpaca.data.live.crypto import *
from alpaca.data.historical.crypto import *
from alpaca.data.requests import *
from alpaca.data.timeframe import *
from alpaca.trading.client import *
from alpaca.trading.stream import *
from alpaca.trading.requests import *
from alpaca.trading.enums import *
import requests
from alpaca.common.exceptions import APIError

url = "https://data.alpaca.markets/v1beta1/options/bars?limit=1000&sort=asc"
# url = "https://paper-api.alpaca.markets/v2/options/bars?limit=1000&sort=asc"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
print("Last Line is executed")
