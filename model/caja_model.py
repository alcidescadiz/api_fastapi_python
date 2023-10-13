from config.cnx import SqlQuerys

class caja_model(SqlQuerys):
    SqlQueryCreateCaja= f'''CREATE TABLE IF NOT EXISTS nombre_tabla(
        id INTEGER PRIMARY KEY AUTOINCREMENT , 
        fecha VARCHAR(100) NOT NULL,
        tipo CHAR(20),
        descripcion VARCHAR(255),
        ingreso DECIMAL(10,2) DEFAULT 0,
        egreso DECIMAL(10,2) DEFAULT 0
    )'''
    SqlQueryAddRowsInCaja = lambda caja : f'''INSERT INTO caja(tipo,ingreso,fecha,descripcion,egreso) VALUES('{caja.tipo}',{caja.ingreso},'{caja.fecha}','{caja.descripcion}',{caja.egreso});'''
    SqlQueryEditRowsInCaja=  lambda caja,id : f'''UPDATE caja SET tipo='{caja.tipo}', ingreso={caja.ingreso},fecha='{caja.fecha}',descripcion='{caja.descripcion}',egreso={caja.egreso} where id={id};'''
    
