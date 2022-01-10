# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:39:31 2022

@author: Utilisateur
"""

def fonction(x): 
    return(x*(x-1.5)) #Ecrire la fonction

x1 = 0.0
f1 = fonction(x1)
sigma = 0.05
x2 = x1-sigma
f2 = fonction(x2)
n = 1
i = 1

if f2 > f1 :
    x2 = x1+sigma
    f2 = fonction(x2)
    while f1>=f2 : 
        i = i+1
        x1 = x2
        x2 = x1+sigma
        f1 = fonction(x1)
        f2 = fonction(x2)
        print("Etape "+str(i))
        print (str(x1)+" "+str(f1)+" "+str(x2)+" "+str(f2))
    print("La solution est entre "+str(x1)+" et "+str(x2)+".")

elif f2 < f1 :
    while f1>=f2 : 
        i = i+1
        x1 = x2
        x2 = x1-sigma
        f1 = fonction(x1)
        f2 = fonction(x2)
        print("Etape "+str(i))
        print (str(x1)+" "+str(f1)+" "+str(x2)+" "+str(f2))
    print("La solution est entre "+str(x1)+" et "+str(x2)+".")
    
elif f2 == f1 : 
    print("La solution est entre "+str(x1)+" et "+str(x2)+".")  