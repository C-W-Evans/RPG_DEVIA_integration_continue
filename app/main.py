class Personnage:
    def __init__(self):
        self.__hp = 10

    def hp(self):
        return self.__hp

    def recevoir_degats(self, attaquant):
        self.__hp = self.__hp - 1

    def est_mort(self):
        return self.__hp == 0