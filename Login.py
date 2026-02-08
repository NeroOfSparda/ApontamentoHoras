import sys
import os
import sqlite3
import sqlite3 as sql
from Utils import resource_path

def acess(login, password):
    acessos_path = resource_path("DB/acessos.db")
    conect = sqlite3.connect(acessos_path)
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
    acessos_path = resource_path("DB/acessos.db")
    conect = sqlite3.connect(acessos_path)
    cursor = conect.cursor()

    cursor.execute("""SELECT 1 FROM USERS 
                       WHERE login = ? AND password = ?""",
            (login, password))
    resultado = cursor.fetchone()

    conect.close()
    return resultado is not None
