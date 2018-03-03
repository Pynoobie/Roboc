# -*-coding:utf-8 -*
# IMPORTATIONS

from classes.Jeu import *





# FONCTIONS

# Fonction principale #

def main():
	"""La fonction principale de notre programme."""
	jeu = Jeu()
	jeu.bienvenue()

	while not jeu.termine:
		jeu.continuer()

	jeu.aurevoir()





# PROGRAMME

if __name__ == "__main__":
	main()
