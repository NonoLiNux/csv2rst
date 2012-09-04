#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Nom du module :        csv2rst
# But : ce script permet de transformer un csv en un tableau formaté en reStucturedText (donc lisible dans un éditeur de texte).
#
# Utilisation : python csv2rst.py fichier.csv fichier.txt
#
# Auteur:      Noémie Lehuby
#
# Created:     03/09/2012
# Copyright:   (c) Noémie Lehuby <noemie.lehuby@gmail.com> - 2012
# Licence:     Faites-en bon usage ;)
#-------------------------------------------------------------------------------

import sys
import csv

############ lecture du fichier source ##############
nom_fichier = sys.argv[1]
fichier = open(nom_fichier, "rb")
lignes = []

try:
    reader = csv.reader(fichier)
    for row in reader:
        lignes.append(row)
finally:
    fichier.close()



############ analyse des colonnes ##############
nb_colonnes = len(lignes[1])

taille_colonne = []
for i in range(nb_colonnes):
    colonne = []
    for ligne in lignes:
        colonne.append ( ligne[i] )
    taille_colonne.append(len(max(colonne, key=len)))



############ écriture du fichier de sortie ##############
motif_interligne ="+"
for i in taille_colonne:
    motif_interligne += "-" * (i+2)
    motif_interligne+= "+"

sortie = open(sys.argv[2], "w") 
#TODO : si pas de deuxième argument, donner un nom par défaut

for ligne in lignes:
    sortie.write( motif_interligne+"\n"+"|")
    for i in range(nb_colonnes):
        sortie.write( " "+ ligne[i] +" "*(taille_colonne[i]-len(ligne[i])) + " |")
        if (i == nb_colonnes - 1) :
            sortie.write("\n")
sortie.write(motif_interligne)
sortie.close()

