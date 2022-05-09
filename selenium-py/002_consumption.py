# 016 Feladat
# Az autód 7 litert fogyaszt országúton és 9-et városban.
# A hévízi üdülésedre 170 kilómétert utazol országúton és 35-öt városban.
# Mennyit fogyaszt az autód csak oda?
# És oda-vissza?
# Mennyibe kerül a teljes út, ha 350 Ft a benzin?
# Oldd meg ezt feladatot úgy, hogy nem előre megadott
# értékekkel (országúti fogyasztás, városi fogyasztás, országúton
# megtett út, városban megtett út, benzin ára) dolgozol,
# hanem a felhasználótól kéred ezeket be.
# Ahol szükséges, ne feledd konvertálni az értékeket!
# A megoldást egy consumption.py nevű file-ban kell beadnod.

fogyasztas_orszagut = 7
fogyasztas_varos = 9
ut_orszagut = 170
ut_varos = 35
benzin_ar = 350

fogy_oda = fogyasztas_orszagut * ut_orszagut + fogyasztas_varos * ut_orszagut
fogy_oda_vissza = 2 * fogy_oda
teljes_ar = fogy_oda_vissza * benzin_ar
print(f'Fogyasztás oda: {fogy_oda}')
print(f'Fogyasztás oda-vissza: {fogy_oda_vissza}')
print(f'Teljes út ára: {teljes_ar}')
