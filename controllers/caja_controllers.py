from config.cnx import SqlQuerys,SqlSentenceSelect, SqlSentence
nombre_tabla ='caja'
class caja_controllers:
    get_all_cajas = lambda : SqlSentenceSelect(SqlQuerys.SqlQueryGetAll(nombre_tabla))
    get_one_caja  = lambda id: SqlSentenceSelect(SqlQuerys.SqlQueryGetOne(nombre_tabla, id))
    create_caja  = lambda caja: SqlSentence(SqlQuerys.SqlQueryAddRows(caja))