class Morpion:

    def __init__(self):
        self.plateau = [[' ' for _ in range(3)]
                        for _ in range(3)]  # plateau de 3x3
        self.joueur = 'X'  # Joueur par défaut

    def afficher(self):
        # Code pour afficher le plateau
        for ligne in self.plateau:
            print("|".join(ligne))
            print("-" * 5)

    def jouer_coup(self, ligne, colonne):
        """Joue un coup pour le joueur actuel à la position donnée."""
        if self.plateau[ligne][colonne] == ' ':
            self.plateau[ligne][colonne] = self.joueur
            return True
        return False

    def changer_joueur(self):
        pass

    def jouer(self):
        pass
