import random

#Fonctions de la Partie C
def charger_mots():
    return ["python", "algorithme", "ordinateur", "reseau"]

def choisir_mot(liste):
    return random.choice(liste).upper()

def construire_masque(mot):
    return ['_'] * len(mot)

#Fonction principale du jeu
def jouer_pendu():
    mot_secret = choisir_mot(charger_mots())
    masque = construire_masque(mot_secret)
    erreurs = 0
    lettres_proposees = []

    print("Bienvenue au jeu du Pendu !")

    #Tant qu'on a moins de 7 erreurs et qu'il reste des '_' dans le masque
    while erreurs < 7 and '_' in masque:
        print("\nMot à deviner :", " ".join(masque))
        print(f"Erreurs : {erreurs}/7")
        print(f"Lettres déjà proposées : {lettres_proposees}")

        #Demande une lettre
        lettre = input("Proposez une lettre : ").upper()

        #Vérification qu'il y a qu'une seule lettre 
        if len(lettre) != 1 or not lettre.isalpha():
            print("Erreur : Veuillez entrer une seule lettre valide.")
            continue

        # Vérifie si la lettre a déjà été proposée
        if lettre in lettres_proposees:
            print("Vous avez déjà proposé cette lettre !")
            continue

        #Ajoute la lettre à la liste des propositions
        lettres_proposees.append(lettre)

        #Vérifie si la lettre est dans le mot
        if lettre in mot_secret:
            print("Bonne lettre !")
            #Révéle la lettre dans le masque
            for i in range(len(mot_secret)):
                if mot_secret[i] == lettre:
                    masque[i] = lettre
        else:
            print("Raté, cette lettre n'est pas dans le mot.")
            erreurs += 1

    #Fin de la boucle
    if '_' not in masque:
        print(f" GAGNÉ ! Le mot était bien : {mot_secret}")
        return True #On renvoie True pour dire que le joueur a gagné
    else:
        print(f" PERDU ! Le mot était : {mot_secret}")
        return False #On renvoie False pour la défaite

#Lancement du jeu
if __name__ == "__main__":
    jouer_pendu()