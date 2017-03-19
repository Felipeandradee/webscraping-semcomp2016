# -*- coding: utf-8 -*-
import json
import requests
from parsel import Selector

# Define o Accept-Language para acessar a pagina do IMDB em inglês
headers = {'Accept-Language': 'en-US'}
response = requests.get("http://www.imdb.com/chart/top", headers=headers)

# pega a lista do 50 primeiros filmes
filmes = \
    Selector(response.text).xpath(".//tr[position()<=50]/td[@class='titleColumn']/..")

top50 = []

# Para cada filme são pegos algumas informações específicas
for n, filme in enumerate(filmes):
    titulo = filme.xpath(".//td[@class='titleColumn']/a/text()").extract_first()
    elenco = filme.xpath(".//td[@class='titleColumn']//@title").extract_first()
    ano = filme.xpath(".//span[@class='secondaryInfo']/text()").re(".*\((\d+)\).*")[0]
    nota = filme.xpath(".//td[contains(@class,'imdbRating')]/strong/text()").extract_first()

    # É pesquisado no Youtube o trailer do filme baseado no seu nome e ano,
    # admitindo que o primeiro resultado da pequisa é o video com o trailer
    url_youtube = "https://www.youtube.com/results?search_query=%s %s Trailer" % (titulo, ano)
    response_youtube = requests.get(url_youtube)
    trailer = Selector(response_youtube.text).xpath(".//*[@class='yt-lockup-title ']//@href").extract_first()

    trailer = "http://youtube.com" + trailer

    print (u'%i: %s - Ano: %s '
           u'\n\t Elenco: %s '
           u'\n\t Nota: %s '
           u'\n\t Trailer: %s'
           % (n + 1, titulo, ano, elenco, nota, trailer))

    # É adicionado o filme em uma lista
    top50.append({
        'colocacao': n + 1,
        'titulo': titulo,
        'ano': ano,
        'elenco': elenco,
        'nota': nota,
        'trailer': trailer

    })

# por fim a lista de filmes é salva como um Json
with open('top50.json', 'w') as f:
    json.dump(top50, f)

print("lista salva.")
