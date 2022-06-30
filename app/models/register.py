import psycopg2


class CreateTables:

    create_aluno = 'CREATE TABLE if not exists public.aluno(id serial unique primary key, nome varchar(80))'
    insert_notas = "insert into aluno values (default,'Guilherme'), (default, 'Arch')"

    create_notas = '''
    CREATE TABLE if not exists notas(
       id serial unique primary key,
       idAluno bigint,
       n1 INT,
       n2 INT,
       n3 INT,
       n4 INT,
       CONSTRAINT idAluno
       FOREIGN KEY(idAluno) 
       REFERENCES aluno(id));
    '''

    def start(self):
        con = psycopg2.connect(host="localhost", database="ArchDB", user="admin", password="admin")
        cur = con.cursor()
        cur.execute(self.create_aluno)
        cur.execute(self.insert_notas)
        cur.execute(self.create_notas)
        con.commit()
        con.close()
