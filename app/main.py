class Personnage:
    def __init__(self):
        self.__hp = 10

    def hp(self):
        return self.__hp
    
    def recevoir_degats(self, attaquantS):
        self.__hp -= 1

    def est_mort(self):
        return self.__hp <= 0
    
    def recevoir_soins(self, soins):
        self.__hp = min(self.__hp + soins, 10)