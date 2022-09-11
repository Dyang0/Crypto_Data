
import cbpro
import time
import pandas as pd
import plotly.graph_objects as gbre
import math





public_client = cbpro.PublicClient()

result = public_client.get_currencies()

#.get_currencies() - returns an array of currencies
#.get_products() - get tokens (can sepcify which value to get row['id'])
#.get_time returns time
#.get_product_order_book('BTC-USD') gets bids of specific token
#.get_product_ticker('BTC-USD')
#.get_24hr_stats
#.get_product_trades('ETH-USD')

eth_trades = public_client.get_product_trades('ETH-USD')



data= open('passphrase.txt', 'r').read().splitlines()

secret = data[0]
public = data[1]
passphrase = data[2]


auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)
#use buy and sell

#print(auth_client.get_accounts())
#print(auth_client.buy(price="10.0", size="2.1", order_type="limit", product_id="ETH-USD"))
#print(auth_client.buy(price="10.0",order_type="market", product_id="ETH-USD"))

#print(auth_client.place_limit_order(product_id="ETH-USD", side="buy", prices="10.0", size=2))
#auth_client.place_market_order
#print(auth_client.cancel_all(product_id="ETH-USD"))
#print(auth_client.get_orders)

products = auth_client.get_products()

#print(auth_client.get_product_historic_rates(product_id="ETH-USD"))
#print("\n")
#print(auth_client.get_product_24hr_stats(product_id="ETH-USD"))
#for row in products:
    #print(row['id'])

#print("\n")

ethInfo = auth_client.get_product_ticker("ETH-USD")
print(ethInfo['price'])

didBuy = True#change to False if you didnt buy



while True:

    
    print("\n")
    historical = pd.DataFrame(auth_client.get_product_historic_rates(product_id='Jasmy-USD'))
    historical.columns= ["Date","Open","High","Low","Close","Volume"]
    historical['Date'] = pd.to_datetime(historical['Date'], unit='s')
    historical.set_index('Date', inplace=True)
    historical.sort_values(by='Date', ascending=True, inplace=True)
    #print(historical)

    historical['50 SMA'] = historical.Close.rolling(50).mean()
    historical.tail()

    fiftyAverage = historical['50 SMA'][-1] 
    priceCurrent = historical["Open"][-1]
    difference = priceCurrent-fiftyAverage
    price1 = auth_client.get_product_ticker("Jasmy-USD")['price']
    difference = float(price1)-fiftyAverage
    
    
    print("Current Average:")
    print(fiftyAverage)
    print("Current Price:")
    print(priceCurrent)
    print("Ticker Price:")
    print(price1)
    print("Difference:")
    print(difference)
    print("-Just Buying-")

    coin = 'f8fbcf1e-8426-47ee-9a07-2c53267f10b1'

    if(didBuy == True):
        print("BOUGHT!")

    currentBalance = auth_client.get_account('f4ca19c6-4b12-4d2b-a103-952800c47e04')['balance']
    print(currentBalance)
    
    #get_account('f4ca19c6-4b12-4d2b-a103-952800c47e04')['balance']

    #float(price1) <= 0.018 and 
    if((difference >= 9.54*math.pow(10,-5)) and didBuy == False): 
        #auth_client.buy(size="600",order_type="market", product_id='JASMY-USD')
        print("BOUGHT!")
        didBuy = True
        break
        

    if((difference <= -(9.54*math.pow(10,-5))) and didBuy == True):
        jasmyAmount = auth_client.get_account('5d16cf11-46b5-4576-bee4-124933debdf2')['balance']
        #auth_client.sell(price=price1,size=jasmyAmount, order_type='limit', product_id='JASMY-USD')
        didBuy = False
        print("\nSuccessful Trade!!!")
        break
    
    time.sleep(2)

    




#while True:
   # print(next(eth_trades))
    #time.sleep(4)

#for row in result:
    #print(row['id'])