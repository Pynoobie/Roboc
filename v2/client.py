# -*-coding:utf-8 -*
# IMPORTATIONS

from classes.Client import *





# FONCTIONS

# Fonction principale #

def main():
	client = Client()

	client.demarrer()

	if client.actif:
		client.ouvert()

		while client.actif:
			client.continuer()

		client.ferme()





# PROGRAMME

if __name__ == "__main__":
	main()
