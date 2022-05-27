from car_salon_new.bolt import Bolt

salon = Bolt()


def show_screen():
    """
    Menü megjelenítése
    """
    print('0. Menü nyomtatása')
    print('1. Kocsi felvétel.  Adja meg a kocsi adatait.')
    print('2, Összes kocsi adatainak lekérdezese')
    print('3. Elado felvétel.  Adja meg az eladó adatait.')
    print('4, Elado adatainak lekérdezese')
    print('5. Vevő felvétel.  Adja meg a vevő adatait.')
    print('6, Összes vevő adatainak lekérdezese')
    print('7, Kocsi eladása')
    print('8, Eladások listája')
    print('9, Kilépés az applikáciobol')



show_screen()  # kiírás a képernyőre
while True:
    try:
        select = int(input('Kérem válasszon: '))
    except ValueError:
        print('Kérem számot adjon meg (0-9)!')
        continue

    if select not in range(10):
        print('Kérem 0 és 9 közötti számot adjon meg!')
        continue

    match select:
        case 0:
            show_screen()
        case 1:
            salon.uj_kocsi()
        case 2:
            salon.lista_kocsi()
        case 3:
            salon.uj_elado()
        case 4:
            salon.lista_elado()
        case 5:
            salon.uj_vevo()
        case 6:
            salon.lista_vevo()
        case 7:
            salon.uj_eladas()
        case 8:
            salon.lista_eladas()
        case 9:
            print('Viszlát, legközelebb!')
            break  # kilépés a while-ból
