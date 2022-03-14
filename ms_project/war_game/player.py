class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        result = self.name
        for card in self.cards:
            result += ", " + str(card)
        return result
