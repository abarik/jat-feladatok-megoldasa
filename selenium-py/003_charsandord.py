# 022 Feladat
# Írj programot, ami kiírja a kisbetűket, és melléjük az karakter kódjukat! A kiírás több oszlopos legyen, és legfeljebb 10 soros. Minta:
# a 97 f 102 .....
# b 98 g 103
# c 99 h 104
# d 100 i 105
# e 101 j 106
# A megoldashoz használd a beépített ord() es chr() függvényeket.
#
# A megoldást egy charsandord.py nevű file-ban kell beadnod.



print('1. megoldás --------------------')
codes = range(ord('a'), ord('z') + 1)  # a kisbetűk belső kódja
for i in range(ord('a'), ord('z') + 1):
    print(f'{chr(i)} {i}')


print('2. megoldás --------------------')
max_line = 10  # maximálisan ennyo sor íródhat ki
codes = range(ord('a'), ord('z') + 1)  # a kisbetűk belső kódja
# az oszlopok száma
col = len(codes) // max_line + (1 if len(codes) % max_line > 0 else 0)
for i in range(max_line):
    for j in range(col):
        index = i * col + j
        if index < len(codes):
            code = codes[index]
            print(f'{chr(code)} {code}', end=' ')
    print()

print('3. megoldás --------------------')
max_line = 10  # maximálisan ennyo sor íródhat ki
codes = range(ord('a'), ord('z') + 1)  # a kisbetűk belső kódja
# az oszlopok száma
col = len(codes) // max_line + (1 if len(codes) % max_line > 0 else 0)
for i in range(max_line):
    for j in range(col):
        index = j * max_line + i
        if index < len(codes):
            code = codes[index]
            print(f'{chr(code)} {code}', end=' ')
    print()
