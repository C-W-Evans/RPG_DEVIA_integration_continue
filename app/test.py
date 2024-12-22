import unittest
from main import Personnage

class Tests(unittest.TestCase):

    # # Test initial

    def test_hp_equals_10(self):
        personnage = Personnage()
        self.assertEqual(personnage.hp(), 10)


    # # Tests pour feature recevoir_degats

    def test_attaquant_enleve_1hp(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_degats(attaquant)
        self.assertEqual(defenseur.hp(), 9)

    def test_attaquant_enleve_2hp(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_degats(attaquant)
        defenseur.recevoir_degats(attaquant)
        self.assertEqual(defenseur.hp(), 8)

if __name__ == "__main__":
    unittest.main()