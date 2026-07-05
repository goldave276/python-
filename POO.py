class Livre:

    def __init__(self, nom, auteur,annee,maison_edition,disponible):
        self.nom = nom
        self.auteur = auteur
        self.annee = annee
        self.maison_edition = maison_edition
        self.disponible = disponible

livre1 = Livre("Python Crash Course","Eric Matthes", 2023, "No Starch Press",True)
livre2 = Livre( "Clean Code","Robert C. Martin",2008,"Prentice Hall",True)       

print(livre1.nom)
print(livre1.auteur)

print(livre2.nom)
print(livre2.auteur)