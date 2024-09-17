# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import geopandas as gp
import numpy as np
import matplotlib.pyplot as plt

# Déclaration de données (entier (int))
print("Hello world!")

x = 2
print(x)
#Déclaration et casse (réel/float)
c= 0,1
d = 0.1

h=(1,5,9,-6,17,-8,31)
print(c)

#déclaration (chaine de caractere / (string ou str))
A= "Sylvain"
A
B='5'
print(A)
print("A")

f = 'salut'
f

g = """girafe"""
print(g)
#Opération math
1+1
a= 2+2
e=6*3 * a


5**10
a + B   #entier + str

#operation sur les chaines de caractere

ch1 = "Hola"
ch1

ch1 + " World"

ch1 * 3


#les separateur des les chaine de characteres
x = 59
nom = "Lilly"
print(nom, "a", x, "ans", sep="")


print(nom, "a", x, "ans", sep="-")


nom, age = "Sami", 80
print (f"{nom} a {age} ans.")

#Boolean
var2 = False
var7 =True
# afficher la classe
type(x)
type(g)
type(B)

#operateur "min" "max"

min(h)

min(d, x)

#conversion
str(e)

#Commenter / décommenter 
# =============================================================================
# 1+1
# 2+2
# 6*3
# =============================================================================

#Enregistrer le fichier python (file > save as > c/votre_repertoire/repertoire/TD1_python.py)

#afficher des guillemet

print("en dessous\ns\'affiche un texte\n \"entre guillemets\"")

#interaction avec input
input('écris moi')

age= input('Écris un chiffre : ')
print("Vous avez :", age, "ans")
input()

nom = input('quel est ton nom, humain?')
print('enchanté,', nom)

#  vérification/comparaison
(e == 72) and (d < 0.2)

X = 'NUL'
Y= 'nul'

print(X==Y)


#Créer des chiffre aléatoire

from random import *

from random import uniform
from random import randint

randint(0,99)

A1 = randint(0,99)

uniform(5.3,10.8)


#Lire le contenu dans un fichier texte 
aaaaa = open("aaaaa.txt", "r")
aaaaa

print(aaaaa)
a= aaaaa.readlines()

print(a)

a.close()  # Fermer le fichier après la lecture


#Ecrire du contenu dans un fichier texte 

aa = open("aaaaa.txt", "a", encoding='utf8')
aa.write('chien\n')
aa.close()  # Fermer le fichier après la lecture

# Réouvrir le fichier en mode lecture
aa = open("aaaaa.txt", "r", encoding='utf8')
ab = aa.readlines()
print(ab)
aa.close()  # Fermer le fichier après la lecture


#Générer un plot (graphique - linéaire)

# Importer les libraries utile
import matplotlib.pyplot as graphic

# échantillon de donnée (exemple pour réaliser le graphic)
x = [1, 2, 3, 4, 5]
y = [1, 8, 4, 16, 25]

# le code pour le graphic linéaire
graphic.plot(x, y)

# Add labels and a title
graphic.xlabel('Axe des x')
graphic.ylabel('Axe des y')
graphic.title('Voici un graphe linéaire simple')

# Display the plot
graphic.show()


# Maintenant au lieu d'un graphic linéaire afficher un graphi "Histogramme"
# Importer les libraries utile
import matplotlib.pyplot as plt
import numpy as np

# générer la donner aléatoire avec numpy
data = np.random.randn(1000)  # 1000 valeurs aléatoires avec une distribution normale

#  afficher l'histogramme
plt.hist(data, bins=30, edgecolor='black')

# habiller le graphic
plt.xlabel('naissance/décés')
plt.ylabel('Age')
plt.title('Mon titre : exemple lage au japon')

# Display the plot
plt.show()




