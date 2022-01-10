# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:14:33 2021

@author: Utilisateur
"""
import numpy as np

def col_piv (lp) :
    neg = False
    n = np.size(lp)
    
    for i in range(n):
        if lp[i]<0:
            neg = True
    
    if neg :
        col_neg = 0
        for j in range(n):
            if lp[j]<0:
               if lp[j]<lp[col_neg]:
                   col_neg = j
        return col_neg
    else:
        return -1

def lin_piv (lp,line,col,colp) : 
    coefs = []
    linp = 0
    
    for i in range(1,line):
        coefs.append(lp[i,col-1]/lp[i,colp])
        
    for j in range(len(coefs)) :
        if coefs[j] < coefs[linp]:
            linp = j
    
    return linp+1

def calcul(lp,line,col,linp,colp):
    pivot = lp[linp,colp]

    new_matrice = np.empty((line,col))
    
    for i in range(col):
        new_matrice[linp,i] = lp[linp,i]/pivot
    
    for j in range(line):
        for k in range(col):
            if j!=linp : 
                new_matrice[j,k] = lp[j,k]-((lp[j,colp]/pivot)*new_matrice[linp,k])

    return new_matrice            
    


#%% Demander les infos à l'utilisateur

# print("Bienvenue dans ce programme de calcul de simplex !")
    
# type_prob = input("Est-ce un problème de maximisation ou de minimisation ? max ou min")
    
# nb_var = input("Saisissez le nombre de variable du problème :")



#%% Algo des simplex

def simplex(simplex):

    

    line, column = np.shape(simplex)

    col_pivot = col_piv(simplex[0,:])
    print("Col pivot 1")

    while col_pivot != -1:
        lin_pivot = lin_piv(simplex,line,column,col_pivot)
        print("line pivot")
        simplex = calcul(simplex, line, column, lin_pivot, col_pivot)
        print("calcul des lignes")
        col_pivot = col_piv(simplex[0,:])
        print("Nouveau tour")

    return(simplex)

def BigM():
    bigm = np.array((10,10))
    return bigm


matrice = np.array([[-3,-4,0,0,1,0],
                    [1,1,1,0,0,4],
                    [2,1,0,1,0,5]])

matrice_simplex = simplex(matrice)
print(matrice_simplex)

c = 'a'

print("Veuillez saisir votre problème d'optimisation dans le fichier problem_simplex.txt")
print("Appuyez sur la touche o quand vous êtes prêt :")

while c!='o':
    c=input()
    
f = open("problem_simplex.txt","r")
ligne = f.readline()

while ligne[0] == '*':
    
    ligne = f.readline()
    
if ligne == "Max":
    ligne = f.readline()
    while ligne[0] != '*':
        print(ligne)







