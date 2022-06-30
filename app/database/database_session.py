import psycopg2
from app.models.register import CreateTables


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


