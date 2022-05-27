class Eladas:
    ID = 0

    def __init__(self, el, ve, ko):
        self.e_id = el
        self.v_id = ve
        self.k_id = ko
        self.id = Eladas.new_id()

    @classmethod
    def new_id(cls):
        cls.ID += 1
        return cls.ID