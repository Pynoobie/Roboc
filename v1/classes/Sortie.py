# -*-coding:utf-8 -*
# IMPORTATIONS

from classes.Obstacle import *





# CLASSE

class Sortie(Obstacle):
	nom = "sortie"
	symbole = "U"

	def arriver(self, partie):
		partie.gagnee = True
		partie.terminee = True
