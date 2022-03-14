class Card:
    def __init__(self, suit, name):
        # instance variables
        self.suit = suit
        self.name = name

        if name == 'Ace':
            self.rank = 14
        elif name == 'King':
            self.rank = 13
        elif name == 'Queen':
            self.rank = 12
        elif name == 'Jack':
            self.rank = 11
        else:
            self.rank = int(name)

    def __str__(self):
        return self.name + " of " + self.suit
