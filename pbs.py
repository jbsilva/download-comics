#!/usr/bin/env python3
# -*-*- encoding: utf-8 -*-*-
# Created: Sat, 18 May 2013 15:00:45 -0300

"""Baixa tirinhas do Pearls Before Swine do GoComics"""

# Este código assume algumas coisas que eram verdade (ou não) no momento em que
# foi criado, mas que têm grande chance de mudar caso o site seja modificado:
#   1)  Formato dos links: gocomics.com/pearlsbeforeswine/YYYY/MM/DD
#   2)  Todas as tirinhas possuem versão ampliada. Apenas 3 não tinham:
#       2002/11/25, 2008/04/30 e 2008/05/26.
#   3)  Só existem duas posições para o link da imagem zoom: linha 342 ou 344
#   4)  Se ocorrer um problema na rede o script pode parar. Você terá que
#       vigiar e reiniciá-lo a partir de onde parou.

__author__ = "Julio Batista Silva"
__copyright__ = ""
__license__ = "GPL"
__version__ = "1.0"

import urllib.request
from datetime import date, timedelta

ua = "Mozilla/5.0 (X11; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0"
site = 'http://www.gocomics.com/pearlsbeforeswine/'

d = date(2002, 1, 7)  # Data da primeira tirinha
fim = date.today()    # Data da última tirinha
while d <= fim:
    url = site + d.strftime("%Y/%m/%d")
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    data = urllib.request.urlopen(req).read().decode('utf-8').splitlines()
    url = data[344][627:689] if data[344][627:689] != "" else data[342][627:689]
    try:
        u = urllib.request.urlopen(url)
        ext = u.info().get_filename().split('.')[1]  # Ou get_content_type()
        nome = d.strftime("%Y_%m_%d") + "." + ext
        with open(nome, mode='wb') as arquivo:
            arquivo.write(u.read())
    except:
        print("Erro no arquivo {}".format(nome))
    d += timedelta(1)
