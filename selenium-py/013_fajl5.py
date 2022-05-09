# 026 Feladat: filekezelés gyakorlása
# Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba,
# úgy, hogy nem tárolod el a szöveget, hanem minden sort azonnal kiírsz!
# A megoldást egy fajl5.py nevű file-ban kell beadnod.


with open('adat.txt', 'r') as f:
    with open('kiir_3.txt', 'w') as f_out:
        f_out.write(f.read())
