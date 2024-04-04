'''
Code et commantaires par Vincent Tremblay
            21 mars 2024

  Autres informations utile sur le code
                ...
                ...
         fin des commentaires 
'''

# Import des libraries
# NA

# _________Classes_________ 

class Etudiant:

  def __init__(self, prenom, nom): # Initialisation (constructor), est appeler des la création d'un étudiant
    self.nom = nom
    self.prenom = prenom
    self.age = 35 # "hardcoder"
    
  #def __str__(self):						# redefinis le "string" renvoyer par l'objet
  #  return f"{self.prenom} {self.nom}({self.age})"		# redefinis le "string" renvoyer par l'objet

  def myfunc(self):			# fonction définis par "vous", affiche les valeurs ds différentes Variables
    print("Mon nom est " + self.prenom + " " + self.nom + ", ", self.age )
    
  def change(self, prenom, nom, age):	# fonction définis par "vous", permet de modifier les valeurs (sécuritaire)
    self.nom = nom
    self.prenom = prenom
    self.age = age

# _________Fin des Classes_________ 


# _________Création des Etudiants_________ 

Etu1 = Etudiant("John", "Tremblay") 	# Création de l'étudiant #1
Etu2 = Etudiant("Amély", "Simard")	# Création de l'étudiant #2

Etu3 = Etu2				# Copie de l'etudiant #2

# voir info sur deep and shallow copy en python pour plus d'information
# https://www.toppr.com/guides/python-guide/tutorials/python-operations/python-shallow-copy-and-deep-copy-with-examples/

# Definition des variables
# NA

# _________Fin de la création_________ 

''' -- utilisation des élements --'''
print("	Premier test :")	#affichage des Étudiants une premiere fois
Etu1.myfunc()     
Etu2.myfunc() 
Etu3.myfunc() 
print(Etu1)			# imprime l'objet Etudiant 1
print(Etu2) 			# imprime l'objet Etudiant 2
print(Etu3)			# imprime l'objet Etudiant 3 - (Identique à l'etudiant 2)

Etu3.prenom = "Boubacar" 	# Modification avec un acces direct a l'objet
Etu3.age = 25 			# Modification avec un acces direct a l'objet

print("	Deuxieme test :")	#affichage des Étudiants une deuxieme fois pour montrer la modification
Etu1.myfunc() 
Etu2.myfunc() 
Etu3.myfunc() 

Etu2.change("Claire", "Larouche", 28) # Modification via la fonction créé précedemment

print("	troisieme test :")
Etu1.myfunc() 
Etu2.myfunc() 
Etu3.myfunc() 



