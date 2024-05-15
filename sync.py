import pymssql
import requests
import json

server = 'AMON'
user = 'devuser'
password = 'Agv.tr/2022'

conn = pymssql.connect(server, user, password, "COMER")
cursor = conn.cursor()

cursor.execute("SELECT * FROM [COMER].[dbo].[IW_PRODUCTOS_WEB]");

row = cursor.fetchone()
products = []

while row:
    products.append(row)
    row = cursor.fetchone()

products = json.dumps(products)
conn.close()


r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process', json=products)
print(f"Status Code: {r.status_code}, Response: {r.json()}")