# -*- coding: utf-8 -*-
import requests
from parsel import Selector

# faz uma requisição do tipo get no site com a programação da SemComp
response = requests.get("http://semcomp.com.br/programacao")

# Pega a div que contém as informações por dia de evento
dias = Selector(response.text).xpath('.//div[contains(@class, "daily-schedule")]')
for i, dia in enumerate(dias):

    print('\nDia: %i\n' % (i+1))

    # Pega as divs com as informações de todas as palestras do dia
    palestrantes = dia.xpath('.//div[@class="talk-details"]')

    # Para cada palestra imprime o horário, nome do palestrante e o tema
    for n, p in enumerate(palestrantes):
        horario = p.xpath(u'.//div[@title="Horário"]//text()').extract_first()
        palestrante = p.xpath('.//div[@title="Palestrante"]//text()').extract_first()
        tema = p.xpath('.//*[@class="talk-title"]//text()').extract_first()

        print(u"%s - %s: %s - %s" % (str(n+1), horario, palestrante, tema))

