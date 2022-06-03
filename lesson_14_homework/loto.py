import random
import cart
import bag
import decors

print('Старт игры')
bag = bag.Bag()
player_list = []
check_win_list = []
players_number = int(input('Введите колличество игроков: '))
for i in range(players_number):
    player = cart.Card()
    player_list.append(player)
    check_win_list.append(player.numbers[0].count('x') +
                          player.numbers[1].count('x') +
                          player.numbers[2].count('x'))
    player.card_generator()
while check_win_list.count(15) < 1:
    check_win_list.clear()
    print('Следующий раунд')
    print(f'В мешке осталось {len(bag.keg_list)} боченков')
    keg_number = bag.get_keg()
    for i in range(players_number):
        # if player_list[players_number-1].name == '_Computer_':
            print(f'Проверяем, есть ли номер {keg_number} '
                  f'у игрока{player_list[i].name}')
            player_list[i].cross_numeral(keg_number)
            check_win_list.append(player_list[i].numbers[0].count('x') +
                                  player_list[i].numbers[1].count('x') +
                                  player_list[i].numbers[2].count('x'))
        # else:
        #     ans = input('Желаете зачеркнуть цифру? y/n: ')
        #     if ans == 'y':
        #         print(f'Проверяем, есть ли номер {keg_number} '
        #               f'у игрока{player_list[i].name}')
        #         if (keg_number in player_list[i].numbers[0] or
        #            keg_number in player_list[i].numbers[1] or
        #            keg_number in player_list[i].numbers[2]):
        #             player_list[i].cross_numeral(keg_number)
        #             check_win_list.append(player_list[i].numbers[0].count('x') +
        #                                   player_list[i].numbers[1].count('x') +
        #                                   player_list[i].numbers[2].count('x'))


print(f'Игра окончена. Победитель - '
      f'{player_list[check_win_list.index(15)].name}')


