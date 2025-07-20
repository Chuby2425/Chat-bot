import sqlite3
import unicodedata

DB_NAME = 'chat.db'

def normalizar(texto):
    texto = texto.lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')  # quita tildes
    return texto

def generar_respuesta(mensaje_usuario):
    mensaje_normalizado = normalizar(mensaje_usuario)
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT pregunta, respuesta FROM respuestas")
    filas = c.fetchall()
    conn.close()

    for pregunta, respuesta in filas:
        # Normaliza CADA palabra clave en la pregunta (antes no lo hacía)
        claves_normalizadas = [normalizar(clave.strip()) for clave in pregunta.split(',')]
        
        # Verifica si ALGUNA clave normalizada está ENTERA en el mensaje
        for clave in claves_normalizadas:
            if clave in mensaje_normalizado.split() or clave == mensaje_normalizado:
                return respuesta

    return "Bot: No entendí tu consulta, ¿podrías reformularla? 🤔"