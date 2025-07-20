import sqlite3

DB_NAME = 'chat.db'

def ver_tabla_respuestas():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, pregunta, respuesta FROM respuestas")
    filas = c.fetchall()
    conn.close()

    for fila in filas:
        print(f"ID: {fila[0]} | Preguntas clave: {fila[1]} | Respuesta: {fila[2]}")

ver_tabla_respuestas()
