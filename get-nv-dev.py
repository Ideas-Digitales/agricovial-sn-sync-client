import pymssql
import requests
import json
import sys
from Logger import Logger
from OrderModel import OrderModel

server = 'AMON'
user = 'devuser'
password = 'Agv.tr/2022'
database = 'COMER2017'
endpoint = 'https://www.agricovial.cl/wp-json/sync/v1/get-orders'
# endpoint = 'http://localhost:3001/wp-json/sync/v1/get-orders'

logger = Logger()
orderModel = OrderModel(server, user, password, database)

conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()

clients = []
orders = []

try:
    
    orders_response = requests.get(endpoint)
    print('request sent')
    orders_response = orders_response.json()
    print('request parsed')
    orders = orders_response['orders']
    # clients = orders_response['clients']
    
except Exception as e:
     
    logger.error("ON REQUEST: " + str(e))
    sys.exit()

# Sincronización de clientes
# if clients: 
#     for c in clients:
#         try:
#             cursor.execute(c['create_client'])
#         except Exception as e:
#             logger.error(str(e) + "\nSQL Query: " + c['create_client'] + "\n")
            
#         try:
#             cursor.execute(c['create_cond'])
#         except Exception as e:
#             logger.error(str(e) + "\nSQL Query: " + c['create_cond'] + "\n")
            
#         try:
#             cursor.execute(c['create_address'])
#         except Exception as e:
#             logger.error(str(e) + "\nSQL Query: " + c['create_address'] + "\n")
            
#         try:
#             cursor.execute(c['create_vendor'])
#         except Exception as e:
#             logger.error(str(e) + "\nSQL Query: " + c['create_vendor'] + "\n")
            
#         try:
#             conn.commit()
#         except Exception as e:
#             logger.error(str(e))
        

if orders:
    
    logger.message("Inicia la importación de órdenes")
    
    for o in orders:
        
        exists = orderModel.checkIfNumOCExists(o['NumOC'])
        
        if (exists):
            continue
            
        logger.message("Inicia proceso de importación de la orden " + str(o['NumOC']))
        
        # Registro de cliente asociado a la orden de compra
        checkClientQueries = ['CheckClient', 'CheckClient2', 'CheckClient3', 'CheckClient4']
        
        try:
            logger.message('Ingresando cliente ' + o['CodAux'])
            
            for key in checkClientQueries:
                cursor.execute(o[key])
            
            logger.message('Cliente registrado ' + o['CodAux'])
                
        except Exception as e:

            logger.error("No se pudo ingresar la orden " + o['NumOC'])
            logger.error(str(e))
            logger.error("SQL Queries")
            
            for key in checkClientQueries:
                logger.error(str(o[key]))
                
            try:
                conn.close()
            except Exception as ex:
                logger.error(str(ex))
            finally:
                conn = pymssql.connect(server, user, password, database)
                cursor = conn.cursor()
            
            continue
            
        sql = ""

        try:
            
            cursor.execute("SELECT MAX(nvnumero) FROM softland.nw_nventa");
            NVNumero = cursor.fetchone()[0]+1
            sql = 'INSERT softland.nw_nventa (NVNumero, nvFem, nvEstado, nvEstFact, nvEstDesp, nvEstRese,\
                        nvEstConc, CotNum, nvFeEnt, CodAux, VenCod, CodMon, CodLista, nvObser, nvCanalNV,\
                        CveCod, NomCon, CodiCC, CodBode, nvSubTotal, nvPorcDesc01, nvDescto01, nvPorcDesc02,\
                        nvDescto02, nvPorcDesc03, nvDescto03, nvPorcDesc04, nvDescto04, nvPorcDesc05,\
                        nvDescto05, nvMonto, nvFeAprob, NumGuiaRes, nvPorcFlete, nvValflete, nvPorcEmb,\
                        nvValEmb, nvEquiv, nvNetoExento, nvNetoAfecto, nvTotalDesc, ConcAuto, CodLugarDesp,\
                        SolicitadoPor, DespachadoPor, Patente, RetiradoPor, NumOC, CheckeoPorAlarmaVtas,\
                        EnMantencion, Usuario, UsuarioGeneraDocto, FechaHoraCreacion, ConcManual, Sistema, CodBodeWms,Proceso)\
                VALUES('+str(NVNumero)+', '+o['nvFem']+', '+o['nvEstado']+', '+o['nvEstFact']+', '+o['nvEstDesp']+', '+o['nvEstRese']+',\
                        '+o['nvEstConc']+', '+o['CotNum']+', '+o['nvFeEnt']+', '+o['CodAux']+', '+o['VenCod']+', '+o['CodMon']+', '+o['CodLista']+', '+o['nvObser']+', '+o['nvCanalNV']+',\
                        '+o['CveCod']+', '+o['NomCon']+', '+o['CodiCC']+', '+o['CodBode']+', '+o['nvSubTotal']+', '+o['nvPorcDesc01']+', '+o['nvDescto01']+', '+o['nvPorcDesc02']+',\
                        '+o['nvDescto02']+', '+o['nvPorcDesc03']+', '+o['nvDescto03']+', '+o['nvPorcDesc04']+', '+o['nvDescto04']+', '+o['nvPorcDesc05']+',\
                        '+o['nvDescto05']+', '+o['nvMonto']+', '+o['nvFeAprob']+', '+o['NumGuiaRes']+', '+o['nvPorcFlete']+', '+o['nvValflete']+', '+o['nvPorcEmb']+',\
                        '+o['nvValEmb']+', '+o['nvEquiv']+', '+o['nvNetoExento']+', '+o['nvNetoAfecto']+', '+o['nvTotalDesc']+', '+o['ConcAuto']+', '+o['CodLugarDesp']+',\
                        '+o['SolicitadoPor']+', '+o['DespachadoPor']+', '+o['Patente']+', '+o['RetiradoPor']+', '+o['NumOC']+', '+o['CheckeoPorAlarmaVtas']+',\
                        '+o['EnMantencion']+', '+o['Usuario']+', '+o['UsuarioGeneraDocto']+', '+o['FechaHoraCreacion']+', '+o['ConcManual']+', '+o['Sistema']+', '+o['CodBodeWms']+','+"'Notas de Venta'"+')'                       
            cursor.execute(sql)
            
            sql = 'INSERT softland.nw_impto (nvNumero, codimpto, valpctIni, afectoImpto, Impto) VALUES('+str(NVNumero)+', '+o['codimpto']+', '+o['valpctIni']+', '+o['afectoImpto']+', '+o['Impto']+')'
            cursor.execute(sql)
            
            for i in o['Items']:
                
                cursor.execute("SELECT max(nvLinea) FROM softland.nw_detnv WHERE nvNumero = "+str(NVNumero)+" and nvLinea < 1000");
                nvLinea = cursor.fetchone();

                if( nvLinea[0] is None ):
                    nvLinea = 1
                else:
                    nvLinea = nvLinea[0]+1

                i['NVNumero'] = NVNumero 
                i['nvLinea'] = nvLinea
                sql = 'INSERT softland.nw_detnv (NVNumero, nvLinea, nvCorrela, nvFecCompr, CodProd, nvCant,\
                        nvPrecio, nvEquiv, nvSubTotal, nvDPorcDesc01, nvDDescto01, nvDPorcDesc02, nvDDescto02,\
                        nvDPorcDesc03, nvDDescto03, nvDPorcDesc04, nvDDescto04, nvDPorcDesc05, nvDDescto05,\
                        nvTotDesc, nvTotLinea, nvCantDesp, nvCantProd, nvCantFact, nvCantDevuelto, nvCantNC,\
                        nvCantBoleta, nvCantOC, DetProd, CheckeoMovporAlarmaVtas, KIT, Partida, Pieza, FechaVencto, CodUMed, CantUVta)\
                        VALUES('+str(i['NVNumero'])+', '+str(i['nvLinea'])+', '+i['nvCorrela']+', '+i['nvFecCompr']+', '+i['CodProd']+', '+i['nvCant']+', '+i['nvPrecio']+',\
                        '+i['nvEquiv']+', '+i['nvSubTotal']+', '+i['nvDPorcDesc01']+', '+i['nvDDescto01']+', '+i['nvDPorcDesc02']+', '+i['nvDDescto02']+',\
                        '+i['nvDPorcDesc03']+', '+i['nvDDescto03']+', '+i['nvDPorcDesc04']+', '+i['nvDDescto04']+', '+i['nvDPorcDesc05']+',\
                        '+i['nvDDescto05']+', '+i['nvTotDesc']+', '+i['nvTotLinea']+', '+i['nvCantDesp']+', '+i['nvCantProd']+', '+i['nvCantFact']+',\
                        '+i['nvCantDevuelto']+', '+i['nvCantNC']+', '+i['nvCantBoleta']+', '+i['nvCantOC']+', '+i['DetProd']+',\
                        '+i['CheckeoMovporAlarmaVtas']+', '+i['KIT']+', '+i['Partida']+', '+i['Pieza']+', '+i['FechaVencto']+', '+i['CodUMed']+', '+i['nvCant']+')'
                cursor.execute(sql)
                
            conn.commit()
            logger.message("Orden " + str(o['NumOC']) + " ingresada. Nota de venta: " + str(NVNumero))
                
        except Exception as e:
            
            logger.error("Falló al insertar la orden número " + str(o['NumOC']))
            logger.error(str(e))
            logger.error("SQL Query: " + sql)
            
            try:
                conn.close()
            except Exception as ex:
                logger.error(str(ex))
            finally:
                conn = pymssql.connect(server, user, password, database)
                cursor = conn.cursor()

logger.message("Termina la importación de órdenes")
orderModel.connection.close()
conn.close()