import sqlite3

def SqlSentence(sqlSentence=''):
    conn = sqlite3.connect('./config/DB.db')
    cursor = conn.cursor()
    sql =sqlSentence
    cursor.execute(sql)
    conn.commit()
    return conn.total_changes
    

def SqlSentenceSelect(sqlSentence=''):
    conn = sqlite3.connect('./config/DB.db')
    cursor = conn.cursor()
    sql =sqlSentence
    cursor.execute(sql)
    return cursor.fetchall()
    
class SqlQuerys:
    SqlQueryGetAll:str= lambda nombreTabla :f'''select * from {nombreTabla} '''
    SqlQueryGetOne:str= lambda nombreTabla, id :f'''select * from {nombreTabla} where id={id}'''
    SqlQueryDeleteOne:str= lambda nombreTabla, id :f'''DELETE from {nombreTabla} where id={id}'''
    


