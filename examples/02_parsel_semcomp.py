# -*- coding: utf-8 -*-
import requests
from parsel import Selector

# Faz uma requisição do tipo GET e guarda o retorno na variável response
response = requests.get("http://semcomp.com.br/programacao")

# Exemplo utilizando um seletor css e extraindo apenas o primeiro item que atende a condição
# Obs: caso não encontrasse nenhum item que atendesse a condição o retorno seria None
sel_css = Selector(response.text).css("h1::text").extract_first()
print(sel_css)

# Exemplo utilizando xpath e extraindo uma lista de todos os itens que atendem a condição
# Obs: caso não encontrasse nenhum item que atendesse a condição o retorno seria uma lista vazia
sel_xpath = Selector(response.text).xpath(".//*[@class='talk-title']/text()").extract()
print(sel_xpath)