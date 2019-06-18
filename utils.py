from service import *
from random import *
from tie import *
import numpy


player_1 = {
    "card": [],
    "priority": 0,
    "name": 'John'

}             # players
player_2 = {
    "card": [],
    "priority": 0,
    "name": 'Geoff'

}             # players
player_3 = {
    "card": [],
    "priority": 0,
    "name": 'Rian'

}             # players
player_4 = {
    "card": [],
    "priority": 0,
    "name": 'Vic'

}             # players

print("4 PLAYERED GAME : ENTER NAMES\n")
player_1['name'] = input("Enter player 1 name: \n")
while(player_1['name']==""):
        player_1['name'] = input("Enter player 1 name (Should not be empty): \n")
player_2['name'] = input("Enter player 2 name: \n")
while(player_2['name']==""):
        player_2['name'] = input("Enter player 2 name (Should not be empty): \n")
player_3['name'] = input("Enter player 3 name: \n")
while(player_3['name']==""):
        player_3['name'] = input("Enter player 3 name (Should not be empty): \n")
player_4['name'] = input("Enter player 4 name: \n")
while(player_4['name']==""):
        player_4['name'] = input("Enter player 4 name (Should not be empty): \n")
print(player_1['name'], "\n", player_2['name'], "\n", player_3['name'], "\n", player_4['name'], "\n")





# draw single card form deck


def drawcard(deck):
    rand_card = randint(0, len(deck)-1)
    if len(deck) > 11:
        return deck.pop(rand_card)
    else:
        return insufficient()

# compare the values
# append card to all the players in loop


def deal_plr(player, player_n):
    if len(partial_deck) > 11:
        for k in range(0, 3):
            if len(partial_deck) > 11:
                test_card = drawcard(partial_deck)
                player_n.append(test_card)
            print(player, player_n[k].card, player_n[k].suit)
    else:
        return insufficient()
    return sort_cards(player_n)


# to check if there is sufficient card for the next draw
def insufficient():
    if(len(partial_deck)<12):
        print(len(partial_deck))
        print("insufficient cards in deck game over")
        quit()          # quitting the game when there is insufficient cards in the deck


# dealing cards to the players and returning sorted list


def deal():
    cards_1 = []
    cards_2 = []
    cards_3 = []
    cards_4 = []
    input("press enter to deal cards")
    cards_1.append(deal_plr(player_1['name'], cards_1))
    player_1['card'] = cards_1
    player_1['priority'] = 0
    input("press enter to deal cards")
    cards_2.append(deal_plr(player_2['name'], cards_2))
    player_2['card'] = cards_2
    player_2['priority'] = 0
    input("press enter to deal cards")
    cards_3.append(deal_plr(player_3['name'], cards_3))
    player_3['card'] = cards_3
    player_3['priority'] = 0
    input("press enter to deal cards")
    cards_4.append(deal_plr(player_4['name'], cards_4))
    player_4['card'] = cards_4
    player_4['priority'] = 0


# diplayng the winner
def display(announce_winner, players_name_list_of_diplay):
    ar = int(announce_winner[0])
    #print(ar)
    print("winner is ", players_name_list_of_diplay[ar])


def checking_tie_win(maximum_of_priority,players_name):
    tie_breaker = []
    tie_again = []
    new_players_list = []
    if len(maximum_of_priority) > 1:
        if len(partial_deck) > 3:
            players_name = []
            for k in range(0, len(maximum_of_priority)):
                test_card = drawcard(partial_deck)  # drawing the single card to break the tie
                tie_breaker.append(test_card)  # appending thw test card ti the tie.breker list
                j = maximum_of_priority[k]  # the value passed to j to find the player number
                players[j]['priority'] = tie_breaker[k].card.value  # assigning the player[j] th dictionary priority value as the card value
                tie_again.append(players[j])
                ar = numpy.array(j)
                #ar = ar+1
                print("card drawn by player", players[j]['name'], tie_breaker[k].card)
                players_name.append(players[j]['name'])
            if len(tie_again) > 1:
                new_players_list.append(priority_tie(tie_again))
                to_flatten_lists(new_players_list)   # flatten the list of list
                checking_tie_win(to_flatten_lists(new_players_list),players_name)  # checking tie again and drawing the cards.

    else:
        display(maximum_of_priority, players_name)



print("""CARD GAME
 CARD PRIORITY A > K > Q > J > 10...2
 
Rules:

Victory:
- A trail (three cards of the same number) is the highest possible combination.
- The next highest is a sequence  eg: A,2,3..and so on in the order order  K > Q > J > 10...2 > A
- The next highest is a pair of cards (e.g.: two Kings or two 10s).
- If all else fails, the top card wins.
- If the top card has the same value, each of the tied players draws a single card till a winner is found.
  Only the newly drawn cards are compared to decide a tie. The top card wins a tie. \n""")
while (1):
    user_imp = input("Game start deal :y/n\n")
    if user_imp == 'n':
        print("Quitting game..")
        break
    elif user_imp == 'y':
                createdeck()
                partial_deck = list(full_deck)   # creating deck for dealing cards
                # while len(partial_deck) > 11:
                print("dealing..")
                deal()
                players_name = [player_1['name'], player_2['name'], player_3['name'], player_4['name']]
                if len(partial_deck) > 11:
                    check_tie(player_1)
                    check_tie(player_2)
                    check_tie(player_3)
                    check_tie(player_4)
                    players = [player_1, player_2, player_3, player_4]                                              # total list of players
                    maximum_of_priority = priority_tie(players)    # from tie.py we get the maximum priority(from the rules of the game)
                    checking_tie_win(maximum_of_priority,players_name)
                else:
                    insufficient()
    else:
        print("Give proper input")

