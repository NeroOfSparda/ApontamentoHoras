import sqlite3
import sqlite3 as sql

from fontTools.unicodedata.Blocks import VALUES


def db(empresa, data, tempo, observacao):
    conect = sqlite3.connect("apontamento.db")
    cursor = conect.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS apontamentos (id INTEGER PRIMARY KEY AUTOINCREMENT,
         empresa TEXT, data TEXT, tempo TEXT, observacao TEXT)""")

    cursor.execute("""INSERT INTO apontamentos (empresa, data, tempo, observacao) 
                        VALUES (?, ?, ?, ?) """,
              (empresa, data, tempo, observacao))

    conect.commit()
    conect.close()

def agrupar():

    conect = sqlite3.connect("apontamento.db")
    cursor = conect.cursor()

    cursor.execute("select distinct empresa from apontamentos")
    empresas = cursor.fetchall()

    conect.close()
    return empresas


