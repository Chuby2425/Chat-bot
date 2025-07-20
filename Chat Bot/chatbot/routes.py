from flask import Blueprint, request, jsonify, render_template
import sqlite3
from chatbot.db import guardar_mensaje
from chatbot.responses import generar_respuesta  # <-- Añade esto


chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/')
def index():
    return render_template('index.html')

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    mensaje_usuario = data.get('mensaje', '').lower().strip()
    guardar_mensaje('usuario', mensaje_usuario)

    respuesta_bot = generar_respuesta(mensaje_usuario)
    guardar_mensaje('bot', respuesta_bot)

    return jsonify({'respuesta': respuesta_bot})

@chatbot_bp.route('/add_response', methods=['POST'])
def add_response():
    try:
        data = request.get_json()
        if not data or 'pregunta' not in data or 'respuesta' not in data:
            return jsonify({"error": "Datos incompletos"}), 400

        conn = sqlite3.connect('chat.db')
        c = conn.cursor()
        c.execute("INSERT INTO respuestas (pregunta, respuesta) VALUES (?, ?)", 
                 (data['pregunta'], data['respuesta']))
        conn.commit()
        conn.close()
        
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500