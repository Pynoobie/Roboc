# -*-coding:utf-8 -*
# IMPORTATIONS





# CLASSE

class Obstacle:
	nom = "obstacle"
	symbole = ""
	franchissable = True

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "<{nomObstacle}: {xObstacle},{yObstacle}>".format(nomObstacle=self.nom.capitalize(), x=self.x, y=self.y)

	def arriver(self, partie):
		pass
