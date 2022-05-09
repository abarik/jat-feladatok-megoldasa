# 037 Feladat
# Szökőév?
# Készíts függvényt, amelyik adott évszámról eldönti,
# hogy az szökőév-e. Szökőév minden negyedik, nem szökőév minden századik,
# mégis az minden 400-adik. (2000-ben ezért volt szökőév.)
# A függvény visszatérési értéke legyen logikai típusú!
# Tipp( % maradekos osztas operátor)
# Írj programot, amelyik a felhasználótól évszámokat kér,
# és mindegyikre kiírja, hogy szökőév-e!
# Használd az előbb megírt függvényt!
# Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900
# Nem szökőév.
# A megoldást egy szokoev.py nevű file-ban kell beadnod.


def szokoev(ev):
    return (ev % 4 == 0 and ev % 100 != 0) or ev % 400 == 0


ev = int(input('Mondjon egy évszámot: '))
print('Szökőév' if szokoev(ev) else 'Nem szökőév')
