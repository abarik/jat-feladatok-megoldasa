# 032 Feladat
# Írj programot, mely addig olvas be számokat a billentyűzetről,
# ameddig azok kisebbek, mint tíz. Írja ki ezek után a
# beolvasott számok összegét!

sum = 0
while True:
    number = int(input('Kérek egy számot: '))
    if number < 10:
        sum += number
    else:
        break
print(f'A begépelt számok összege: {sum}')