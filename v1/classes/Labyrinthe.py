# -*-coding:utf-8 -*
# IMPORTATIONS

from classes.Robot import *
from classes.Obstacle import *
from classes.Mur import *
from classes.Porte import *
from classes.Sortie import *





# FONCTIONS

def creerLabyrintheDepuisContenuFichier(contenuFichier):
	x = 0
	y = 0
	robot = None
	obstacles = []

	symboles = {
		"o": Mur,
		".": Porte,
		"u": Sortie,
		"x": Robot
	}

	for caractere in contenuFichier:
		if caractere == "\n":
			x = 0
			y += 1
			continue
		elif caractere == " ":
			pass
		elif caractere.lower() in symboles:
			classe = symboles[caractere.lower()]
			objet = classe(x, y)
			if type(objet) is Robot:
				if robot is None:
					robot = objet
				else:
					raise ValueError("ERREUR - Vous essayez d'insérer un nouveau robot en (x={xRobotAInserer}, y={yRobotAInserer}) alors qu'il y en a déjà un en (x={xRobotDejaPresent}, y={yRobotDejaPresent}).".format(xRobotAInserer=x, yRobotAInserer=y, xRobotDejaPresent=robot.x, yRobotDejaPresent=robot.y))
			else:
				obstacles.append(objet)
		else:
			raise ValueError("ERREUR - Symbole inconnu en (x={xSymboleInconnu}, y={ySymboleInconnu}) : {symboleInconnu}".format(xSymboleInconnu=x, ySymboleInconnu=y, symboleInconnu=caractere))

		x += 1

	nombreColonnes = x
	nombreLignes = y+1

	labyrinthe = Labyrinthe(nombreColonnes, nombreLignes, robot, obstacles)
	return labyrinthe





# CLASSE

class Labyrinthe:
	def __init__(self, nombreColonnes, nombreLignes, robot, obstacles):
		self.grille = {}
		self.invisibles = []

		# Étape 1 : On vérifie les paramètres 'nombreColonnes' et 'nombreLignes' qui correspondent aux dimensions du labyrinthe
		if type(nombreColonnes) is int and nombreColonnes > 0:
			self.nombreColonnes = nombreColonnes
		else:
			raise ValueError("ERREUR - Vous essayez de créer un labyrinthe avec un nombre de colonnes incorrect.")

		if type(nombreLignes) is int and nombreLignes > 0:
			self.nombreLignes = nombreLignes
		else:
			raise ValueError("ERREUR - Vous essayez de créer un labyrinthe avec un nombre de lignes incorrect.")

		# Étape 2 : On vérifie que le paramètre 'robot' a reçu un objet de la classe Robot avec des coordonnées valides
		if type(robot) is Robot:
			if robot.x >= 0 and robot.x < self.nombreColonnes and robot.y >= 0 and robot.y < self.nombreLignes:
				self.robot = robot
				self.grille[(robot.x, robot.y)] = robot
			else:
				raise ValueError("ERREUR - Vous essayez d'insérer un Robot en (x={xRobotAInserer}, y={yRobotAInserer}), soit en dehors des limites de la grille (xMin=0, yMin=0, xMax={xMax}, yMax={yMax}).".format(xRobotAInserer=robot.x, yRobotAInserer=robot.y, xMax=self.nombreColonnes-1, yMax=self.nombreLignes-1))
		else:
			raise ValueError("ERREUR - Vous essayez de passer un objet qui n'est pas issu de la classe Robot au paramètre 'robot'.")

		# Étape 3 : On vérifie que le paramètre 'obstacles' a reçu une liste d'objets issus de classes héritées de la classe Obstacle avec des coordonnées valides et non occupées par un autre objet
		for obstacle in obstacles:
			if isinstance(obstacle, Obstacle):
				if obstacle.x >= 0 and obstacle.x < self.nombreColonnes and obstacle.y >= 0 and obstacle.y < self.nombreLignes:
					if (obstacle.x, obstacle.y) not in self.grille:
						self.grille[(obstacle.x, obstacle.y)] = obstacle
					else:
						raise ValueError("ERREUR - Vous essayez d'insérer un obstacle en (x={xObstacleAInserer}, y={yObstacleAInserer}), où se trouve déjà un autre objet ({nomObjetDejaPresent}).".format(xObstacleAInserer=obstacle.x, yObstacleAInserer=obstacle.y, nomObjetDejaPresent=self.grille[(obstacle.x, obstacle.y)].nom))
				else:
					raise ValueError("ERREUR - Vous essayez d'insérer un obstacle en (x={xObstacleAInserer}, y={yObstacleAInserer}), soit en dehors des limites de la grille (xMin=0, yMin=0, xMax={xMax}, yMax={yMax}).".format(xObstacleAInserer=obstacle.x, yObstacleAInserer=obstacle.y, xMax=self.nombreColonnes-1, yMax=self.nombreLignes-1))
			else:
				raise ValueError("ERREUR - Vous essayez de passer une liste d'objets qui ne sont pas tous issus de classes héritées de la classe Obstacle au paramètre 'obstacles'.")

	def afficher(self):
		representation = ""
		premiereLigne = True
		for y in range(self.nombreLignes):
			if not premiereLigne:
				representation += "\n"
			else:
				premiereLigne = False
			for x in range(self.nombreColonnes):
				if (x, y) in self.grille:
					representation += self.grille[(x, y)].symbole#.upper()
				else:
					representation += " "
		print(representation)

	def valider_deplacement(self, direction, nombrePas):
		robot = self.robot
		coords = [robot.x, robot.y]
		nombrePasRestants = nombrePas
		deplacementValide = True

		while nombrePasRestants > 0:
			if direction == "n":
				coords[1] -= 1
			elif direction == "s":
				coords[1] += 1
			elif direction == "o":
				coords[0] -= 1
			elif direction == "e":
				coords[0] += 1
			else:
				deplacementValide = False
				nombrePas = 0

			x, y = coords
			if x >= 0 and x < self.nombreColonnes and y >= 0 and y < self.nombreLignes:
				if (x, y) in self.grille and not self.grille[(x, y)].franchissable:
					deplacementValide = False
					nombrePas = 0
			else:
				deplacementValide = False
				nombrePas = 0

			nombrePasRestants -= 1

		return deplacementValide

	def actualiser_invisibles(self):
		for obstacle in list(self.invisibles):
			if (obstacle.x, obstacle.y) not in self.grille:
				self.grille[(obstacle.x, obstacle.y)] = obstacle
				self.invisibles.remove(obstacle)

	def deplacer_robot(self, partie, direction, nombrePas):
		deplacementValide = self.valider_deplacement(direction, nombrePas)

		if deplacementValide:
			robot = self.robot
			coords = [robot.x, robot.y]
			nombrePasRestants = nombrePas

			while nombrePasRestants > 0:
				if direction == "n":
					coords[1] -= 1
				elif direction == "s":
					coords[1] += 1
				elif direction == "o":
					coords[0] -= 1
				elif direction == "e":
					coords[0] += 1

				nombrePasRestants -= 1

			x, y = coords

			obstacle = self.grille.get((x, y))
			if obstacle is None or obstacle.franchissable:
				if obstacle:
					self.invisibles.append(obstacle)

				del self.grille[(robot.x, robot.y)]

				self.grille[(x, y)] = robot
				robot.x = x
				robot.y = y
				self.actualiser_invisibles()
				self.afficher()

				if obstacle:
					obstacle.arriver(partie)
		else:
			print("ERREUR - Déplacement invalide !")
