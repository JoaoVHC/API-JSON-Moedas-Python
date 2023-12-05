from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,CLP-BRL")
    dic_requisicao = requisicao.json()
    titulo = "Bem vindo a cotação em tempo real de moedas"
    return render_template('index.html', clp_bid=dic_requisicao['CLPBRL']['bid'], usd_bid=dic_requisicao['USDBRL']['bid'])

if __name__ == '__main__':
    app.run(debug=True)