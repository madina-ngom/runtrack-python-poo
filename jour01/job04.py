class SePresenter():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def _setNom(self):    
        self.nom = input ("Quel est votre nom ?")
    def _setPrenom(self):
        self.prenom = input ("Quel est votre prenom ?")

