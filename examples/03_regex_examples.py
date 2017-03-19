# -*- coding: utf-8 -*-
import re
import requests
from parsel import Selector

# Pode usar RegEx para que o parsel retorne uma lista contendo apenas uma parte específica do texto,
# Exemplo:
# texto: 08:00 ~ 12:00
# RegEx: .* (.+) ~.*
# retorno: 08:00
response = requests.get("http://semcomp.com.br/programacao")
sel = Selector(response.text).xpath(u".//*[@title='Horário']/text()").re(".* (.+) ~.*")
print ("RegEx horários de palestras SemComp: %s" % sel)

# RegEx para validar um username baseado nas regras:
# pode possuir de 3 à 16 caracteres sendo eles letras, números, _ (underline) e - (hífen)
# Exemplo:
# username = "Felipe_831"
# Valido
# username = "$|Felip3|$"
# Invalido
username = "_Felipe-123"
pattern = re.compile("^[a-zA-Z0-9_-]{3,16}$")
if pattern.match(username):
    print("Valido")
else:
    print("Invalido")

# RegEx para encontrar emails em um site
response = requests.get("https://blogs.msdn.microsoft.com/testing123/2009/02/06/email-address-test-cases/")
sel_footer = Selector(response.text).xpath(".//text()").re("([\w\.\-]+@[\w\-]+\.[\w\.]{2,6}$)")
for n, s in enumerate(sel_footer):
    print ("%i : %s" % (n+1, s))