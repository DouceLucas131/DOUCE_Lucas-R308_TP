import random

def charger_mots():
    #Charge une liste de mots
    liste_mots = ["python", "algorithme", "ordinateur", "reseau", "programmation"]
    return liste_mots

def choisir_mot(liste):
    #Choisit un mot au hasard et le met en MAJUSCULES
    mot_aleatoire = random.choice(liste)
    return mot_aleatoire.upper()

def construire_masque(mot):
    #Construit un masque de '_' de la même longueur que le mot
    return ['_'] * len(mot)

