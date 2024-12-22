import unittest
from main import Personnage

class Tests(unittest.TestCase):

    # # Test initial

    def test_hp_equals_10(self):
        personnage = Personnage()
        self.assertEqual(personnage.hp(), 10)

if __name__ == "__main__":
    unittest.main()