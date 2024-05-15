import requests

response = requests.get('https://www.agricovial.test/wp-json/sync/v1/get-orders', verify=False).json()
orders = response['orders']
for order in orders:
    print(order['CheckClient'])
    break