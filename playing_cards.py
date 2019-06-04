from enum import Enum
from enum import IntEnum
from random import *
import numpy as np

full_deck=[]
partial_deck=[]
player_1=[]
plyr1=[]
player_2=[]
plyr2=[]
player_3=[]
plyr3=[]
player_4=[]
plyr4=[]
pr=[]
priority=0
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
    return sort_cards(player_1)
def deal_plr2():
    for k in range (0,3):
        if(len(partial_deck)>0):
            test_card=drawcard(partial_deck)
            player_2.append(test_card)
        print("player 2",player_2[k].card,player_2[k].suit,(player_2[k].card).value)
    return sort_cards(player_2)
def deal_plr3():
    for k in range (0,3):
        if(len(partial_deck)>0):
            test_card=drawcard(partial_deck)
            player_3.append(test_card)
        print("player 3",player_3[k].card,player_3[k].suit,(player_3[k].card).value)
    return sort_cards(player_3)
def deal_plr4():
    for k in range (0,3):
        if(len(partial_deck)>0):
            test_card=drawcard(partial_deck)
            player_4.append(test_card)
        print("player 4",player_4[k].card,player_4[k].suit,(player_4[k].card).value)
    return sort_cards(player_4)

def sort_cards(list_comp):
    list_comp.sort(key=lambda x:(x.card).value, reverse=True)
    return list_comp

def check(list_compare):
    if(((list_compare[0].card).value)==((list_compare[1].card).value)):
        if(((list_compare[1].card).value)==((list_compare[2].card).value)):
            print("all three equal")
            priority=1
        print("two cards equal")
        priority=2
    else:
        for k in range(0,3):
            if(((list_compare[k].card).value)==14):
                ((list_compare[k].card).value)==1
        if((((list_compare[0].card).value)-1)==((list_compare[1].card).value)):
            print(((list_compare[1].card).value)-1)
            if((((list_compare[1].card).value)-1)==((list_compare[2].card).value)):
                print("consecutive")
                priority=3
        priority=0
    return priority

def tie(temp_list) :
        print("draw single card from the deck")
        test_card=drawcard(partial_deck)
        temp_list.append(test_card)
        print("card is",(temp_list.card).value)
        return temp_list

def check_tie(priority_list,player_list):
    values = np.priority_list
    #if 3 cards same
    searchval = 3
    li = np.where(values == searchval)[0]
    if(len(li)>1):
        for l in range(len(li)):
            c=li[l]
            tie(player_list[c+1])
    else:
        #if 2 cards same
        searchval = 2
        li_2 = np.where(values == searchval)[0]
        if(len(li_2)>1):
            for l in range(len(li_2)):
                c=li_2[l]
                tie(player_list[c+1])
        else:
            #if consecutive
            searchval = 1
            li_3 = np.where(values == searchval)[0]
            if(len(li_3)>1):
                for l in range(len(li_3)):
                    c=li_3[l]
                    tie(player_list[c+1])
            else:
                #if no players gets any of the winning criteria
                searchval = 0
                li_4 = np.where(values == searchval)[0]
                if(len(li_4)>1):
                    for l in range(len(li_4)):
                        c=li_4[l]
                        tie(player_list[c+1])






#create deck
createdeck()
#creating deck for dealing cards
partial_deck=list(full_deck)
#dealing cards to the players and returning sorted list
player_1=deal_plr1()
player_2=deal_plr2()
player_3=deal_plr3()
player_4=deal_plr4()
#list of players in a list
players=[player_1,player_2,player_3,player_4]
d=0
while d<4:
    pr[d]=check(players[d])
    d=d+1



check_tie(pr,players)





#checking if tie, if tie then tie breaker
#final winner - decision
