import os
import psycopg2

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

#rota para a exibição das notas por aluno
@router.get("/status")
async def ping(settings: Settings = Depends(get_settings)):
    con = psycopg2.connect(host="localhost", database="ArchDB", user="admin", password="admin")
    cur = con.cursor()
    sql = '''
        select nome, n1, n2, n3, n4, idaluno, n.id 
        from notas n 
        inner join aluno a on a.id = n.idaluno 
    '''
    cur.execute(sql)
    recset = cur.fetchall()
    response = {'nome': [], 'n1': [], 'n2': [], 'n3': [], 'n4': [], 'idaluno': [], 'idnota': []}
    data = {}
    for i, rec in enumerate(recset):
        response['nome'].append(recset[i][0])
        response['n1'].append(recset[i][1])
        response["n2"].append(recset[i][2])
        response["n3"].append(recset[i][3])
        response["n4"].append(recset[i][4])
        response["idaluno"].append(recset[i][5])
        response["idnota"].append(recset[i][6])

    #print (response)
        data[f'aluno {response["idnota"][i]}'] = {'nome': response['nome'][i], 'n1': response['n1'][i],
                                                  'n2': response['n2'][i], 'n3': response['n3'][i],
                                                  'n4': response['n4'][i], 'idaluno': response['idaluno'][i]}

    #data = dict(zip(recset[0], recset[1]))
    print(data)

    return {
        "response": data
    }