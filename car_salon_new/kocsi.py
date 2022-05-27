class Kocsi:
    ID = 0

    def __init__(self, tipus, szin, ev, ar):
        self.tipus = tipus
        self.szin = szin
        self.ev = ev
        self.ar = ar
        self.id = Kocsi.new_id()

    @classmethod
    def new_id(cls):
        cls.ID += 1
        return cls.ID
