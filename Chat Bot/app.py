from flask import Flask
from chatbot.routes import chatbot_bp
from chatbot.db import crear_tabla, insertar_respuestas_iniciales

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chatbot_bp)  
    crear_tabla()
    insertar_respuestas_iniciales()   
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True)  # Añade ssl_context
