import cbpro


data= open('passphrase.txt', 'r').read().splitlines()

secret = data[0]
public = data[1]
passphrase = data[2]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)

#print(auth_client.get_accounts)
#print(auth_client.get_account('5d16cf11-46b5-4576-bee4-124933debdf2'))
#print(auth_client.get_account('f4ca19c6-4b12-4d2b-a103-952800c47e04')['balance'])

#print(auth_client.buy(size="1400",order_type="market", product_id="Jasmy-USD"))
#auth_client.buy(size="10",order_type="market", product_id='JASMY-USD')

#print(auth_client.get_products())
print(auth_client.get_accounts)