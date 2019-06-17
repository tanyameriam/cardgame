from enum import Enum
from enum import IntEnum

full_deck = []  # full original deck
# enum for class cards


class Card(IntEnum):
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2

# enum for suits


class Suite(Enum):
    SPADES = "spades"
    CLUBS = "clubs"
    HEART = "heart"
    DIAMOND = "diamond"


class playingcards:
    def __init__(self,cardvalue,cardsuit):
        self.card = cardvalue
        self.suit = cardsuit


# creating deck
def createdeck():
    for suit in Suite:
        for card in Card:
            full_deck.append(playingcards(Card(card), Suite(suit)))
    return full_deck


# sort cards based on their values
def sort_cards(list_comp):
    list_comp.sort(key=lambda x: x.card.value, reverse=True)
    return list_comp


def to_flatten_lists(list_of_lists):
    flattened_list = []
    for x in list_of_lists:
        for y in x:
            flattened_list.append(y)
    return flattened_list



