#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:17:52 2020

@author: emmalestang
"""

import numpy as np
import pandas as pd
import csv
from math import *
import matplotlib.pyplot as plt



#On convertie le fichier csv en liste
def conv (): 
    donnees = pd.read_csv(open('/Users/emmalestang/Desktop/EIVP/Algorithme et programmation/EIVP_KM.csv'),sep=';')
    capteur=donnees["id"].tolist()
    noise=donnees["noise"].tolist()
    temp=donnees["temp"].tolist()
    humid=donnees["humidity"].tolist()
    lum=donnees["lum"].tolist()
    co2=donnees["co2"].tolist()
    date=(donnees["sent_at"].tolist())
    return(noise,temp,humid,lum,co2,date,capteur)

#Algorithme de tri permettant de detecter les anomalie dans les listes
def tri(l_n,l_t,l_h,l_l,l_c,l_date):
    l=len(l_date)
    for i in range(l-1) :
      for j in range(l-i-1)  :
        if l_date[j] > l_date[j+1]:
            l_date[j],l_date[j+1] = l_date[j+1],l_date[j]
            l_n[j],l_n[j+1] = l_n[j+1],l_n[j]
            l_t[j],l_t[j+1] = l_t[j+1],l_t[j]
            l_h[j],l_h[j+1] = l_h[j+1],l_h[j]
            l_l[j],l_l[j+1] = l_l[j+1],l_l[j]
            l_c[j],l_c[j+1] = l_c[j+1],l_c[j]
    return  (l_n,l_t,l_h,l_l,l_c,l_date) 

#On demande avec quelle donnée on veut travailler
def choixdonnée():
    choix=input('choix données: 0-noise,1-temperature,2-humidite,3-luminosite,4-co2 : ')
    return int(choix)

#On demande avec quel capteur on veut travailler
def choixcapteur():
    choixcapteur=input('choix du capteur : 1, 2, 3, 4, 5, 6 : ')
    return int(choixcapteur)

#Formation des listes en fonction du capteur et de la donnée
def listeparcapteur():
    L=[]
    d=choixdonnée()
    c=choixcapteur()
    for i in range(len(conv()[6])):
        if conv()[6][i]==c:
            L.append(conv()[d][i])
    return L

#Tracé des courbes demandées
def graph():
    Y=[]
    X=[]
    d=choixdonnée()
    c=choixcapteur()
    for i in range(len(conv()[6])):
        if conv()[6][i]==c:
            Y.append(conv()[d][i])
            X.append(conv()[5][i])
    plt.plot(X,Y)
    plt.show()
    
##############################################################################
##############################################################################

def minimum(listep):
    minimum = liste[0]
    for i in range(1,len(liste)):
        if minimum > liste[i]:
            minimum = liste[i]
    return minimum  

def maximum(liste):
    maximum = liste[0]
    for i in range(1,len(liste)):
        if maximum < liste[i]:
            maximum = liste[i]
    return maximum  

def moyenne(liste):
    l = len(liste)
    somme = 0
    for i in range(l):
        somme += liste[i]
    return float(somme/l)

def variance(liste):
    v = 0
    for i in range(len(liste)):
        v += (liste[i] - moyenne(liste))**2
    return v/len(liste)

def ecart_type(liste):  
    return sqrt(variance(liste))

def tri_croiss(liste):
    #algoithme bubble sort
    l=len(liste)
    for i in range(l-1) :
      for j in range(l-i-1)  :
        if liste[j] > liste[j+1]:
            liste[j],liste[j+1] = liste[j+1],liste[j]
            
    return  liste  

def mediane(liste):
    tri = tri_croiss(liste)
    l = len(tri)
    if l%2 == 0:
        mediane = moyenne([tri[l//2], tri[(l//2)-1]])
    else :
        mediane = tri[l//2]
    return mediane


def rosee():
    TR=[]
    l=len(conv()[1])
    for i in range(l-1):
        alpha=((17.27*(conv()[1])[i])/(237.7+(conv()[1])[i]))+log((conv()[2])[i]/100)
        TR.append((237.7*alpha)/(17.27-alpha))
    return TR

def humidex():
    H=[]
    l=len(conv()[1])
    for i in range(l-1):
        c=5417.7530*((1/273.16)-(1/(273.15+rosee()[i])))
        a=(conv()[1])[i]+0.5555*(6.11*(exp(c))-10)
        H.append(a)
    return H

def humidexbis(T,TR): #T:température TR: température de rosée
    c=5417.7530*((1/273.16)-(1/(273.15+TR)))
    return T+0.5555*(6.11*(exp(c))-10)

def indcorrelation (liste1, liste2):
    sigma = 0
    l=len(liste1)
    for i in range (l-1):
        sigma+=(liste1[i]-moyenne(liste1))*(liste2[i]-moyenne(liste2))*(1/l)
    id=sigma/(ecart_type(liste1)*ecart_type(liste2))
    return id

#################################################################################################

def comparaisonliste(liste1,liste2):
    l=len(liste1)
    L=[]
    C=[]
    for i in range(l):
        a=liste1[i]-liste2[i]
        L.append(a)
    for j in range(l):
        if L[j]>= 0.975*mediane(L) and L[j]<=(1.025)*mediane(L):
            C.append(L[j])
    return len(C)
        
















