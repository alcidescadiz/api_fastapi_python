import sqlite3

def SqlSentence(sqlSentence=''):
    conn = sqlite3.connect('./config/DB.db')
    cursor = conn.cursor()
    sql =sqlSentence
    cursor.execute(sql)
    conn.commit()
    conn.close()
    

def SqlSentenceSelect(sqlSentence=''):
    conn = sqlite3.connect('./config/DB.db')
    cursor = conn.cursor()
    sql =sqlSentence
    cursor.execute(sql)
    return cursor.fetchall()
    
class SqlQuerys:
    SqlQueryCreateTable= f'''CREATE TABLE IF NOT EXISTS nombre_tabla(
        id INTEGER PRIMARY KEY AUTOINCREMENT , 
        fecha VARCHAR(100) NOT NULL,
        tipo CHAR(20),
        descripcion VARCHAR(255),
        ingreso DECIMAL(10,2) DEFAULT 0,
        egreso DECIMAL(10,2) DEFAULT 0
    )'''
    SqlQueryGetAll= lambda nombreTabla :f'''select * from {nombreTabla} '''
    SqlQueryGetOne= lambda nombreTabla, id :f'''select * from {nombreTabla} where id={id}'''
    SqlQueryAddRows = lambda caja : f'''INSERT INTO caja(tipo,ingreso,fecha,descripcion,egreso) VALUES('{caja.tipo}',{caja.ingreso},'{caja.fecha}','{caja.descripcion}',{caja.egreso});'''



