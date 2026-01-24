import sqlite3
import sqlite3 as sql

#Função para criação do arquivo e da tabela de apontamentos, caso não exista

def db_login(login):
    return f"DB/apontamento_{login}.db"

def db(empresa, data, tempo, observacao, login):
    path = db_login(login)
    conect = sqlite3.connect(path)
    cursor = conect.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS apontamentos (id INTEGER PRIMARY KEY AUTOINCREMENT,
         empresa TEXT, data TEXT, tempo INTEGER, observacao TEXT)""")

    cursor.execute("""INSERT INTO apontamentos (empresa, data, tempo, observacao) 
                        VALUES (?, ?, ?, ?) """,
                   (empresa, data, tempo, observacao))

    conect.commit()
    conect.close()

#Função para agrupamento das informações baseado nas empresas

def agrupar(data, login):
    path = db_login(login)
    conect = sqlite3.connect(path)
    cursor = conect.cursor()

    cursor.execute(
        """SELECT empresa, data, SUM(tempo), observacao FROM apontamentos where data = ? GROUP BY empresa""",
        (data,))
    empresas = cursor.fetchall()

    conect.close()
    return empresas

def extract_db(login):
    path = db_login(login)
    conect = sqlite3.connect(path)
    cursor = conect.cursor()

    cursor.execute("""SELECT empresa, data, tempo, observacao FROM apontamentos""")
    extracted = cursor.fetchall()

    conect.close()
    return extracted