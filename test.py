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
from gestionTaches import ConnexionMySQL, marquerTache, modifierTache, supprimerTache, ajouterTache, creerCompte, seConnecter, Taches

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
        
    def test_ajouter_tache(self):
        self.assertTrue(ajouterTache("Ambro", "1234", "titreTest", "description", "0", "2024-05-05"))

    def test_marquer_tache(self):
        #la tache 10 est ajouter par Ambro, il peut donc le modifier 
        #l'Admin aussi a la main sur cette tache
        #l'utilisateur Ina ne peut parcontre pas modifier cette 
         
        self.assertTrue(marquerTache(10, "Ambro", 1234))
        self.assertTrue(marquerTache(10, "Admin", 1234))
        self.assertTrue(marquerTache(10, "Ina", 1234))
        self.assertTrue(marquerTache(10, "Sokwende", 1234))
        
    def test_modifier_tache(self):
        self.assertTrue(modifierTache(10, "Admin", "1234", "titre", "description"))
        self.assertTrue(modifierTache(10, "Ambro", "1234", "titre", "description"))
        self.assertTrue(modifierTache(10, "Ina", "1234", "titre", "description"))

    def test_supprimer_tache(self):
        #self.assertTrue(modifierTache(10, "Admin", "1234", "titre", "description"))
        self.assertTrue(supprimerTache(10, "Ambro", "1234"))
        self.assertTrue(supprimerTache(10, "Ina", "1234"))

if __name__ == '__main__':
    unittest.main()
