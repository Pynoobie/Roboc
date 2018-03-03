# -*-coding:utf-8 -*
# IMPORTATIONS





# CLASSE

class Robot:
	nom = "robot"
	symbole = "x"

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "<Robot: {xRobot},{yRobot}>".format(xRobot=self.x, yRobot=self.y)
