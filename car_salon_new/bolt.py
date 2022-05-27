from car_salon_new.eladas import Eladas
from car_salon_new.elado import Elado
from car_salon_new.kocsi import Kocsi
from car_salon_new.vevo import Vevo


class Bolt:
    def __init__(self):
        self.eladok = []
        self.kocsik = []
        self.vevok = []
        self.eladasok = []

        # n_eladas = Eladas(el, ve, ko)
        # self.eladas.append(n_eladas)

    def uj_kocsi(self):
        tipus = input('Kérem a kocsi típusát: ')
        szin = input('Kérem a kocsi színét: ')
        ev = input('Kérem a kocsi évjáratát: ')
        ar = int(input('Kérem a kocsi árát: '))
        u_k = Kocsi(tipus, szin, ev, ar)
        self.kocsik.append(u_k)

    def lista_kocsi(self):
        if len(self.kocsik) == 0:
            print('Nincs eladó kocsi!')
        else:
            for k in self.kocsik:
                print(f'(ID: {k.id} TÍPUS: {k.tipus} SZÍN: {k.szin} ÉVJÁRAT: {k.ev} ÁR: {k.ar})')

    def uj_elado(self):
        nev = input('Kérem az eladó nevét: ')
        u_e = Elado(nev)
        self.eladok.append(u_e)

    def lista_elado(self):
        if len(self.eladok) == 0:
            print('Nincs eladó!')
        else:
            for e in self.eladok:
                print(f'(ID: {e.id} NÉV: {e.nev})')

    def uj_vevo(self):
        nev = input('Kérem a vevő nevét: ')
        u_v = Vevo(nev)
        self.vevok.append(u_v)

    def lista_vevo(self):
        if len(self.vevok) == 0:
            print('Nincs vevő!')
        else:
            for v in self.vevok:
                print(f'(ID: {v.id} NÉV: {v.nev})')

    def uj_eladas(self):
        e_id = input('Kérem az eladó ID-jét: ')
        v_id = input('Kérem a vevő ID-jét: ')
        k_id = input('Kérem a kocsi ID-jét: ')
        el = Eladas(e_id, v_id, k_id)
        self.eladasok.append(el)

        i = 0
        for k in self.kocsik:
            if k.ID == int(k_id):
                break
            i += 1
        if i in range(len(self.kocsik)):
            del self.kocsik[i]

    def lista_eladas(self):
        if len(self.eladasok) == 0:
            print('Nem történt eladás!')
        else:
            for e in self.eladasok:
                print(f'(ELADÓ ID: {e.e_id} VEVŐ ID: {e.v_id} KOCSI ID: {e.k_id})')


