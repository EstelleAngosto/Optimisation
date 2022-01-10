# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:52:15 2022

@author: Utilisateur
"""

def fonction(x): 
    return(x**3-x-1) #Ecrire la fonction

def derive_fonction(x,dx):
    return (F_pos(x,dx)-F_neg(x,dx))/(2*dx) #Ecrire la fonction dérivée

def derive_seconde_fonction(x,dx):
    return (F_pos(x,dx)-2*fonction(x)+F_neg(x,dx))/((dx)**2) #Ecrire la dérivée seconde de la fonction

def F_neg(x,dx) : 
    return fonction(x-dx)
    
def F_pos(x,dx) : 
    return fonction(x+dx)

x = 1
i = 0
deltaX = 0.01
epsilon = 0.001
devfonc = derive_fonction(x,deltaX)
print(devfonc)
secdevfonc = derive_seconde_fonction(x,deltaX)

while abs(devfonc)>epsilon:
    print ("Etape "+str(i))
    print ("x : "+str(x))
    x = x - deltaX*(F_pos(x,deltaX)-F_neg(x,deltaX))/(2*(F_pos(x,deltaX)-2*fonction(x)+F_neg(x,deltaX)))
    devfonc = derive_fonction(x,deltaX)
    secdevfonc = derive_seconde_fonction(x,deltaX)
    i = i+1
    
print("Résultat final : "+str(x))