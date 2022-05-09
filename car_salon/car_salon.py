# - Írjunk egy programot, ami induláskor nyomtat nekünk egy menüt és az alábbi funkciókat tudja.

#   0. Menu nyomtatása.
#   1. Kocsi felvétel.  Adja meg a kocsi márkáját és alvázszámát.
#   2, Összes kocsi adatainak lekérdezese
#   3, Kocsi adatainak lekérdezese index/key alapján. (márka, alvázszámát)
#   4, Kocsi eladása (töröljük a rendszerből egy kocsit)
#   5, Kilépés az applikáciobol



import car_salon_utils as csu

car_db = {
    'auto_increment_id': 0,
    'cars': []  # üres adatbázisal indítunk
}
# car_db['cars'].append({'ss':12})
# print(car_db)
csu.show_screen()  # kiírás a képernyőre
while True:
    try:
        select = int(input('Kérem válasszon: '))
    except ValueError:
        print('Kérem számot adjon meg (0-5)!')
        continue

    if select not in range(6):
        print('Kérem 0 és 5 közötti számot adjon meg!')
        continue

    match select:
        case 0:
            csu.show_screen()
        case 1:
            csu.insert_car(car_db)
        case 2:
            csu.list_cars(car_db)
        case 3:
            csu.show_car(car_db)
        case 4:
            csu.del_car(car_db)
        case 5:
            print('Viszlát, legközelebb!')
            break  # kilépés a while-ból
