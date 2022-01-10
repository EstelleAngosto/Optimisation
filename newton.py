# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 21:54:22 2022

@author: Utilisateur
"""

def fonction(x): 
    return(x**3-x-1) #Ecrire la fonction

def derive_fonction(x):
    return(3*x**2-1) #Ecrire la fonction dérivée

def derive_seconde_fonction(x):
    return(6*x) #Ecrire la dérivée seconde de la fonction

x = 1
i = 0
epsilon = 0.0001
devfonc = derive_fonction(x)
secdevfonc = derive_seconde_fonction(x)

while abs(devfonc)>epsilon:
    print ("Etape "+str(i))
    print ("x : "+str(x))
    x = x - devfonc/secdevfonc
    devfonc = derive_fonction(x)
    secdevfonc = derive_seconde_fonction(x)
    i = i+1
    
print("Résultat final : "+str(x))