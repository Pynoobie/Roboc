# -*-coding:utf-8 -*
# IMPORTATIONS

from classes.Serveur import *





# FONCTIONS

# Fonction principale #

def main():
	serveur = Serveur()

	serveur.demarrer()

	if serveur.actif:
		serveur.ouvert()

		while serveur.actif:
			serveur.continuer()

		seveur.ferme()





# PROGRAMME

if __name__ == "__main__":
	main()
