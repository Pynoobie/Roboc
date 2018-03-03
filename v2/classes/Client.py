# -*-coding:utf-8 -*
# IMPORTATIONS

import socket
import time





# CLASSE

class Client:
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
				assert port >= self.portMin and port <= self.portMax
			except ValueError:
				print(messageErreur)
			except AssertionError:
				print(messageErreur)
			else:
				portEnAttente = False

		return port

	def demarrer(self):
		nombreTentativesRestantesConnexionServeur = 3
		connexionServeurReussie = False

		while not connexionServeurReussie and nombreTentativesRestantesConnexionServeur > 0:
			self.hote = self.choisirHote()
			self.port = self.choisirPort()
			try:
				self.connexionServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.connexionServeur.connect((self.hote, self.port))
			except Exception:
				nombreTentativesRestantesConnexionServeur -= 1
				if nombreTentativesRestantesConnexionServeur > 1:
					messageErreur = "ERREUR - Connexion du client sur le port {port} de l'hôte {hote} échouée... {nombreTentativesRestantesConnexionServeur} tentatives restantes...".format(port=self.port, hote=self.hote, nombreTentativesRestantesConnexionServeur=nombreTentativesRestantesConnexionServeur)
				else:
					messageErreur = "ERREUR - Connexion du client sur le port {port} de l'hôte {hote} échouée... {nombreTentativesRestantesConnexionServeur} tentative restante...".format(port=self.port, hote=self.hote, nombreTentativesRestantesConnexionServeur=nombreTentativesRestantesConnexionServeur)
				print(messageErreur)
			else:
				connexionServeurReussie = True

		if connexionServeurReussie:
			self.actif = True

	def ouvert(self):
		nomProgramme = "CLIENT"
		print("#"*(len(nomProgramme)+4))
		print("# {nomProgramme} #".format(nomProgramme=nomProgramme))
		print("#"*(len(nomProgramme)+4))
		print("Client connecté au serveur de jeu sur le port {port} de l'hôte {hote}...".format(port=self.port, hote=self.hote))

	def ferme(self):
		print("Client fermé...")

	def continuer(self):
		print("Client actif...")
		time.sleep(3)
