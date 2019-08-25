import alpaca_trade_api as tradeapi
from twython import Twython
import time

base_url = 'https://paper-api.alpaca.markets'
api_key_id = 'REPLACE'
api_secret = 'REPLACE'

api = tradeapi.REST(
    base_url=base_url,
    key_id=api_key_id,
    secret_key=api_secret,
    api_version="v2"
)

account = api.get_account()


if account.trading_blocked:
    print('Account is currently restricted from trading.')


print('${} is available as buying power.'.format(account.buying_power))


order = api.submit_order(
    symbol='AAPL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)

time.sleep(2)
my_order = api.get_order(order.id)




twitter = Twython(
    "REPLACE",
    "REPLACE",
    "REPLACE",
    "REPLACE"
)

orderPrice = my_order.filled_avg_price
orderQty = my_order.filled_qty
orderSym = my_order.symbol
string = ""

if my_order.filled_qty > 0:
    string = "Purchased " + str(orderQty) + " shares of " + str(orderSym) + " at $" + str(orderPrice) + "."
else:
    string = "No shares purchased."


twitter.update_status(status=string)
print("Tweeted: %s" % string)


