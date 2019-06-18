# cardgame
A cardgame in python


Basic Rules:
- Each player is dealt three cards.
- 'A' is considered to have a higher number value.
- 'A' is considered the top card in a face-off. So the order is A > K > Q > J > 10...2

Victory:
- A trail (three cards of the same number) is the highest possible combination.
- The next highest is a sequence (numbers in order, e.g., 4,5,6. A is considered to have a value of 1).
                    eg: A,2,3..and so on in the order order  K > Q > J > 10...2 > A
- The next highest is a pair of cards (e.g.: two Kings or two 10s).
- If all else fails, the top card (by number value wins).
- If the top card has the same value, each of the tied players draws a single card till a winner is found. Only the newly drawn cards are compared to decide a tie. The top card wins a tie.

In the code:
There are three modules namingly, service.py,utils.py,tie,py

The code is run from utils.py.

-python 3.7.2
 -numpy 1.16.4
