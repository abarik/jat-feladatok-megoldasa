# 028 Feladat
# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik.
# Kétféle italt ismerünk: sör és kóla.
# Ha a felhasználó kiskorú, és sört kér, akkor közöld vele,
# hogy sajnos nem adhatsz neki. Ha a felhasználó 60 feletti, és
# kólát kér, akkor közöld vele, hogy a koffein megemelheti a
# vérnyomását. Ha ismeretlen italt adott meg, akkor írd ki,
# hogy csak sört és kólát tudunk adni.
# Minden más esetben szolgáld ki.
# (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")
# A megoldást egy bartender.py nevű file-ban kell beadnod.

age = int(input('Életkorod? '))
ital = input('Mit innál? ')
if age < 18 and ital == "sör":
    print('Sajnos nem adhatok sört!')
elif age > 60 and ital == 'kóla':
    print('A kóla koffein tartalma emelheti a vérnyomást!')
elif ital not in ['sör', 'kóla']:
    print('Sajnos csak sör és kóla kapható!')
elif ital == 'sör':
    print('Parancsoljon, a söre.')
elif ital == 'kóla':
    print('Parancsoljon,a kólája.')
