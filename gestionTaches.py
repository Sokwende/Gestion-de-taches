# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:24:02 2024

@author: HP
"""
#importation des modules necessaires
import mysql.connector
from datetime import datetime
from colorama import init, Fore, Back, Style
init()
#==============Application de gestion des taches==================# 

#classe de connexion à la base de données smartGestion
class ConnexionMySQL:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )

            if self.connection.is_connected():
                #print("Connexion à la base de données réussie.")
                return self.connection
            else:
                print("Erreur de connexion à la base de données.")
                return None
        except mysql.connector.Error as e:
            print("Erreur de connexion à la base de données:", e)
            return None
    
connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
connexion.connect()

class creerCompte:
    def __init__(self, username, typecompte, email, password, nom, prenom):
        self.username = username
        self.typeCompte = typecompte
        self.email = email
        self.password = password
        self.nom = nom
        self.prenom = prenom
        
        connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
        cursor = connexion.connect().cursor()
        query = "INSERT INTO utilisateur (username, typecompte, email, password, nom, prenom) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (username, typecompte, email, password, nom, prenom)
        cursor.execute(query, values)
        connexion.connection.commit()
        print("Compte créé avec succès!")

class seConnecter:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
        cursor = connexion.connect().cursor()
        query = "SELECT * FROM utilisateur where username = %s and password=%s"
        donnees = (username, password)
        cursor.execute(query, donnees)
        
        if cursor.fetchone():
            print("Connexion réussie !")
            print("#"+"===Bienvenue "+username+"==="+"#")
            Taches(username, password)
        else:
            print("Identifiants invalides. Connexion échouée.")
            cursor.close()
            

class ajouterTache:
    def __init__(self, username,password, titre, description, etat, dateDebut):
        self.username = username
        self.titre = titre
        self.description = description
        self.etat = etat
        self.dateDebut = dateDebut
        self.password = password
        connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
        cursor = connexion.connect().cursor()
        query = "SELECT * FROM utilisateur where username = %s and password = %s"
        donnees = (username, password)
        cursor.execute(query, donnees)
        idUser = cursor.fetchall()[0][0]
        
        cursor = connexion.connect().cursor()
        query = "INSERT INTO tache(iduser,titre, description, etat, datedebut) VALUES (%s,%s,%s,%s,%s)"
        donnees = (idUser,titre, description, etat, dateDebut)
        cursor.execute(query, donnees)

class marquerTache:
    def __init__(self, idTache, username, password):
        
        self.idTache = idTache
        self.username = username
        self.password = password
        
        connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
        cursor = connexion.connect().cursor()
        query = "SELECT * FROM utilisateur where username = %s and password = %s"
        donnees = (username, password)
        cursor.execute(query, donnees)
        idUser = cursor.fetchall()[0][0]
        
        cursor = connexion.connect().cursor()
        if username == 'Admin':
            query = "SELECT * FROM tache" 
        else:
            query = "SELECT * FROM tache WHERE iduser=%s"%(idUser)
        cursor.execute(query)
        taches = cursor.fetchall()
        idTaches = []
        for tache in taches:
            idTaches.append(tache[0])
        
        if idTache not in idTaches:
            print("Vous n'avez pas le droit de modifier cette tâche")
        else:
            cursor = connexion.connect().cursor()
            query = "UPDATE tache SET etat='1' where idtache=%s"%(idTache)
            cursor.execute(query)
            print(Fore.GREEN +"Tache %s terminée"%idTache)
            print(Style.RESET_ALL)
            
class modifierTache:
    def __init__(self, idTache, username,password,  titre, description):
        self.idTache = idTache
        self.username = username
        self.password = password
        self.titre = titre
        self.description = description
        
        connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
        cursor = connexion.connect().cursor()
        query = "SELECT * FROM utilisateur where username = %s and password = %s"
        donnees = (username, password)
        cursor.execute(query, donnees)
        idUser = cursor.fetchall()[0][0]
        
        cursor = connexion.connect().cursor()
        if username == 'Admin':
            query = "SELECT * FROM tache" 
        else:
            query = "SELECT * FROM tache WHERE iduser=%s"%(idUser)
        cursor.execute(query)
        taches = cursor.fetchall()
        idTaches = []
        for tache in taches:
            idTaches.append(tache[0])
        if idTache not in idTaches:
            print(Fore.RED +"Vous n'avez pas le droit de modifier cette tâche")
            print(Style.RESET_ALL)
        else:
            cursor = connexion.connect().cursor()
            query = "UPDATE tache SET titre=%s, description = %s where idtache=%s"
            donnees = [titre, description, idTache]
            cursor.execute(query, donnees)
            print(Fore.GREEN +"Tâche %s modifiée"%idTache)
            print(Style.RESET_ALL)
            
class supprimerTache:
    def __init__(self, idTache, username, password):
        
        self.idTache = idTache
        self.username = username
        self.password = password
        
        connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
        cursor = connexion.connect().cursor()
        query = "SELECT * FROM utilisateur where username = %s and password = %s"
        donnees = (username, password)
        cursor.execute(query, donnees)
        idUser = cursor.fetchall()[0][0]
        
        cursor = connexion.connect().cursor()
        if username == 'Admin':
            query = "SELECT * FROM tache" 
        else:
            query = "SELECT * FROM tache WHERE iduser=%s"%(idUser)
        cursor.execute(query)
        taches = cursor.fetchall()
        idTaches = []
        for tache in taches:
            idTaches.append(tache[0])
        if idTache not in idTaches:
            print(Fore.RED +"Vous n'avez pas le droit de modifier cette tâche")
            print(Style.RESET_ALL)
        else:
            cursor = connexion.connect().cursor()
            query = "DELETE FROM tache where idtache=%s"%(idTache)
            cursor.execute(query)
            print(Fore.GREEN +"Tache %s supprimée"%idTache)
            print(Style.RESET_ALL)
            
class Taches:
    def __init__(self, username, password):
        quitter = False
        while quitter == False:
            print(Fore.MAGENTA +"Que voulez-vous faire?")
            print(Style.RESET_ALL)
            print("1-Ajouter des taches\n2-Voir les taches\n3-Voir des statistiques\n4-Quitter")
            
            choix = int(input("Choisir: "))
            while choix !=1 and choix !=2 and choix !=3 and choix !=4:
                print("choix invalid")
                print("1-Ajouter des taches\n2-Voir les taches\n3-Voir des statistiques\n4-Quitter")
                choix = int(input("Choisir: "))
            if choix !=4:
                connexion = ConnexionMySQL("localhost", "root", "", "projetjenkins")
                cursor = connexion.connect().cursor()
                query = "SELECT * FROM utilisateur where username = %s and password = %s"
                donnees = (username, password)
                cursor.execute(query, donnees)
                idUser = cursor.fetchall()[0][0]
                #on a recuperer l'id de l'utilisateur pour la suite des operations
                
                if choix == 1:
                    print(Fore.MAGENTA +"Ajout d'une nouvelle tache")
                    print(Style.RESET_ALL)
                    titre = str(input("Entrez le titre de votre tache: "))
                    description = str(input("Decrivez votre tache: "))
                    etat = 0 #par defaut une tache est à l'etat non terminé
                    dateDebut = datetime.now()
                    ajouterTache(username, password, titre, description, etat, dateDebut)
                    print(Fore.GREEN +"Tache ajoutée")
                    print(Style.RESET_ALL)
                elif choix == 2:
                    
                    cursor = connexion.connect().cursor()
                    if username == 'Admin':
                        query = "SELECT * FROM tache" 
                    else:
                        query = "SELECT * FROM tache WHERE iduser=%s"%(idUser)
                    cursor.execute(query)
                    taches = cursor.fetchall()
                    idTaches = []
                    if username == 'Admin':
                        print(15*"="+"DEBUT"+15*"=")
                        for tache in taches:
                            idTaches.append(tache[0])
                            print(35*"_"+"\n")
                            etat = ""
                            if tache[4]==0:
                                etat = "Non terminée"
                            elif tache[4]==1:
                                etat = "terminée"
                            print("Id de la tâche: "+str(tache[0])+"\n"+
                                  "Id de l'utilisateur: "+str(tache[1])+"\n"+
                                  "Titre: "+str(tache[2])+"\n"+
                                  "Description: "+str(tache[3])+"\n"+
                                  "Etat: "+etat+"\n"+
                                  "Date de début: "+str(tache[5]))
                        print(15*"="+"FIN"+15*"=")
                    else:
                        print(15*"="+"DEBUT"+15*"=")
                        for tache in taches:
                            idTaches.append(tache[0])
                            print(35*"_"+"\n")
                            etat = ""
                            if tache[4]==0:
                                etat = "Non terminée"
                            elif tache[4]==1:
                                etat = "terminée"
                            print("Id de la tâche: "+str(tache[0])+"\n"+
                                  "Titre: "+str(tache[2])+"\n"+
                                  "Description: "+str(tache[3])+"\n"+
                                  "Etat: "+etat+"\n"+
                                  "Date de début: "+str(tache[5]))
                        print(15*"="+"FIN"+15*"=")
                    print(Fore.MAGENTA +"Voulez vous Modifier, supprimer ou marquer une tâche?")
                    print(Style.RESET_ALL)
                    print("1-oui\n"
                          "2-non\n")
                    choix = int(input("Choisir: "))
                    quitter2 = False
                    while quitter2 == False:
                        if choix == 1:
                            print("1-Marquer une tâche comme terminée\n"
                                  "2-Modifier une tâche\n"
                                  "3-Supprimer une tâche\n"
                                  "4-Quitter")
                            autrechoix = int(input("Choisir: "))
                            if autrechoix ==1:
                                idTache = int(input("Entrez l'id de la tache: "))
                                marquerTache(idTache, username, password)
                                
                            elif autrechoix == 2:
                                idTache = int(input("Entrez l'id de la tache: "))
                                titre = str(input("Entrez le nouveau titre: "))
                                description = str(input("Entrez la nouvelle description: "))
                                modifierTache(idTache, username, password, titre, description)
                                
                            elif autrechoix == 3:
                                idTache = int(input("Entrez l'id de la tache: "))
                                supprimerTache(idTache, username, password)
                                 
                            elif autrechoix == 4:
                                quitter2 = True
                            else:
                                print("erreur")
                        else:
                            quitter2 = True
                    
                elif choix == 3:
                    cursor = connexion.connect().cursor()
                    if username == 'Admin':
                        query = "call StatistiquesTachesParUtilisateur(%s)"%idUser
                    else:
                        query = "call StatistiquesTaches"
                    cursor.execute(query)
                    stat = cursor.fetchall()[0]
                    print(15*"-"+"DEBUT STATISTIQUES"+15*"-")
                    print("Nombre de tâches ajoutées: %s\n"
                          "Nombre de tâches terminées: %s\n"
                          "Pourcentage: %s%%\n"
                          "Nombre de tâches non terminées: %s\n"
                          "Pourcentage: %s%%"%(stat[0], stat[1], stat[2], stat[3],stat[4]))
                    print(15*"-"+"FIN STATISTIQUES"+15*"-")
            else:
                quitter = True

if __name__ == "__main__":
    #creation de compte
    print("#"+28*"="+"#")
    print("#"+"=====Gestion des tâches====="+"#")
    print("#"+28*"="+"#")
    
    print(Fore.MAGENTA +"Avez vous deja un compte?")
    print(Style.RESET_ALL)
    print("1: oui")
    print("2: non")
    
    estAuthentifie = int(input("Choisir une option: "))
    i=1
    while estAuthentifie !=1 and estAuthentifie!=2:
        if i==5:
            print("Essaie limite: Vous essayez 5 fois")
            break
        i+=1
        print("Choix invalid")
        estAuthentifie = int(input("Choisir une option: "))
    if estAuthentifie==1:
        print(Fore.MAGENTA +"Veuillez vous connecter")
        print(Style.RESET_ALL)
        username = str(input("Nom d'utilisateur: "))
        password = str(input("Mot de passe: "))
        
        seConnecter(username, password)
        
    elif estAuthentifie==2:
        print(Fore.MAGENTA +"Veuillez creer un compte")
        print(Style.RESET_ALL)
        nom = str(input("Entrez votre nom: "))
        prenom = str(input("Entrez votre prenom: "))
        email = str(input("Entrez votre adresse mail: "))
        username = str(input("Entrez un nom d'utilisateur: "))
        password = str(input("Entrez un mot de passe: "))
        password2 = str(input("Confirmez le mot de passe: "))
        if password == password2:
            creerCompte(username,0,email,password,nom,prenom)
            print(Fore.MAGENTA +"Veuillez vous connecter")
            print(Style.RESET_ALL)
            username = str(input("Nom d'utilisateur: "))
            password = str(input("Mot de passe: "))
            
            seConnecter(username, password)
        else:
            print("erreur: les mot de passe ne correspondent pas")
    
