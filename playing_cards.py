from enum import Enum
from enum import IntEnum
from random import *
full_deck=[]
partial_deck=[]
player_1=[]
player_2=[]
player_3=[]
player_4=[]

class Card(IntEnum):
    ACE =14
    KING =13
    QUEEN =12
    JACK =11
    TEN=10
    NINE=9
    EIGHT=8
    SEVEN=7
    SIX=6
    FIVE=5
    FOUR=4
    THREE=3
    TWO=2


#enum for suits
class Suite(Enum):
    SPADES="spades"
    CLUBS="clubs"
    HEART="heart"
    DIAMOND="diamond"


class playingcards:
    def __init__(self,cardvalue,cardsuit):
        self.card = cardvalue
        self.suit = cardsuit

#creating the full deck
def createdeck():
    for suit in Suite:
        for card in Card:
            full_deck.append(playingcards(Card(card),Suite(suit)))
    return full_deck


#draw single catd form deck
def drawcard(deck):
    rand_card=randint(0, len(deck)-1)
    return deck.pop(rand_card)

#compare the values
#append card to all the players in loop
def deal_plr1():
    for k in range (0,3):
        if(len(partial_deck)>0):
            test_card=drawcard(partial_deck)
            player_1.append(test_card)
        print("player 1",player_1[k].card,player_1[k].suit,(player_1[k].card).value)
    return player_1
def deal_plr2():
    for k in range (0,3):
        if(len(partial_deck)>0):
            test_card=drawcard(partial_deck)
            player_2.append(test_card)
        print("player 2",player_2[k].card,player_2[k].suit,(player_2[k].card).value)
    return player_2
def deal_plr3():
    for k in range (0,3):
        if(len(partial_deck)>0):
            test_card=drawcard(partial_deck)
            player_3.append(test_card)
        print("player 3",player_3[k].card,player_3[k].suit,(player_3[k].card).value)
    return player_3
def deal_plr4():
    for k in range (0,3):
        if(len(partial_deck)>0):
            test_card=drawcard(partial_deck)
            player_4.append(test_card)
        print("player 4",player_4[k].card,player_4[k].suit,(player_4[k].card).value)
    return player_4

def sort_cards(list_comp):
    list_comp.sort(key=lambda x:(x.card).value)
    print([item.card for item in list_comp])
    return list_comp



#create deck
createdeck()
partial_deck=list(full_deck)
deal_plr1()
sort_cards(player_1)
deal_plr2()
sort_cards(player_2)
deal_plr3()
sort_cards(player_3)
deal_plr4()
sort_cards(player_4)
