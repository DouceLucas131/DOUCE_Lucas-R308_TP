def ajouter_etudiant(d, nom, note) :    
    if not isinstance(note, (float, int)) :
       raise ValueError("La note doit être un nombre") #Renvoie une erreur si le type de note n'est pas float ou int

    if note < 0 : 
        raise ValueError("Note négatives impossible") #Renvoie une erreur si la note < 0
    
    if note > 20 : 
        raise ValueError("Note plus que 20 impossible") #Renvoie une erreur si la note excede 20

    d[nom] = note #Ajoute les nouvelles entrées au dictionnaire si il n'y a pas d'erreurs

def moyenne_classe(d) :
    if len(d) == 0 : 
        return "Le distionnaire est vide" #Erreur si le distionnaire est vide
    else : 
        return sum(d.values()) / len(d) #"sum(d.values()) / len(d) trouve la moyenne en divisant par le nombre d'étudiant"

def meilleur_etudiant(d) :
    meilleur_nom = 0
    meilleure_note = -1 #Car les notes sont entre 0 et 20
    
    for nom, note in d.items() : #Parcourt les éléments du dictionnaire
        if note > meilleure_note : 
            meilleur_nom = nom
            meilleure_note = note 
    
    return (meilleur_nom, meilleure_note)



d = {} #Le dictionnaire est vide au début
ajouter_etudiant(d, "Bob", 15.5)
ajouter_etudiant(d, "Max", 20)
ajouter_etudiant(d, "Alice", 10.7)


print(d)
print(moyenne_classe(d))
print(meilleur_etudiant(d))
    