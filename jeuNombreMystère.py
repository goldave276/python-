
import random

def engager():
    print("\n veuillez choisir un niveau de difficultés")
    print("\nniveau 1 - entre 1 et 10")
    print("\nniveau2 - entre 1 et 100")
    print("\nniveau3 - entre 1 et 500")


    while True:
        try:
            ch = int(input("\n choisissez le niveau par son chiffre"))
            niveaux = {
                1:10,
                2:100,
                3:500
            }

            if ch in niveaux:
                return random.randint(1, niveaux[ch])

            print("\nChoisissez 1, 2 ou 3.")      
        except ValueError:
                print("\n veuiller entrer un entier valide")
        
    
    



def comparaison(nombreMystere,proposition):
    if nombreMystere < proposition:
        return "\nplus petit"
    elif nombreMystere > proposition:
        return "\n plus grand"
    else:
        return ""
    


def sauvegarderScore(score):
    with open("scores.txt", "a") as fichier:
        fichier.write(str(score) + "\n")




def chargerMeilleurScore():
    try:
        with open("scores.txt", "r") as fichier:
            scores = [int(ligne.strip()) for ligne in fichier]
            return max(scores) if scores else 0
    except FileNotFoundError:
        return 0
    
    
        
def jouerUnePartie(nombreMystere):
   
    score = 0 
    essai = 0
    print ("\n vous aurez 10 essais")
    while essai < 10:
       
        try:
            proposition = int(input("\nveuillez entrer votre nombre"))
        except ValueError:
            print("veuiller entrer un entier")
            continue

        message = comparaison(nombreMystere, proposition)
        print(message)
        
        essai += 1 
        if nombreMystere != proposition:
            print("\n il vous reste", 10 - essai) 
             

        if nombreMystere == proposition:  
            print("\n vous avez trové le nombre en", essai,"essaie,\n le nombre mystere etait", nombreMystere) 
            return 11 - essai
        
    else:
        print("\n vous avez perdu,\n le nombre mystere etait", nombreMystere)

    return 0




def demandeRejouer():
    while True: 
        print("O pour rejouer ou N pour arreter")

        choix = input("\n voulez vous encore jouer ?")

        if choix not in ("N","O"):
            print("\n la valeur est incorrecte")
            continue
        return choix
    


def main():
    bestScore = chargerMeilleurScore()

    while True:
        print("bienvenue dans le jeu de devinnette")
        nombreMystere = engager()
        score = jouerUnePartie(nombreMystere)
            

        choix = demandeRejouer()

        if choix == "N":
            if score > bestScore :
                bestScore = score 
                sauvegarderScore(bestScore)
                print(bestScore)
            break
        if choix == "O":
            if score > bestScore :
                bestScore = score
                sauvegarderScore(bestScore)
            score = 0 
        

        
main()
    




