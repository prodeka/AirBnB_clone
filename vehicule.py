class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_infos(self):
        print(f"{self.marque} {self.modele} - Année {self.annee}")