import random

def jouer():
    #Nombre entre 1 et 100
    r = random.randint(1, 100) 
    essai = 0
    max_essai = 10 

    while essai < max_essai:
        try:
            #On utilise try/except pour éviter le crash si on tape des lettres
            n = int(input("Donnez un nombre : "))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")
            continue #On relance la boucle sans compter d'essai
        
        essai += 1 #On compte l'essai ici

        if n > r: 
            print("Trop Grand")
        
        elif n < r:
            print("Trop Petit")

        else:
            print(f"C'est Gagné en {essai} essai(s) !")
            return #On quitte la fonction immédiatement car on a gagné
    
    #Si on sort de la boucle sans avoir fait de return, c'est qu'on a perdu
    print(f"C'est Perdu, le nombre secret était {r}")

def main():
    #Rejouabilité
    while True:
        jouer()
        rejouer = input("\nVoulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != 'o':
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    main()