import requests
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,CLP-BRL")

print(requisicao)
print(requisicao.json())
dic_requisicao = requisicao.json()
print(f"Cotação de 1 Peso Chileno para Real é: {dic_requisicao['CLPBRL']['bid']}")
print(f"Cotação de 1 Dolar para Real é: {dic_requisicao['USDBRL']['bid']}")