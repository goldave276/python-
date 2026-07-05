import json


class Livre:
    def __init__(self, nom, auteur, annee, maison_edition, disponible):
        self.nom = nom
        self.auteur = auteur
        self.annee = annee
        self.maison_edition = maison_edition
        self.disponible = disponible

    def to_dict(self):
        return {
            "nom": self.nom,
            "auteur": self.auteur,
            "annee": self.annee,
            "maison d'edition": self.maison_edition,
            "disponible": self.disponible,
        }

    @classmethod
    def from_dict(cls, data):
        maison_edition = data.get("maison_edition", data.get("maison d'edition", ""))
        disponible = data.get("disponible", True)

        if isinstance(disponible, str):
            disponible = disponible.lower() == "true"

        return cls(
            data.get("nom", ""),
            data.get("auteur", ""),
            int(data.get("annee", 0)),
            maison_edition,
            disponible,
        )

    def afficher(self):
        print(f"nom : {self.nom}")
        print(f"auteur : {self.auteur}")
        print(f"annee : {self.annee}")
        print(f"maison d'edition : {self.maison_edition}")
        print(f"disponible : {self.disponible}")

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print("\nLivre emprunte avec succes")
        else:
            print("\nLivre deja emprunte")

    def rendre(self):
        if not self.disponible:
            self.disponible = True
            print("\nLivre rendu avec succes")
        else:
            print("\nCe livre est deja disponible")


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self):
        nom = input("\nle nom de l'oeuvre : ")
        auteur = input("\nl'auteur de l'oeuvre : ")

        while True:
            try:
                annee = int(input("\nl'annee de publication : "))
                break
            except ValueError:
                print("\nVeuillez entrer une valeur juste")

        maison_edition = input("\nla maison d'edition : ")

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

        nouveau_livre = Livre(nom, auteur, annee, maison_edition, disponible)
        self.livres.append(nouveau_livre)

        print("\nLivre ajoute avec succes")

    def afficherTousLesLivres(self):
        if not self.livres:
            print("\nla bibliotheque est vide")
        else:
            print("\n===== Liste des livres =====")
            for livre in self.livres:
                livre.afficher()
                print("-" * 30)

    def rechercherLivre(self):
        rechercher = input("\nquel livre recherches tu ? ").strip().lower()

        for livre in self.livres:
            if rechercher == livre.nom.lower():
                print("\nlivre trouve")
                livre.afficher()
                break
        else:
            print("\nlivre introuvable")

    def supprimerLivre(self):
        supprimer = input("\nquel livre voulez vous supprimer ? ").strip().lower()

        if not self.livres:
            print("\nbibliotheque vide")
            return

        for livre in self.livres:
            if supprimer == livre.nom.lower():
                self.livres.remove(livre)
                print("\nlivre supprime avec succes")
                break
        else:
            print("\nlivre introuvable")

    def choisirLivre(self, action):
        nom = input(f"\nQuel livre voulez-vous {action} ? ").strip().lower()

        for livre in self.livres:
            if livre.nom.lower() == nom:
                return livre

        print("\nlivre introuvable")
        return None

    def sauvegarderLivre(self):
        with open("bibliotheque.json", "w", encoding="utf-8") as fichier:
            json.dump(
                [livre.to_dict() for livre in self.livres],
                fichier,
                indent=4,
                ensure_ascii=False,
            )

        print("\nlivre sauvegarde")

    def chargerLivre(self):
        try:
            with open("bibliotheque.json", "r", encoding="utf-8") as fichier:
                donnees = json.load(fichier)
                self.livres = [Livre.from_dict(livre) for livre in donnees]
                print("\nbibliotheque chargee")
                return self.livres
        except (FileNotFoundError, json.JSONDecodeError):
            print("\naucune sauvegarde trouvee")
            return []


def messageAccueil():
    print("\ngestionnaire de taches")
    print("\n1. Ajouter un livre")
    print("\n2. Afficher les livres")
    print("\n3. emprunter un livre")
    print("\n4. rendre un livre")
    print("\n5. Rechercher un livre")
    print("\n6. Supprimer un livre")
    print("\n7. Sauvegarder")
    print("\n8. Charger")
    print("\n9. Quitter")
    print("\n")


def choixOption():
    while True:
        try:
            choix = int(input("\nveuiller choisir une option : "))
            break
        except ValueError:
            print("\nVeuillez entrer une valeur juste")

    return choix


biblio = Bibliotheque()


def main():
    while True:
        messageAccueil()
        choix = choixOption()

        if choix == 1:
            biblio.ajouter_livre()
        elif choix == 2:
            biblio.afficherTousLesLivres()
        elif choix == 3:
            livre = biblio.choisirLivre("emprunter")
            if livre is not None:
                livre.emprunter()
        elif choix == 4:
            livre = biblio.choisirLivre("rendre")
            if livre is not None:
                livre.rendre()
        elif choix == 5:
            biblio.rechercherLivre()
        elif choix == 6:
            biblio.supprimerLivre()
        elif choix == 7:
            biblio.sauvegarderLivre()
        elif choix == 8:
            biblio.chargerLivre()
        elif choix == 9:
            break
        else:
            print("\nchoix invalide")


if __name__ == "__main__":
    main()
