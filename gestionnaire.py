
import json


bibliotheque = []


def messageAccueil(): 
    print("\ngestionnaire de taches ")
    print("\n1. Ajouter un livre")
    print("\n2. Afficher les livres")
    print("\n3. Rechercher un livre")
    print("\n4. Supprimer un livre  ")
    print("\n5. Sauvegarder")
    print("\n6. Charger")
    print("\n7. Quitter")
    print("\n")



def choixOption():
    while True:
        try:
            choix = int(input("\nveuiller choisir une option"))
            break
        except  ValueError:
            print("\nVeuiller entrer une valeur juste ")

    return choix



def ajouterUnLivre():

    while True:
        try:
          annee = int(input("\nl'annee de publication: "))
          break  
        except  ValueError:
            print("\nVeuiller entrer une valeur juste ")

    while True:
        disponible = input("Disponible (True/False) : ").lower()

        if disponible == "true":
         disponible = True
         break
        elif disponible == "false":
            disponible = False
            break
        else:
            print("Entrez True ou False.")



    livre = {
    "nom": input("\nle nom de l'oeuvre: "),
    "auteur": input("\nle nom de l'auteur: "),
    "annee": annee,
    "maison d'edition": input("\n la maison d'edition"),
    "disponible": disponible
    }

    bibliotheque.append(livre)

    print("`\nlivre ajoute avec succes")

    return livre

def afficherLeLivre(livre):
    print("\nlivre: ")
    print("\n nom : ", livre["nom"])
    print("\nauteur :", livre["auteur"])
    print("\nannee:", livre["annee"])
    print("\nmaison d'edition :", livre["maison d'edition"])
    print("\n disponible : ", livre["disponible"])

def afficherTousLesLivres():
    if len(bibliotheque) == 0:
        print("\nBibliotheque vide")
    else:
        for livre in bibliotheque:
            afficherLeLivre(livre)



def rechercherLivre():
    rechercher = input("\nquel livre refcherches tu ?")
    for livre in bibliotheque:
        if livre["nom"].lower() == rechercher.lower():
            print("\nLivre trouvé")
            afficherLeLivre(livre)
            break 
    else:
        print("\nLivre introuvable")



def supprimerLivre():
    supprimer = input("\n quel livre voulez vous supprimer")

    if not bibliotheque:
        print("\n bibliotheque vide")
        return
        

    for livre in bibliotheque:
        if livre["nom"].lower() ==  supprimer.lower():
            print("\n Livre trouve")
            bibliotheque.remove(livre) 
            print("\n livre supprime")
            break
    else:
         print("\nle livre n'exsite pas")


def sauvegarderLivre():
    with open("biblioteque.json", "w", encoding= "utf-8") as fichier:
        json.dump(bibliotheque, fichier, indent=4)

    print("\nlivre sauvegarder")

def chargerLivre():
    try:
       with open("biblioteque.json", "r", encoding= "utf-8") as fichier:
        bibliotheque = json.load(fichier)
        print("\nBibliotheque chargé")
        return bibliotheque
    except (FileNotFoundError, json.JSONDecodeError):
       return []
       
    


def main():

    global bibliotheque
    while True:
        messageAccueil()
        choix = choixOption()
        if choix == 1:
            ajouterUnLivre()
        elif choix == 2:
            afficherTousLesLivres()
        elif choix == 3:
            rechercherLivre()
        elif choix ==  4:
            supprimerLivre()
        elif choix == 5:
            sauvegarderLivre()
        elif choix == 6:
           bibliotheque = chargerLivre()
        elif choix == 7:
          break
        else:
            print("\nchoix invalide")
    

main()  
