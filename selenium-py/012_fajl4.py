# 026 Feladat: filekezelés gyakorlása
# Olvasd be a fájlt, tárold a sorokat listában,
# majd írd ki a lista tartalmát így, ahogy beolvastad,
# soronként egy szóval egy másik fájlba!
# A megoldást egy fajl4.py nevű file-ban kell beadnod.

with open('adat.txt', 'r') as f:
    with open('kiir_2.txt', 'w') as f_out:
        line = f.readline()
        while line:
            f_out.write(line)
            line = f.readline()
