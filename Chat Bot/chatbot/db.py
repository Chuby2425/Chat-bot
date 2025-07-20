import sqlite3

DB_NAME = 'chat.db'

def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            mensaje TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS respuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pregunta TEXT,
            respuesta TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insertar_respuestas_iniciales():
    respuestas = [
        ("hola,buenas,hey,holi,qué tal,buenos días,buenas tardes,holaaa", "¡Hola! ¿En qué te puedo ayudar hoy? 😊"),
        ("precio,precios,cuánto cuesta,vale,tarifa,cobran,cuánto es,cotización,cotizar", "Los precios varían según el servicio que necesites. ¿Te interesa algo específico?"),
        ("servicio,servicios,ofrecen,qué hacen,tipo de trabajo,qué brindan,trabajos,actividades", "Ofrecemos mantenimiento, pintura, luces, limpieza, revisiones y más. 🚗✨"),
        ("dónde están,ubicación,cómo llegar,dirección,están ubicados,lugar,dónde queda", "Estamos en Santiago de Puriscal, 50 metros norte del Ministerio de Salud. 📍"),
        ("horario,abren,horarios,cierran,horas de atención,cuándo abren,cuándo cierran", "Nuestro horario es de lunes a sábado, de 8:00 a.m. a 5:00 p.m. ⏰"),
        ("cita,agendar,reservar,disponibilidad,programar,agenda", "Podés agendar una cita escribiéndonos por aquí o llamando directamente. 📅"),
        ("teléfono,número,contacto,llamar,whatsapp,celular", "Claro, podés llamarnos o escribirnos al 6396-9171. 📞"),
        ("facebook,instagram,redes sociales,tienen redes,redes,social media", "Sí, estamos en Facebook e Instagram como @fastriders 📱"),
        ("formas de pago,métodos de pago,aceptan sinpe,pago,tarjetas,efectivo,transferencia", "Aceptamos efectivo, SINPE Móvil y transferencias bancarias. 💳"),
        ("emergencia,urgencia,urge,urgente,rápido,express,prisa,atención inmediata", "Sí, atendemos casos urgentes. Avisanos y te damos prioridad. 🚨")
    ]

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Limpia la tabla para evitar duplicados (opcional pero recomendado)
    c.execute("DELETE FROM respuestas")
    
    for pregunta, respuesta in respuestas:
        c.execute("INSERT INTO respuestas (pregunta, respuesta) VALUES (?, ?)", (pregunta, respuesta))
    
    conn.commit()
    conn.close()

def obtener_respuestas():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT pregunta, respuesta FROM respuestas")
    filas = c.fetchall()
    conn.close()
    return filas

def guardar_mensaje(usuario, mensaje):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO mensajes (usuario, mensaje) VALUES (?, ?)", (usuario, mensaje))
    conn.commit()
    conn.close()