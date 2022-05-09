# 026 Feladat: filekezelés gyakorlása
# Olvasd be a fájlt, tárold a sorokat listában,
# majd írd ki a lista tartalmát egy sorként egy másik fájlba!
# A megoldást egy fajl3.py nevű file-ban kell beadnod.

with open('adat.txt', 'r') as f:
    with open('kiir_1.txt', 'w') as f_out:
        my_list = f.readlines()
        for line in my_list:
            f_out.write(line)
