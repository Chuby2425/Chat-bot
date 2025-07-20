
# 🤖 ChatBot en Flask

Este es un proyecto de chatbot simple desarrollado con **Python**, **Flask** y **SQLite**. El bot responde automáticamente a consultas del usuario utilizando palabras clave definidas en una base de datos local (`chat.db`).

---

## 🚀 Funcionalidades

- Responde a saludos, precios, ubicación, horario, servicios, entre otros.
- Lee palabras clave desde una tabla en SQLite para generar respuestas.
- Guarda el historial de mensajes del usuario en la base de datos.
- Interfaz web básica para interactuar con el chatbot.

---

## 🧱 Estructura del Proyecto

```
chatbot/
│
├── app.py                  # Punto de entrada principal
├── chatbot/
│   ├── __init__.py         # Crea y configura la app de Flask
│   ├── routes.py           # Define las rutas del chatbot
│   ├── logic.py            # Lógica para generar respuestas
│   ├── db.py               # Funciones para gestionar SQLite
│
├── templates/
│   └── index.html          # Interfaz del usuario
│
├── static/
│   └── style.css           # Estilos (opcional)
│
├── chat.db                 # Base de datos SQLite
└── README.md               # Este archivo
```

---

## ⚙️ Requisitos

- Python 3.8+
- Flask

Instalación de dependencias:

```bash
pip install flask
```

---

## ▶️ Cómo ejecutar la app

1. Cloná o copiá este repositorio.
2. Asegurate de tener `chat.db` y que esté inicializado.
3. Ejecutá la aplicación:

```bash
python app.py
```

4. Abrí tu navegador en `http://localhost:5000`

---

## 🧠 Cómo funciona el chatbot

- Las **palabras clave** están almacenadas en la tabla `respuestas` de la base de datos `chat.db`.
- Cuando el usuario escribe un mensaje, se busca si alguna palabra clave está contenida en su texto.
- Si se encuentra coincidencia, se devuelve la respuesta relacionada.

---

## 📦 Base de datos

El archivo `db.py` se encarga de:

- Crear las tablas `mensajes` y `respuestas` si no existen.
- Insertar respuestas iniciales.
- Guardar el historial de los mensajes.

---

## ✨ Ejemplo de palabras clave

```
pregunta: hola,buenas,hey
respuesta: ¡Hola! ¿En qué te puedo ayudar hoy? 😊
```

---

## 📍 Ubicación del negocio (ejemplo real)

> Estamos en Santiago de Puriscal, 50 metros norte del Ministerio de Salud. 📍

---

## 📞 Contacto

> WhatsApp: 6396-9171  
> Redes sociales: Facebook e Instagram como @eyvtechnology

---

## 📅 Horario

> Lunes a sábado: 8:00 a.m. – 5:00 p.m.

---

## ✅ Estado

Proyecto en desarrollo. Puedes modificar `chat.db` para agregar más respuestas y funcionalidades.

---

## Licencia

Este proyecto es de uso libre para propósitos educativos o personales.
