import sqlite3
import sqlite3 as sql

def acess(login, password):
    conect = sqlite3.connect("acessos.db")
    cursor = conect.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY AUTOINCREMENT,
         login TEXT, password TEXT)""")

    cursor.execute("""INSERT INTO USERS (login, password) 
                        VALUES (?, ?) """,
                   (login, password))

    conect.commit()
    conect.close()


def select(login, password):
    conect = sqlite3.connect("acessos.db")
    cursor = conect.cursor()

    cursor.execute("""SELECT login, password FROM USERS 
                       WHERE login = ? AND password = ?""",
            (login, password))
    resultado = cursor.fetchone()

    conect.close()
    return resultado
