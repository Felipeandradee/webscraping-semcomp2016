# -*- coding: utf-8 -*-
import requests

# Faz uma requisição do tipo GET e coloca o retorno na variavel response
response = requests.get("http://semcomp.com.br/programacao")

# Cria um arquivo html com o conteudo do response
with open('programacao.html', 'w') as f:
    f.write((response.text).encode('utf-8'))
    f.close()

print("Arquivo criado.")
