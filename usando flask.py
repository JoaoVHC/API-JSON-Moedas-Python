from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,CLP-BRL")
    dic_requisicao = requisicao.json()
    return render_template('index.html', clp_bid=dic_requisicao['CLPBRL']['bid'], usd_bid=dic_requisicao['USDBRL']['bid'])

if __name__ == '__main__':
    app.run(debug=True)