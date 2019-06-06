from enum import Enum
from enum import IntEnum
from random import *
import numpy as np
from static import *
from tie import *
from utils import *

full_deck=[]            #full original deck
pr=[]                   #priority list according to the rules

#creating the full deck
def createdeck():
    for suit in Suite:
        for card in Card:
            full_deck.append(playingcards(Card(card),Suite(suit)))
    return full_deck


class playingcards:
    def __init__(self,cardvalue,cardsuit):
        self.card = cardvalue
        self.suit = cardsuit

#to check if there is sufficient card for the next draw
def insufficient():
    if(len(partial_deck)==0):
        print("insufficient cards in deck game over")
        quit()          #quitting the game when there is insufficient cards in the deck

#compare the values
#append card to all the players in loop
def deal_plr(player,player_n):
    for k in range (0,3):
        if(len(partial_deck)>0):
            test_card=drawcard(partial_deck)
            player_n.append(test_card)
        print(player,player_n[k].card,player_n[k].suit,(player_n[k].card).value)
    return sort_cards(player_n)


#sort cards based on their values
def sort_cards(list_comp):
    list_comp.sort(key=lambda x:(x.card).value, reverse=True)
    return list_comp

#draw single catd form deck
def drawcard(deck):
    rand_card=randint(0, len(deck)-1)
    if(len(deck)>0):
        return deck.pop(rand_card)
    else:
        return insufficient()




# def deal_plr2():
#     for k in range (0,3):
#         if(len(partial_deck)>0):
#             test_card=drawcard(partial_deck)
#             player_2.append(test_card)
#         print("player 2",player_2[k].card,player_2[k].suit,(player_2[k].card).value)
#     return sort_cards(player_2)
# def deal_plr3():
#     for k in range (0,3):
#         if(len(partial_deck)>0):
#             test_card=drawcard(partial_deck)
#             player_3.append(test_card)
#         print("player 3",player_3[k].card,player_3[k].suit,(player_3[k].card).value)
#     return sort_cards(player_3)
# def deal_plr4():
#     for k in range (0,3):
#         if(len(partial_deck)>0):
#             test_card=drawcard(partial_deck)
#             player_4.append(test_card)
#         print("player 4",player_4[k].card,player_4[k].suit,(player_4[k].card).value)
#     return sort_cards(player_4)



#method to print winner
def winner(x):
    print("winner is player : ", x+1)
    deal()



#dealing cards to the players and returning sorted list
def deal():
    while len(partial_deck) > 0:
        player_1.append(deal_plr("player1", player_1))
        player_2.append(deal_plr("player2", player_2))
        player_3.append(deal_plr("player3", player_3))
        player_4.append(deal_plr("player4", player_4))
        #list of players in a list
        players=[player_1,player_2,player_3,player_4]
        d=0
        while d<4:
            pr.append(check(players[d]))
            d=d+1


        #checking if tie, if tie then tie breaker
        compare_tie = check_tie(pr, players)
        again_compre_tie(compare_tie, players)
    insufficient()


#create deck
createdeck()

#creating deck for dealing cards
partial_deck = list(full_deck)
deal()
