import sqlite3
import sqlite3 as sql


def db(empresa, data, tempo, observacao):
    conect = sqlite3.connect("apontamento.db")
    cursor = conect.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS apontamentos (id INTEGER PRIMARY KEY AUTOINCREMENT,
         empresa TEXT, data TEXT, tempo INTEGER, observacao TEXT)""")

    cursor.execute("""INSERT INTO apontamentos (empresa, data, tempo, observacao) 
                        VALUES (?, ?, ?, ?) """,
                   (empresa, data, tempo, observacao))

    conect.commit()
    conect.close()


def agrupar():
    conect = sqlite3.connect("apontamento.db")
    cursor = conect.cursor()

    cursor.execute(
        "SELECT empresa, data, SUM(tempo), GROUP_CONCAT(observacao, '; ') FROM apontamentos GROUP BY empresa, data")
    empresas = cursor.fetchall()

    conect.close()
    return empresas
