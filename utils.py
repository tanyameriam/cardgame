from enum import Enum
from enum import IntEnum
from random import *
import numpy as np
from playing_cards import *
from static import *
from tie import *

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







#compare eacch card value to check the priorities
# 3 : All equal
# 2 : 2 cards equal
# 1 : cards consequent
# 0 : none of the above

def check(list_compare):
    if(((list_compare[0].card).value)==((list_compare[1].card).value)):
        if(((list_compare[1].card).value)==((list_compare[2].card).value)):
            #print("all three equal")
            priority=1
        priority=2
        #print("two cards equal")
    elif(((list_compare[1].card).value)==((list_compare[2].card).value)):
        #print("two cards equal")
        priority=2
    else:
        for k in range(0,3):
            if(((list_compare[k].card).value)==14):
                if((((list_compare[1].card).value))==3 and ((list_compare[2].card).value)==2):
                    priority=3
        if((((list_compare[0].card).value)-1)==((list_compare[1].card).value)):
            if((((list_compare[1].card).value)-1)==((list_compare[2].card).value)):
                #print("consecutive")
                priority=3
        priority=0
    return priority

