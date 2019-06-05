from enum import Enum
from enum import IntEnum
from random import *
import numpy as np
from playing_cards import *

#passing the priority list and players list, to find the winner, if there is a tie passing to the tie() method for drwaing another card
def check_tie(priority_list,player_list):
    values = np.array(priority_list)
    #if 3 cards same
    searchval = 3
    li = np.where(values == searchval)[0]
    if(len(li)>1):
        for l in range(len(li)):
            c=li[l]
            compare_tie.append(tie(player_list[c]))
        if(len(li)==1):
            winner(c+1)
            #print("winner is player : ",c+1)

    else:
        #if 2 cards same
        searchval = 2
        li_2 = np.where(values == searchval)[0]
        if(len(li_2)>1):
            for l in range(len(li_2)):
                c=li_2[l]
                compare_tie.append(tie(player_list[c]))
            if(len(li_2)==1):
                winner(c+1)
                #print("winner is player : ",c+1)

        else:
            #if consecutive
            searchval = 1
            li_3 = np.where(values == searchval)[0]
            if(len(li_3)>0):
                for l in range(len(li_3)):
                    c=li_3[l]
                    compare_tie.append(tie(player_list[c]))
                if(len(li_3)==1):
                    #print("winner is player : ",c+1)
                    winner(c+1)

            else:
                #if no players gets any of the winning criteria
                searchval = 0
                li_4 = np.where(values == searchval)[0]
                if(len(li_4)==4):
                    for l in range(len(li_4)):
                        c=li_4[l]
                        compare_tie.append(tie(player_list[c]))
    return compare_tie

#if there is tie again in the priority list of the players draw single card again from the partial deck
def again_compre_tie(tie_list_again, plyrs):
    max=(tie_list_again[0].card).value
    f[0]=0
    for v in range(0, len(tie_list_again)):
        if max <= (tie_list_again[v].card).value:
            f[v]=v                  #f[] gets the maximum value of the list
            max=(tie_list_again[v].card).value

            if len(f) > 1:  # if again in the single card draw there is tie, pass to tie() to draw again for the respective players
                for i in range(0, len(f)):
                    c = f[i]  # to find the player number
                    tie(plyrs[c + 1])  # calling the tie function with the player number
            else:
                winner(v + 1)
                # print("winner is player : ",x+1)
            #print("winner is player : ",v+1)
            winner(v+1)





#draw a single card from the deck
def tie(temp_list) :
        print("draw single card from the deck")
        test_card=drawcard(partial_deck)
        print("card is",(test_card.card).value)
        return test_card

