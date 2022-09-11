
import cbpro
import time
import pandas as pd
import plotly.graph_objects as go

data= open('passphrase.txt', 'r').read().splitlines()

secret = data[0]
public = data[1]
passphrase = data[2]


auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)



historical = pd.DataFrame(auth_client.get_product_historic_rates(product_id='JASMY-USD'))
historical.columns= ["Date","Open","High","Low","Close","Volume"]
historical['Date'] = pd.to_datetime(historical['Date'], unit='s')
historical.set_index('Date', inplace=True)
historical.sort_values(by='Date', ascending=True, inplace=True)
#print(historical)

historical['25 SMA'] = historical.Close.rolling(25).mean()
historical.tail()

print(historical)

fig = go.Figure(data=[go.Candlestick(x = historical.index,
                                    open = historical['Open'],
                                    high = historical['High'],
                                    low = historical['Low'],
                                    close = historical['Close'],
                                    ),
                     go.Scatter(x=historical.index, y=historical['25 SMA'], line=dict(color='purple', width=1))])


fig.show()

historical['50 SMA'] = historical.Close.rolling(50).mean()
historical.tail()

print(historical)

fig1 = go.Figure(data=[go.Candlestick(x = historical.index,
                                    open = historical['Open'],
                                    high = historical['High'],
                                    low = historical['Low'],
                                    close = historical['Close'],
                                    ),
                     go.Scatter(x=historical.index, y=historical['50 SMA'], line=dict(color='purple', width=1))])


fig1.show()