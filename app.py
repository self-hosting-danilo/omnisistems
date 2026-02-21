from flask import Flask, render_template, request, send_from_directory
import telebot
from dotenv import load_dotenv
import os

load_dotenv()


API_TOKEN_TELEBOT = os.getenv("TELEGRAM_TOKEN", '')
CHAT_ID = os.getenv('CHAT_ID', '')

app = Flask(__name__, static_folder='static')
# bot = telebot.TeleBot(API_TOKEN_TELEBOT)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        servico = request.form.get('servico')
        mensagem = request.form.get('mensagem')

        form_ = f"""Nome: {nome} \n Email: {email} \n serviço: {servico} \n mensagem: {mensagem}"""

        # bot.send_message(CHAT_ID, form_)

    return render_template('index.html')

@app.route("/service-worker.js")
def sw():
    return send_from_directory(".", "service-worker.js")

@app.route("/manifest.json")
def manifest():
    return send_from_directory(".", "manifest.json")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
