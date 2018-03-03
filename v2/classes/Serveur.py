# -*-coding:utf-8 -*
# IMPORTATIONS

import socket
import select
import time





# CLASSE

class Serveur:
	def __init__(self):
		self.hote = ""
		self.portMin = 1024
		self.portMax = 65535
		self.port = 0
		self.connexionServeur = None
		self.actif = False

	def choisirHote(self):
		hote = input("Hôte : ")
		if len(hote) == 0:
			hote = "localhost"
		return hote

	def choisirPort(self):
		messageErreur = "ERREUR - Vous devez saisir un numéro de port compris entre {portMin} et {portMax}".format(portMin=self.portMin, portMax=self.portMax)
		portEnAttente = True

		while portEnAttente:
			port = input("Port (entre {portMin} et {portMax}) : ".format(portMin=self.portMin, portMax=self.portMax))
			try:
				port = int(port)
				assert 
			except ValueError:
				print(messageErreur)
			except AssertionError:
				print(messageErreur)
			else:
				portEnAttente = False

		return port

	def demarrer(self):
		self.hote = self.choisirHote()

	def ouvert(self):
		nomProgramme = "SERVEUR"
		print("#"*(len(nomProgramme)+4))
		print("# {nomProgramme} #".format(nomProgramme=nomProgramme))
		print("#"*(len(nomProgramme)+4))
		print("Serveur ouvert sur le port {port} de l'hôte {hote}...".format(port=self.port, hote=self.hote))

	def ferme(self):
		print("Serveur fermé...")

	def continuer(self):
		print("Serveur actif...")
		time.sleep(3)
