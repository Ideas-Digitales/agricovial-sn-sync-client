import pymssql
from Logger import Logger

server = 'AMON'
user = 'devuser'
password = 'Agv.tr/2022'

conn = pymssql.connect(server, user, password, "COMER")
cursor = conn.cursor()

logger = Logger()

def checkIfNumOCExists(NumOC):
    conn = pymssql.connect(server, user, password, "COMER")
    cursor = conn.cursor()
    sql = "SELECT * FROM softland.nw_nventa venta WHERE venta.NumOC = '" + str(NumOC) + "'"
    cursor.execute(sql)
    row = cursor.fetchone()
    conn.close()
    
    if(row):
        return True
    else:
        return False
        
NumOC = 15886546546546321657987654
if(checkIfNumOCExists(NumOC)):
    print(str(NumOC) + " exists")
    logger.error(str(NumOC) + " exists")
else:
    print(str(NumOC) + " doesn't exist")
    logger.error(str(NumOC) + " doesn't exist")