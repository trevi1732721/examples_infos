'''
Code et commantaires par Vincent Tremblay
            21 mars 2024

  Autres informations utile sur le code
                ...
                ...
         fin des commentaires 
'''

# import des libraries
# NA

# Definition des variables
# NA

# _________Fonctions_________ 

#imprime un "hello world"
def helloWorld():
    print("\t Hello World")

# Imprime plusieurs "Hello World"
def helloWorlds(rep):        # rep represente le nb de repetition
    for i in range(rep): 
        print(f'\t Hello World #{i}')

# Imprime trois elements
def write(un, deux, trois):
    print("\t "+ un + deux + trois)

# Contient toutes les etapes du code
def main():    # Non necessaire

    print("Fonction #1") 
    helloWorld()         

    print("\nFonction #2")
    helloWorlds(5)

    print("\nFonction #3")
    write("Hello", " World","!")

#Debut du code
main()




