import orodja
import re
import requests

STEVILO_STRANI =1

vzorec = (r'players.+?">(?P<ime>.+?)<.*? data-stat="pos" >(?P<pozicija>.*?)<.*?stat="age" >(?P<starost>.*?)<.*?href="/teams.*?">(?P<ekipa>.*?)<.*?stat="g" >(?P<odigrane>.*?)<.*?data-stat="gs" >(?P<zacete>.*?)<.*?data-stat="mp_per_g" >(?P<minute>.*?)<.*?stat="trb_per_g" >(?P<rebounds>.*?)<.*?data-stat="ast_per_g" >(?P<asistence>.*?)<.*?data-stat="stl_per_g" >(?P<steals>.*?)<.*?data-stat="blk_per_g" >(?P<blokade>.*?)<.*?data-stat="tov_per_g" >(?P<turnovers>.*?)<.*?data-stat="pts_per_g" >(?P<tocke>.*?)<')


igralci = 0

#for stran in range(STEVILO_STRANI):
#    stran += 1
#    url = "https://www.basketball-reference.com/leagues/NBA_2022_per_game.html"
#    datoteka = "Nba.html"
#    orodja.shrani_spletno_stran(url, datoteka)
#    vsebina = orodja.vsebina_datoteke(datoteka)
#
#    with open('zadetki.html', 'a', encoding='utf-8') as f:
#        for zadetek in re.finditer(vzorec, vsebina, flags=re.DOTALL):
#            print(zadetek.groupdict(), file=f, end=",\n")
#            igralci += 1


with open("zadetki.html", 'r', encoding='utf-8') as f:
    seznam = f.read()
    seznam = eval(seznam)
    orodja.zapisi_csv(seznam,["ime","pozicija","starost","ekipa","odigrane","zacete","minute","rebounds","asistence","steals","blokade","turnovers","tocke"],"csv_file")
