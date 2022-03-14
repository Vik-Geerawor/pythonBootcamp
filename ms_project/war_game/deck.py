from card import Card


def generate_suit(suit, cards):
    for i in range(0, 13):          # upper limit = 13
        if i == 0:
            cards.append(Card(suit, 'Ace'))
        elif i == 10:
            cards.append(Card(suit, 'Jack'))
        elif i == 11:
            cards.append(Card(suit, 'Queen'))
        elif i == 12:
            cards.append(Card(suit, 'King'))
        else:
            cards.append(Card(suit, str(i + 1)))


class Deck:

    def __init__(self):
        # instance variable
        self.cards = []

        # generate suits
        generate_suit('Clubs', self.cards)
        generate_suit('Diamonds', self.cards)
        generate_suit('Hearts', self.cards)
        generate_suit('Spades', self.cards)

    def show_cards(self):
        for card in self.cards:
            print(card)
