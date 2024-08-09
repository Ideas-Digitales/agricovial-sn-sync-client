import pymssql

class OrderModel:
    
    connection = None
    cursor = None
    
    def __init__(self, server, user, password, database):
        
        self.connection = pymssql.connect(server, user, password, database)
        self.cursor = self.connection.cursor()
        
    def checkIfNumOCExists(self, NumOC, NvFem):
        
        sql = "SELECT * FROM softland.nw_nventa venta WHERE venta.NumOC = '" + str(NumOC) + "' AND venta.VenCod = 'ECom'" + "AND YEAR(" + NvFem + ") = YEAR(venta.NvFem)"
        print(sql)
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        
        if(row):
            return True
        else:
            return False