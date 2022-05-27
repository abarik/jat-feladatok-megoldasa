class Elado:
    ID = 0

    def __init__(self, nev):
        self.nev = nev
        self.id = Elado.new_id()

    @classmethod
    def new_id(cls):
        cls.ID += 1
        return cls.ID
