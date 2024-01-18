from flask import Flask, render_template # Estruturas para criar o site
from flask_socketio import SocketIO, send # estruturas para criar o chat

chave_seguranca = "dinx0ej23mrce-0,mrx0-2,r-029,0@#$%¨&*()"

app = Flask(__name__)
app.config["SECRET"] = chave_seguranca
app.config["DEBUG"] = True
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host='localhost')