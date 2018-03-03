# -*-coding:utf-8 -*
# IMPORTATIONS





# CLASSE

class Partie:
	"""La classe Partie permet de simuler le fonctionnement d'une partie au cours du jeu."""

	def __init__(self, carteChoisie):
		"""Le constructeur de notre classe Partie.
		Il définit quelques attributs propres à la partie en cours."""
		self.carte = carteChoisie
		self.labyrinthe = carteChoisie.labyrinthe
		self.nombreCoups = 0
		self.gagnee = False
		self.terminee = False

	def continuer(self):
		commande, direction, nombrePas = self.saisirCommande()
		if commande != "q": # dans ce cas on sait qu'on a demandé un déplacement
			self.labyrinthe.deplacer_robot(self, direction, nombrePas)
			self.nombreCoups += 1

	def saisirCommande(self):
		commandesPossibles = ["q", "n", "s", "o", "e"]
		direction = ""
		nombrePas = 0
		messageErreur = "ERREUR - Vous devez saisir une commande reconnue.\nQ : sauvegarder et quitter\nN : 1 pas vers le Nord\nS : 1 pas vers le Sud\nO : 1 pas vers l'Ouest\nE : 1 pas vers l'Est\nExemple : N2 : 2 pas vers le Nord"
		commandeEnAttente = True

		while commandeEnAttente:
			commande = input("> ")
			commande = commande.lower()
			longueurCommande = len(commande)

			if longueurCommande == 0:
				print(messageErreur)
			elif longueurCommande == 1:
				if commande in commandesPossibles:
					if commande in "nsoe":
						direction = commande
						nombrePas = 1
					else:
						self.terminee = True
					commandeEnAttente = False
				else:
					print(messageErreur)
			else:
				if commande[0] in commandesPossibles:
					if commande[0] in "nsoe":
						direction = commande[0]
						try:
							nombrePas = int(commande[1:])
						except ValueError:
							print(messageErreur)
						else:
							commandeEnAttente = False
					else:
						print(messageErreur)
				else:
					print(messageErreur)

		return commande, direction, nombrePas
