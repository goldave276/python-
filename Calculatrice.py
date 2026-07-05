
#Version ameliorée du code avec les tuples, listes, dictionnaires et fonctions
def addition(a,b):
    resultat = a + b 
    return resultat 

def soustraction(a,b):
    resultat = a - b
    return resultat 

def multiplication(a,b):
    resultat = a * b
    return resultat 

def division(a,b):
    if(b == 0):
        print("division impossible")
        return None
    elif(b not in (0,1)):
        resultat = a / b
    else: resultat = a
    
    return resultat 

#dictionnaire
operation = {
    "+": addition,
    "-": soustraction,
    "*": multiplication,
    "/": division
}

# liste (historique)

historique = []

while True:
    print("\n+ - * /")
    op = input("operation (ou q pour quitter)")

    if op == "q":
        break

    if op not in operation:
        print("operation inconnue")
        continue
    print("Veeuillez entrer deux valeurs")
    nbr1 = float(input("le nombre1 svp"))
    nbr2 = float(input("le nombre2 svp"))

    resultat = operation[op](nbr1, nbr2)

    #tuple
    calcul = (nbr1, op, nbr2, resultat)

    #historique
    historique.append(calcul)

    print("resultat:", resultat)


#affichage de l'historique 
print("\n historique")
for calc in historique:
    print(calc)






# premiere version du code 
# print( "votre calculatrice")
# print("Veeuillez entrer deux valeurs")
# nbr1 = float(input("le nombre1 svp"))
# nbr2 = float(input("le nombre2 svp"))


# print("choisir l'opération")
# print("1 - l'addition")
# print("2 - la soustraction")
# print("3 - la multiplication")
# print("4 - la division ")

# choix = int(input("veuillez prendre une decison "))

# if (choix == 1):
#     print("resultat :", addition(nbr1, nbr2))
# elif(choix == 2):
#     print("resultat :", soustraction(nbr1, nbr2))
# elif(choix == 3):
#     print("resultat :", multiplication(nbr1, nbr2))
# elif(choix == 4):
#     print("resultat :", division(nbr1, nbr2))
# else : print("choix invalide")