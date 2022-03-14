from deck import Deck
from player import Player
import random


def distribute_cards(my_deck, player1, player2):
    turn = 1
    count = len(my_deck.cards)

    while count > 0:
        # idx_card = random.randrange(0, count)
        # print(f"Index of card: {idx_card}")

        random_card = my_deck.cards.pop(random.randrange(0, count))
        # print(f"A random card: {random_card}")

        if turn == 1:
            player1.cards.append(random_card)
            turn = 2
        elif turn == 2:
            player2.cards.append(random_card)
            turn = 1

        count = len(my_deck.cards)
        # print(f"No. of cards left: {count}")

    return player1, player2


def play_war(is_war, player1, player2, card_position):
    if player1.cards[card_position + 4].rank > player2.cards[card_position + 4].rank:
        print(f"{player1.cards[card_position + 4]} > {player2.cards[card_position + 4]}")
        for i in range(0, 5):
            player1.cards.append(player1.cards.pop(card_position + i))
            player1.cards.append(player2.cards.pop(card_position + i))
        is_war = False
    elif player2.cards[card_position + 4].rank > player1.cards[card_position + 4].rank:
        print(f"{player2.cards[card_position + 4]} > {player1.cards[card_position + 4]}")
        for i in range(0, 5):
            player2.cards.append(player1.cards.pop(card_position + i))
            player2.cards.append(player2.cards.pop(card_position + i))
        is_war = False
    else:
        card_position = card_position + 5

    return is_war, player1, player2, card_position


if __name__ == '__main__':
    my_deck = Deck()
    player1 = Player('Vik')
    player2 = Player('Neli')

    print(f"*** Start ***\n")
    player1, player2 = distribute_cards(my_deck, player1, player2)

    game_on = True
    while game_on:
        if player1.cards[0].rank > player2.cards[0].rank:
            print(f"{player1.cards[0]} > {player2.cards[0]}")
            player1.cards.append(player1.cards.pop(0))
            player1.cards.append(player2.cards.pop(0))
        elif player2.cards[0].rank > player1.cards[0].rank:
            print(f"{player1.cards[0]} < {player2.cards[0]}")
            player2.cards.append(player1.cards.pop(0))
            player2.cards.append(player2.cards.pop(0))
        else:
            print(f"War Time: {player2.cards[0]} = {player1.cards[0]}")
            is_war = True
            war_card_position = 0

            print(f"{player1.name}:{len(player1.cards)} vs "
                  f"{player2.name}:{len(player2.cards)}")
            try:
                while is_war:
                    if len(player1.cards) >= 4 and len(player2.cards) >= 4:
                        is_war, player1, player2, war_card_position \
                            = play_war(is_war, player1, player2, war_card_position)
                    else:
                        is_war = False
                        game_on = False
                        break
            except IndexError:
                print(f"Player ran out of card")
                print(f"{player1.name}:{len(player1.cards)} vs "
                      f"{player2.name}:{len(player2.cards)}")
                break

    print(f"\nFinal Result")
    if len(player1.cards) > len(player2.cards):

        print(f"{player1.name} wins the war")
    else:
        print(f"{player2.name} wins the war")

    print(f"{player1.name}:{len(player1.cards)} vs "
          f"{player2.name}:{len(player2.cards)}")



