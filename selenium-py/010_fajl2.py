# 026 Feladat: filekezelés gyakorlása
# Olvasd be a fájlt, tárold a sorokat listában,
# majd írd ki a lista tartalmát egy sorban!
# A megoldást egy fajl2.py nevű file-ban kell beadnod.


with open('adat.txt', 'r') as f:
    my_list = f.readlines()
    # print(my_list)
    print(' '.join(my_list).replace('\n', ''))
