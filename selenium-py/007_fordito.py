# 010 Feladat
# Írj egy Python programot, amely a felhasználótól pozitív számokat
# kér be mindaddig, amíg a felhasználó nullát nem ad be!
# A program az összes értéket tárolja egy listában,
# majd írja ki a képernyőre a lista elemeit fordított sorrendben!
# A megoldást egy fordito.py nevű file-ban kell beadnod.

my_list = list()

while True:
    num = int(input('Kérek egy számot: '))
    if num != 0:
        my_list.insert(0, num)
    else:
        break
print(my_list)
