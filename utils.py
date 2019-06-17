from service import *
from random import *
from tie import *
import numpy


player_1 = {
    "card": [],
    "priority": 0,
    "name": 'abc'

}             # players
player_2 = {
    "card": [],
    "priority": 0,
    "name": 'def'

}             # players
player_3 = {
    "card": [],
    "priority": 0,
    "name": 'ghi'

}             # players
player_4 = {
    "card": [],
    "priority": 0,
    "name": 'jkl'

}             # players


# draw single card form deck


def drawcard(deck):
    rand_card = randint(0, len(deck)-1)
    if len(deck) > 0:
        return deck.pop(rand_card)
    else:
        return insufficient()

# compare the values
# append card to all the players in loop


def deal_plr(player, player_n):
    if len(partial_deck) > 3:
        for k in range(0, 3):
            if len(partial_deck) > 0:
                test_card = drawcard(partial_deck)
                player_n.append(test_card)
            print(player, player_n[k].card, player_n[k].suit, player_n[k].card.value)
    else:
        return insufficient()
    return sort_cards(player_n)


#to check if there is sufficient card for the next draw
def insufficient():
    if(len(partial_deck)==0):
        print(len(partial_deck))
        print("insufficient cards in deck game over")
        quit()          #quitting the game when there is insufficient cards in the deck


# dealing cards to the players and returning sorted list


def deal():
    cards_1 = []
    cards_2 = []
    cards_3 = []
    cards_4 = []
    cards_1.append(deal_plr("player1", cards_1))
    player_1['card'] = cards_1
    player_1['priority'] = 0
    cards_2.append(deal_plr("player2", cards_2))
    player_2['card'] = cards_2
    player_2['priority'] = 0
    cards_3.append(deal_plr("player3", cards_3))
    player_3['card'] = cards_3
    player_3['priority'] = 0
    cards_4.append(deal_plr("player4", cards_4))
    player_4['card'] = cards_4
    player_4['priority'] = 0

# diplayng the winner
def display(announce_winner):
    ar = numpy.array(announce_winner)
    print(ar + 1)
    print("winner is ", ar+1, "player number in the list..  ")


def checking_tie_win(maximum_of_priority):
    tie_breaker = []
    tie_again = []
    new_players_list = []
    if len(maximum_of_priority) > 1:
        if len(partial_deck) > 3:
            for k in range(0, len(maximum_of_priority)):
                test_card = drawcard(partial_deck)  # drawing the single card to break the tie
                tie_breaker.append(test_card)  # appending thw test card ti the tie.breker list
                j = maximum_of_priority[k]  # the value passed to j to find the player number
                players[j]['priority'] = tie_breaker[k].card.value  # assigning the player[j] th dictionary priority value as the card value
                tie_again.append(players[j])
                ar = numpy.array(j)
                ar = ar+1
                print("card drawn by player", ar, tie_breaker[k].card, tie_breaker[k].card.value)
            if len(tie_again) > 1:
                new_players_list.append(priority_tie(tie_again))
                to_flatten_lists(new_players_list)   # flatten the list of list
                checking_tie_win(to_flatten_lists(new_players_list))  # checking tie again and drawing the cards.

    else:
        display(maximum_of_priority)



print("CARD GAME: CARD PRIORITY A > K > Q > J > 10...2")
user_imp = input("Game start deal :y/n")
if user_imp == 'n':
    print("Quitting game..")
    quit()
else:
    if user_imp == 'y':
        createdeck()
        partial_deck = list(full_deck)   # creating deck for dealing cards
        while len(partial_deck) > 3:
            print("dealing..")
            deal()
            if len(partial_deck) > 3:
                check_tie(player_1)
                check_tie(player_2)
                check_tie(player_3)
                check_tie(player_4)
                players = [player_1, player_2, player_3, player_4]                                              # total list of players
                maximum_of_priority = priority_tie(players)    # from tie.py we get the maximum priority(from the rules of the game)

                checking_tie_win(maximum_of_priority)
            else:
                insufficient()
        print("insufficient cards in the deck")
        quit()



