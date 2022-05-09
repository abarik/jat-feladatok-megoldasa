from os import system, name


def show_screen():
    """
    Menü megjelenítése
    """
    print('0. Menü nyomtatása')
    print('1. Kocsi felvétel.  Adja meg a kocsi márkáját és alvázszámát.')
    print('2, Összes kocsi adatainak lekérdezese')
    print('3, Kocsi adatainak lekérdezese index/key alapján. (márka, alvázszámát)')
    print('4, Kocsi eladása (töröljük a rendszerből egy kocsit)')
    print('5, Kilépés az applikáciobol')


def insert_car(db):
    marka = input('Adja meg a kocsi márkáját: ')
    alvsz = input('Adja meg a kocsi alvázszámát: ')
    db['auto_increment_id'] += 1
    db['cars'].append({
        'id': db['auto_increment_id'],
        'marka': marka,
        'alvsz': alvsz
    })


def list_cars(db):
    if len(db['cars']) > 0:
        for car in db['cars']:
            print(f'ID: {car["id"]}, Márka: {car["marka"]}, Alvázszáma: {car["alvsz"]}')
    else:
        print('Üres a lista!')


def show_car(db):
    try:
        id = int(input('Adja meg a lekérdezendő kocsi azonosítóját (ID): '))
    except ValueError:
        print('Nem számot adott meg!')
    else:
        output = False
        for car in db['cars']:
            if car['id'] == id:
                print(f'({car["marka"]}, {car["alvsz"]})')
                output = True
                break
        if not output:
            print("Nincs ilyen ID!")


def del_car(db):
    try:
        id = int(input('Adja meg a törlendő kocsi azonosítóját (ID): '))
    except ValueError:
        print('Nem számot adott meg!')
    else:
        torles = False
        for car in db['cars']:
            if car['id'] == id:
                db['cars'].remove(car)
                torles = True
                break
        if not torles:
            print("Nem történt törlés (nincs ilyen ID)!")
