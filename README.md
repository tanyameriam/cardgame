# cardgame
A non-conventional cardgame in python


Basic Rules:
- Each player is dealt three cards.
- 'A' is considered to have a number value of 1.
- 'A' is considered the top card in a face-off. So the order is A > K > Q > J > 10...2

Victory:
- A trail (three cards of the same number) is the highest possible combination.
- The next highest is a sequence (numbers in order, e.g., 4,5,6. A is considered to have a value of 1).
- The next highest is a pair of cards (e.g.: two Kings or two 10s).
- If all else fails, the top card (by number value wins).
- If the top card has the same value, each of the tied players draws a single card till a winner is found. Only the newly drawn cards are compared to decide a tie. The top card wins a tie.

In the code:
There are four modules Utils.py , Tie.py , playingcards,py ,static.py

In playingcards.py
1) creation of deck
2) dealing cards to the players
3)single card drawing function
4)if insufficient cards quitting the game displaying insufficient cards

in Tie.py
1)checking tie after the first deal
2)if equal priority passing to the singe card drawing function, to break the tie
3)here highest facing card wins
4)if again tie, draws single card and determines the winner .

Utils.py
1)class cards and suits declared
2)checkign the priority according to the rules and priority is returned

Static.py
1)all the global variables declared




