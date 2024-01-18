from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "dinx0ej23mrce-0,mrx0-2,r-029,0@#$%¨&*()"
app.debug = True  # Adicionando modo de depuração
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)

@app.route("/")
def home():
    return render_template("homepage.html")


if __name__ == "__main__":
    socketio.run(app, host='localhost')
