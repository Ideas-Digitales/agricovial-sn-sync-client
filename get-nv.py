import pymssql
import requests
import json

server = 'AMON'
user = 'devuser'
password = 'Agv.tr/2022'

conn = pymssql.connect(server, user, password, "COMER")
cursor = conn.cursor()


orders_response = requests.get('https://www.agricovial.cl/wp-json/sync/v1/get-orders')
orders_response = orders_response.json()

orders = orders_response['orders']

for o in orders:
    cursor.execute("select max(nvnumero) from softland.nw_nventa ");
    NVNumero = cursor.fetchone()[0]+1
    o['NVNumero'] = NVNumero

    sql = 'INSERT softland.nw_nventa (NVNumero, nvFem, nvEstado, nvEstFact, nvEstDesp, nvEstRese,\
                nvEstConc, CotNum, nvFeEnt, CodAux, VenCod, CodMon, CodLista, nvObser, nvCanalNV,\
                CveCod, NomCon, CodiCC, CodBode, nvSubTotal, nvPorcDesc01, nvDescto01, nvPorcDesc02,\
                nvDescto02, nvPorcDesc03, nvDescto03, nvPorcDesc04, nvDescto04, nvPorcDesc05,\
                nvDescto05, nvMonto, nvFeAprob, NumGuiaRes, nvPorcFlete, nvValflete, nvPorcEmb,\
                nvValEmb, nvEquiv, nvNetoExento, nvNetoAfecto, nvTotalDesc, ConcAuto, CodLugarDesp,\
                SolicitadoPor, DespachadoPor, Patente, RetiradoPor, NumOC, CheckeoPorAlarmaVtas,\
                EnMantencion, Usuario, UsuarioGeneraDocto, FechaHoraCreacion, ConcManual, Sistema, CodBodeWms,Proceso)\
        VALUES('+str(o['NVNumero'])+', '+o['nvFem']+', '+o['nvEstado']+', '+o['nvEstFact']+', '+o['nvEstDesp']+', '+o['nvEstRese']+',\
                '+o['nvEstConc']+', '+o['CotNum']+', '+o['nvFeEnt']+', '+o['CodAux']+', '+o['VenCod']+', '+o['CodMon']+', '+o['CodLista']+', '+o['nvObser']+', '+o['nvCanalNV']+',\
                '+o['CveCod']+', '+o['NomCon']+', '+o['CodiCC']+', '+o['CodBode']+', '+o['nvSubTotal']+', '+o['nvPorcDesc01']+', '+o['nvDescto01']+', '+o['nvPorcDesc02']+',\
                '+o['nvDescto02']+', '+o['nvPorcDesc03']+', '+o['nvDescto03']+', '+o['nvPorcDesc04']+', '+o['nvDescto04']+', '+o['nvPorcDesc05']+',\
                '+o['nvDescto05']+', '+o['nvMonto']+', '+o['nvFeAprob']+', '+o['NumGuiaRes']+', '+o['nvPorcFlete']+', '+o['nvValflete']+', '+o['nvPorcEmb']+',\
                '+o['nvValEmb']+', '+o['nvEquiv']+', '+o['nvNetoExento']+', '+o['nvNetoAfecto']+', '+o['nvTotalDesc']+', '+o['ConcAuto']+', '+o['CodLugarDesp']+',\
                '+o['SolicitadoPor']+', '+o['DespachadoPor']+', '+o['Patente']+', '+o['RetiradoPor']+', '+o['NumOC']+', '+o['CheckeoPorAlarmaVtas']+',\
                '+o['EnMantencion']+', '+o['Usuario']+', '+o['UsuarioGeneraDocto']+', '+o['FechaHoraCreacion']+', '+o['ConcManual']+', '+o['Sistema']+', '+o['CodBodeWms']+','+"'Notas de Venta'"+')'
                
    print(sql)            
    cursor = conn.cursor()
    cursor.execute('INSERT softland.nw_nventa (NVNumero, nvFem, nvEstado, nvEstFact, nvEstDesp, nvEstRese,\
                nvEstConc, CotNum, nvFeEnt, CodAux, VenCod, CodMon, CodLista, nvObser, nvCanalNV,\
                CveCod, NomCon, CodiCC, CodBode, nvSubTotal, nvPorcDesc01, nvDescto01, nvPorcDesc02,\
                nvDescto02, nvPorcDesc03, nvDescto03, nvPorcDesc04, nvDescto04, nvPorcDesc05,\
                nvDescto05, nvMonto, nvFeAprob, NumGuiaRes, nvPorcFlete, nvValflete, nvPorcEmb,\
                nvValEmb, nvEquiv, nvNetoExento, nvNetoAfecto, nvTotalDesc, ConcAuto, CodLugarDesp,\
                SolicitadoPor, DespachadoPor, Patente, RetiradoPor, NumOC, CheckeoPorAlarmaVtas,\
                EnMantencion, Usuario, UsuarioGeneraDocto, FechaHoraCreacion, ConcManual, Sistema, CodBodeWms,Proceso)\
        VALUES('+str(o['NVNumero'])+', '+o['nvFem']+', '+o['nvEstado']+', '+o['nvEstFact']+', '+o['nvEstDesp']+', '+o['nvEstRese']+',\
                '+o['nvEstConc']+', '+o['CotNum']+', '+o['nvFeEnt']+', '+o['CodAux']+', '+o['VenCod']+', '+o['CodMon']+', '+o['CodLista']+', '+o['nvObser']+', '+o['nvCanalNV']+',\
                '+o['CveCod']+', '+o['NomCon']+', '+o['CodiCC']+', '+o['CodBode']+', '+o['nvSubTotal']+', '+o['nvPorcDesc01']+', '+o['nvDescto01']+', '+o['nvPorcDesc02']+',\
                '+o['nvDescto02']+', '+o['nvPorcDesc03']+', '+o['nvDescto03']+', '+o['nvPorcDesc04']+', '+o['nvDescto04']+', '+o['nvPorcDesc05']+',\
                '+o['nvDescto05']+', '+o['nvMonto']+', '+o['nvFeAprob']+', '+o['NumGuiaRes']+', '+o['nvPorcFlete']+', '+o['nvValflete']+', '+o['nvPorcEmb']+',\
                '+o['nvValEmb']+', '+o['nvEquiv']+', '+o['nvNetoExento']+', '+o['nvNetoAfecto']+', '+o['nvTotalDesc']+', '+o['ConcAuto']+', '+o['CodLugarDesp']+',\
                '+o['SolicitadoPor']+', '+o['DespachadoPor']+', '+o['Patente']+', '+o['RetiradoPor']+', '+o['NumOC']+', '+o['CheckeoPorAlarmaVtas']+',\
                '+o['EnMantencion']+', '+o['Usuario']+', '+o['UsuarioGeneraDocto']+', '+o['FechaHoraCreacion']+', '+o['ConcManual']+', '+o['Sistema']+', '+o['CodBodeWms']+','+"'Notas de Venta'"+')')
    conn.commit()
    
    cursor = conn.cursor()
    cursor.execute('INSERT softland.nw_impto (nvNumero, codimpto, valpctIni, afectoImpto, Impto)\
        VALUES('+str(o['NVNumero'])+', '+o['codimpto']+', '+o['valpctIni']+', '+o['afectoImpto']+', '+o['Impto']+')')
    conn.commit()
    

    for i in o['Items']:

        cursor.execute("select max(nvLinea) from softland.nw_detnv where nvNumero = "+str(NVNumero)+" and nvLinea < 1000");
        nvLinea = cursor.fetchone();

        if( nvLinea[0] is None ):
            nvLinea = 1
        else:
            nvLinea = nvLinea[0]+1

        i['NVNumero'] = NVNumero 
        i['nvLinea'] = nvLinea

        cursor.execute('INSERT softland.nw_detnv (NVNumero, nvLinea, nvCorrela, nvFecCompr, CodProd, nvCant,\
                nvPrecio, nvEquiv, nvSubTotal, nvDPorcDesc01, nvDDescto01, nvDPorcDesc02, nvDDescto02,\
                nvDPorcDesc03, nvDDescto03, nvDPorcDesc04, nvDDescto04, nvDPorcDesc05, nvDDescto05,\
                nvTotDesc, nvTotLinea, nvCantDesp, nvCantProd, nvCantFact, nvCantDevuelto, nvCantNC,\
                nvCantBoleta, nvCantOC, DetProd, CheckeoMovporAlarmaVtas, KIT, Partida, Pieza, FechaVencto, CodUMed, CantUVta)\
                VALUES('+str(i['NVNumero'])+', '+str(i['nvLinea'])+', '+i['nvCorrela']+', '+i['nvFecCompr']+', '+i['CodProd']+', '+i['nvCant']+', '+i['nvPrecio']+',\
                '+i['nvEquiv']+', '+i['nvSubTotal']+', '+i['nvDPorcDesc01']+', '+i['nvDDescto01']+', '+i['nvDPorcDesc02']+', '+i['nvDDescto02']+',\
                '+i['nvDPorcDesc03']+', '+i['nvDDescto03']+', '+i['nvDPorcDesc04']+', '+i['nvDDescto04']+', '+i['nvDPorcDesc05']+',\
                '+i['nvDDescto05']+', '+i['nvTotDesc']+', '+i['nvTotLinea']+', '+i['nvCantDesp']+', '+i['nvCantProd']+', '+i['nvCantFact']+',\
                '+i['nvCantDevuelto']+', '+i['nvCantNC']+', '+i['nvCantBoleta']+', '+i['nvCantOC']+', '+i['DetProd']+',\
                '+i['CheckeoMovporAlarmaVtas']+', '+i['KIT']+', '+i['Partida']+', '+i['Pieza']+', '+i['FechaVencto']+', '+i['CodUMed']+', '+i['nvCant']+')')
        conn.commit()