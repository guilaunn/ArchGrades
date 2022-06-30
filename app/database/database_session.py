import psycopg2
from app.models.register import CreateTables

#conectando com o banco, verificando se as tabelas ja foram criadas, caso não foram, são criadas
def global_init() -> None:

    con = psycopg2.connect(host="localhost", database="ArchDB", user="admin", password="admin")
    cur = con.cursor()
    sql = "select table_name  from information_schema.tables where table_schema = 'public'"
    cur.execute(sql)
    recset = cur.fetchall()
    if len(recset) == 0:
        steps = [CreateTables()]
        for step in steps:
            step.start()
    con.close()

