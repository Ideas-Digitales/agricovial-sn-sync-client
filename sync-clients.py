import pymssql
import requests
import json

server = 'AMON'
user = 'devuser'
password = 'Agv.tr/2022'

conn = pymssql.connect(server, user, password, "COMER")
cursor = conn.cursor()




# OBTENER TODO
cursor.execute("EXEC OBT_DOC_IMPAGOS '2023-09-01', '2023-10-10', 'DCTO_IMPAGOS', 1");
cursor.execute("SELECT * FROM DCTO_IMPAGOS INNER JOIN softland.cwtauxi ON softland.cwtauxi.CodAux = DCTO_IMPAGOS.Client WHERE EstadoDoc = 'IMPAGO'");
row = cursor.fetchone()
doctos = []

while row:
    doctos.append(row)
    row = cursor.fetchone()

doctos = json.dumps(doctos, default=str)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=documentos', json=doctos)
print(f"Status Code: {r.status_code}, Response: {r.json()}")



# GIROS
cursor.execute("SELECT * FROM [COMER].[softland].[cwtgiro]");
row = cursor.fetchone()
giros = []

while row:
    giros.append(row)
    row = cursor.fetchone()

giros = json.dumps(giros)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=giros', json=giros)
print(f"Status Code: {r.status_code}, Response: {r.json()}")


# PROVINCIAS
cursor.execute("SELECT * FROM [COMER].[softland].[cwtprovincia]");
row = cursor.fetchone()
provincias = []

while row:
    provincias.append(row)
    row = cursor.fetchone()

provincias = json.dumps(provincias)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=provincias', json=provincias)
print(f"Status Code: {r.status_code}, Response: {r.json()}")


# REGIONES
cursor.execute("SELECT * FROM [COMER].[softland].[cwtregion]");
row = cursor.fetchone()
regiones = []

while row:
    regiones.append(row)
    row = cursor.fetchone()

regiones = json.dumps(regiones)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=regiones', json=regiones)
print(f"Status Code: {r.status_code}, Response: {r.json()}")


# CIUDAD
cursor.execute("SELECT * FROM [COMER].[softland].[cwtciud]");
row = cursor.fetchone()
ciudades = []

while row:
    ciudades.append(row)
    row = cursor.fetchone()

ciudades = json.dumps(ciudades)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=ciudades', json=ciudades)
print(f"Status Code: {r.status_code}, Response: {r.json()}")



# COMUNAS
cursor.execute("SELECT * FROM [COMER].[softland].[cwtcomu]");
row = cursor.fetchone()
comunas = []

while row:
    comunas.append(row)
    row = cursor.fetchone()

comunas = json.dumps(comunas)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=comunas', json=comunas)
print(f"Status Code: {r.status_code}, Response: {r.json()}")



# CANALESVENTAS
cursor.execute("SELECT * FROM [COMER].[softland].[cwtcvcl]");
row = cursor.fetchone()
canalesventas = []

while row:
    canalesventas.append(row)
    row = cursor.fetchone()

canalesventas = json.dumps(canalesventas, default=str)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=canalesventas', json=canalesventas)
print(f"Status Code: {r.status_code}, Response: {r.json()}")


# VENDEDORES
cursor.execute("SELECT * FROM [COMER].[softland].[cwtvend]");
row = cursor.fetchone()
vendedores = []

while row:
    vendedores.append(row)
    row = cursor.fetchone()

vendedores = json.dumps(vendedores, default=str)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=vendedores', json=vendedores)
print(f"Status Code: {r.status_code}, Response: {r.json()}")


# AUXILIARES
cursor.execute("SELECT * FROM [COMER].[softland].[cwtauxi]");
row = cursor.fetchone()
auxiliares = []

while row:
    auxiliares.append(row)
    row = cursor.fetchone()

auxiliares = json.dumps(auxiliares, default=str)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=auxiliares', json=auxiliares)
print(f"Status Code: {r.status_code}, Response: {r.json()}")


# CLIENTES
cursor.execute("SELECT * FROM softland.cwtauxi;");
row = cursor.fetchone()
clientes = []

while row:
    clientes.append(row)
    row = cursor.fetchone()

clientes = json.dumps(clientes, default=str)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=clientes', json=clientes)
print(f"Status Code: {r.status_code}, Response: {r.json()}")

# DIRECCIONES
cursor.execute("SELECT * FROM softland.cwtauxd;");
row = cursor.fetchone()
direcciones = []

while row:
    direcciones.append(row)
    row = cursor.fetchone()

direcciones = json.dumps(direcciones, default=str)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=direcciones', json=direcciones)
print(f"Status Code: {r.status_code}, Response: {r.json()}")


conn.close()

conn = pymssql.connect(server, user, password, "COMER")
cursor = conn.cursor()

# AUXILIARES
cursor.execute("SELECT * FROM TYP_ComuDespacho");
row = cursor.fetchone()
auxiliares = []

while row:
    auxiliares.append(row)
    row = cursor.fetchone()

auxiliares = json.dumps(auxiliares, default=str)
r = requests.post('https://www.agricovial.cl/wp-json/sync/v1/process-variables?type=despacho', json=auxiliares)
print(f"Status Code: {r.status_code}, Response: {r.json()}")



conn.close()








