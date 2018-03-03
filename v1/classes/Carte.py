# -*-coding:utf-8 -*
# IMPORTATIONS

import os
from classes.Labyrinthe import *





# FONCTIONS

def chargerCartes():
	cartes = []
	nomsFichiers = os.listdir("cartes")
	for nomFichier in nomsFichiers:
		if nomFichier.endswith(".txt"):
			cheminFichier = os.path.join("cartes", nomFichier)
			with open(cheminFichier, "r") as fichierCarte:
				contenuFichier = fichierCarte.read()
				carte = Carte(nomFichier, contenuFichier)
				cartes.append(carte)
	return cartes

def afficherCartes(cartes):
	print("Cartes disponibles :")
	for indiceCarte, carte in enumerate(cartes):
		print("{numeroCarte} - {nomCarte}".format(numeroCarte=indiceCarte+1, nomCarte=carte.nom))

def choisirCarte(cartes):
	numerosCartes = [indiceCarte+1 for indiceCarte, carte in enumerate(cartes)]
	numeroCarteEnAttente = True

	while numeroCarteEnAttente:
		numeroCarte = input("Saisissez le numéro de la carte dont vous souhaitez vous munir : ")
		try:
			numeroCarte = int(numeroCarte)
			assert numeroCarte in numerosCartes
		except ValueError:
			print("ERREUR - Vous devez saisir un nombre.")
		except AssertionError:
			print("ERREUR - Vous devez saisir un nombre correspondant à une carte disponible.")
		else:
			numeroCarteEnAttente = False

	return cartes[numeroCarte-1]

def confirmerCarteChoisie(carteChoisie):
	print("Vous vous munissez de la carte : {nomCarteChoisie}".format(nomCarteChoisie=carteChoisie.nom))





# CLASSE

class Carte:
	def __init__(self, nomFichier, contenuFichier):
		self.nom = nomFichier[:-4]
		self.labyrinthe = creerLabyrintheDepuisContenuFichier(contenuFichier)

	def __repr__(self):
		return "<Carte: {nomCarte}>".format(nomCarte=self.nom)
