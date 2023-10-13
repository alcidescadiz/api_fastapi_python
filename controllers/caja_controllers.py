from config.cnx import SqlSentenceSelect, SqlSentence
from model.caja_model import caja_model
nombre_tabla ='caja'
class caja_controllers:
    get_all_cajas = lambda : SqlSentenceSelect(caja_model.SqlQueryGetAll(nombre_tabla))
    get_one_caja  = lambda id: SqlSentenceSelect(caja_model.SqlQueryGetOne(nombre_tabla, id))
    create_caja  = lambda caja: SqlSentence(caja_model.SqlQueryAddRowsInCaja(caja))
    edit_caja  = lambda caja,id: SqlSentence(caja_model.SqlQueryEditRowsInCaja(caja,id))
    delete_one_caja  = lambda id: SqlSentence(caja_model.SqlQueryDeleteOne(nombre_tabla, id))