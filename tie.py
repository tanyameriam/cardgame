def check_tie(player_cards):
   if player_cards['card'][0].card.value == player_cards['card'][1].card.value:
       if player_cards['card'][1].card.value == player_cards['card'][2].card.value:
            player_cards['priority'] = 1
       else:
            player_cards['priority'] = 2
   elif player_cards['card'][1].card.value == player_cards['card'][2].card.value:
        player_cards['priority'] = 2
   else:
       for k in range(0, 3):
           if player_cards['card'][k].card.value == 14:
               if player_cards['card'][1].card.value == 3 and player_cards['card'][2].card.value == 2:
                   player_cards['priority'] = 3
       for k in range(0, 3):
           if player_cards['card'][k].card.value != 14:
               if player_cards['card'][0].card.value - 1 == player_cards['card'][1].card.value:
                   if player_cards['card'][1].card.value - 1 == player_cards['card'][2].card.value:
                        player_cards['priority'] = 3


def priority_tie(players_list):
    player_number = []
    priority = []
   # player_numbers_tie = priority_players_list
    for k in range(0, len(players_list)):
        priority.append(players_list[k]['priority'])
        maximum_priority = max(priority)
    for j in range(0, len(players_list)):
        if maximum_priority == players_list[j]['priority']:
            player_number.append(j)
    if len(player_number) > 1:
        print("tie")
    return player_number















