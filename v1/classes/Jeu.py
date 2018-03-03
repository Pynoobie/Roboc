# -*-coding:utf-8 -*
# IMPORTATIONS

import pickle
from classes.Carte import *
from classes.Partie import *
from sauvegardes import *





# CLASSE

class Jeu:
	"""La classe Jeu permet de disposer d'un objet afin de faciliter le déroulement du jeu."""

	def __init__(self):
		"""Le constructeur de notre classe Jeu.
		Il définit quelques attributs propres au jeu avec des valeurs par défaut."""
		self.nom = "LE JEU DU LABYRINTHE"
		self.cartes = []
		self.termine = False

	def initialiser(self):
		self.cartes = chargerCartes()

	def bienvenue(self):
		print("#"*(len(self.nom)+4))
		print("# {nomJeu} #".format(nomJeu=self.nom))
		print("#"*(len(self.nom)+4))
		print("Bienvenue dans le jeu du labyrinthe ! Vous pensez pouvoir en sortir ? C'est ce qu'on va voir !")

	def aurevoir(self):
		print("Au revoir !")

	def continuer(self):
		# Étape 1 : On vérifie si il y a une partie sauvegardée qui n'a pas été finie et on propose au joueur de la poursuivre
		partie = None
		partieSauvegardee = self.chargerPartieSauvegardee()

		# Si on a récupéré un objet de la classe Partie, on demande au joueur s'il veut la poursuivre
		if partieSauvegardee is not None:
			continuerPartieSauvegardee = self.continuerPartieSauvegardee()
			if continuerPartieSauvegardee:
				partie = partieSauvegardee
				partie.terminee = False

		# Étape 2 : Si on a rien récupéré ou qu'on ne souhaite pas poursuivre la partie sauvegardee, on charge les cartes depuis les fichiers .txt du dossier "cartes"
		if partie is None:
			self.initialiser()

			# Étape 3 : On demande au joueur de choisir une carte parmi les cartes disponibles et on crée la partie à partir de cette carte
			afficherCartes(self.cartes)
			carteChoisie = choisirCarte(self.cartes)
			confirmerCarteChoisie(carteChoisie)

			partie = Partie(carteChoisie)

		# Étape 4 : On démarre une nouvelle partie sur la carte choisie, qui se poursuit tant qu'elle n'est pas gagnée
		# ou qu'on a pas saisi la commande pour quitter la partie et le jeu
		partie.labyrinthe.afficher()

		while not partie.terminee:
			partie.continuer()

		# Étape 5 : La partie est terminée, soit elle a été gagnée soit elle a été interrompue.
		if partie.gagnee:
			if partie.nombreCoups == 1:
				print("Bravo ! Vous avez trouvé la sortie en 1 coup !")
			else:
				print("Bravo ! Vous avez trouvé la sortie en {nombreCoups} coups !".format(nombreCoups=partie.nombreCoups))

			# Si on a gagné la partie sauvegardée on peut vider le fichier qui la contient, ainsi au tour de boucle suivant partieSauvegardee vaudra None
			if partie is partieSauvegardee:
				self.supprimerPartieSauvegardee()
			self.rejouer()
		else:
			self.sauvegarderPartie(partie)
			self.termine = True

	def rejouer(self):
		oui = ['o', 'oui']
		non = ['n', 'non']
		rejouerEnAttente = True
		while rejouerEnAttente:
			rejouer = input("Voulez-vous rejouer (o/n) ? ")
			rejouer = rejouer.lower()
			if rejouer in oui or rejouer in non:
				rejouerEnAttente = False
			else:
				print("ERREUR - Vous devez répondre par oui ou par non.")
		if rejouer in non:
			self.termine = True

	def sauvegarderPartie(self, partie):
		with open("sauvegardes/sauvegarde", "wb") as fichierSauvegarde:
			monPickler = pickle.Pickler(fichierSauvegarde)
			monPickler.dump(partie)

	def chargerPartieSauvegardee(self):
		try:
			with open("sauvegardes/sauvegarde", "rb") as fichierSauvegarde:
				monUnpickler = pickle.Unpickler(fichierSauvegarde)
				partieSauvegardee = monUnpickler.load()
		except Exception:
			partieSauvegardee = None
		return partieSauvegardee

	def continuerPartieSauvegardee(self):
		oui = ['o', 'oui']
		non = ['n', 'non']
		continuerPartieSauvegardeeEnAttente = True

		while continuerPartieSauvegardeeEnAttente:
			continuerPartieSauvegardee = input("Voulez vous continuer la dernière partie sauvegardée (o/n) ? ")
			continuerPartieSauvegardee = continuerPartieSauvegardee.lower()
			if continuerPartieSauvegardee in oui or continuerPartieSauvegardee in non:
				continuerPartieSauvegardeeEnAttente = False
			else:
				print("ERREUR - Vous devez répondre par oui ou par non.")

		if continuerPartieSauvegardee in oui:
			return True
		else:
			return False

	def supprimerPartieSauvegardee(self):
		try:
			with open("sauvegardes/sauvegarde", "w") as fichierSauvegarde:
				fichierSauvegarde.write("")
		except Exception:
			print("ERREUR - Le script n'a pas réussi à supprimer le fichier contenant la partie sauvegardée.")
