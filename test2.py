# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:43:22 2024

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May  6 23:07:54 2024
@author: HP
"""

import unittest
from gestionTaches import ConnexionMySQL, creerCompte, seConnecter, Taches

class TestGestionTaches(unittest.TestCase):

    # Test de la classe ConnexionMySQL
    def test_connexion_mysql(self):
        connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
        self.assertIsNotNone(connexion.connect())

    # Test de la classe creerCompte
    def test_creer_compte(self):
        creerCompte("test_user", 0, "test@example.com", "testpassword", "Test", "User")
        connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
        cursor = connexion.connect().cursor()
        query = "SELECT * FROM utilisateur WHERE username = 'test_user'"
        cursor.execute(query)
        self.assertIsNotNone(cursor.fetchone())

    # Test de la classe seConnecter
    #def test_se_connecter(self):
    #    self.assertTrue(seConnecter("test_user", "testpassword"))

    # Test de la classe Taches
    #def test_taches(self):
        #self.assertIsInstance(Taches("test_user"), Taches)

if __name__ == '__main__':
    unittest.main()
