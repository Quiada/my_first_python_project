details_damage_price = {'energy gun': 100, 'minigun': 70, 'thor hammer': 50, 'laser gun': 80, 'rail gun': 90, 'sniper rifle': 150}
details_survive_price = {'shield': 50, 'energy shield': 80, 'resist': 30, 'evasion': 100, 'armor': 140}
users_bot = {}
player_list = []
def player_maker(players_list):
    user_choose = 'yes'
    while user_choose == 'yes' or user_choose == 'y':
        user_input = input('input a Player name - ')
        if len(user_input)<3:
            continue
        player_list.append(str.capitalize(user_input))
        user_choose = input('More Players - Y/N -')
    print(f'Players - {str(player_list)[1:-1]}')
def bot_maker(start_sum,players_list):
    for player in player_list:
        wallet = start_sum
        users_bot[player] = {}
        while wallet >=min(details_survive_price.values()):
            string_1 = f'{player}, you have {wallet} coins'
            print(f'{string_1:=^82}')
            print('{detail:^^80}'.format(detail='Damage deal details'))
            for gun, price in details_damage_price.items():
                print(f'{gun} - {price}')
            print('{detail:^^80 }.format(detail = Survive detailes')
            for survive_detail, price in details_survive_price.items():
                print(f'{survive_detail} - {price}')
                user_choose = str.lower(input('Choose your details -'))
                if user_choose in users_bot[player].keys():
                    print('{string:!^80}'.format(string='not enough coins'))
                    continue
                wallet -= details_survive_price[user_choose]
            else:
                if user_choose in details_damage_price.keys():
                    if wallet < details_survive_price[user_choose]:
                        print('{string:!^80}\n'.format(string='not enough '))
                        continue
                    wallet -= details_survive_price[user_choose]
                    users_bot[player][user_choose] = details_survive_price[user_choose]
                else:
                    print('\nYour choose is wrong!\n')
                    continue
                print(f'\n\n{player} bot_details: {str(users_bot[player].keys())[11:-2]}\n\n')
            for player in player_list:
                print(f'{player} bot details: {str(users_bot[player].keys())[11:-2]}')
player_maker(player_list)
start_sum = int(input('Input start capital - '))
max_start_sum = sum(details_damage_price.values())+sum(details_survive_price.values())
min_start_sum = sum(details_damage_price.values())
if start_sum > max_start_sum:
    start_sum = max_start_sum
if start_sum < min_start_sum:
    start_sum = min_start_sum
bot_maker(start_sum=start_sum, players_list=player_list)
