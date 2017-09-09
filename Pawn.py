class Pawn:

    def __init__(self, couleur):
        """
        :type couleur str
        """
        # todo: couleur -> color
        self.couleur = couleur

    def __repr__(self):
        return str(self.couleur)
