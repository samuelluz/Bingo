class Player(object):
    def __init__(self, player_id, ticket):
        self.player_id = player_id
        self.ticket = ticket
        self.points = 0


def loadPlayerData(filename):
    player_list = []
    with open(filename, 'r') as f:
        for line in f:
            p_id = line[0:8]
            p_game = line[9:]

            # print(p_game.strip())
            player_list.append(
                Player(p_id, p_game.strip().split(' ')))

    return player_list


def savePlayerData(player_data, filename='results.txt'):
    with open(filename, 'w') as f:
        for p in player_data:
            f.write(
                ':'.join([p.player_id, ' '.join(p.ticket), str(p.points)]) + '\n')


def saveWinners(player_data, filename='winners.txt'):
    with open(filename, 'w') as f:
        for p in player_data:
            if p.points == 25:
                f.write(
                    ':'.join([p.player_id, ' '.join(p.ticket), str(p.points)]))


def newNumber(player_data, new_number):
    winners_id = []
    for p in player_data:
        if str(new_number) in p.ticket:
            if p.points < 25:
                p.points += 1

            if p.points >= 25 and p.player_id not in winners_id:
                winners_id.append(p.player_id)

    return winners_id


def playerById(player_data, p_id):
    for p in player_data:
        if p.player_id == p_id:
            return p_id


def main():
    numbers = [5, 6, 9, 10, 12, 22, 23, 24, 25, 26, 34, 37, 39,
               40, 43, 46, 48, 50, 51, 60, 63, 65, 70, 72, 74]
    player_list = loadPlayerData('dados totais.txt')
    history_numbers = []
    # while True:
    #     n = input('Type new number:')
    #     while str(n) in history_numbers:
    #         n = input('Repeated number!\nType new number:')
    #     history_numbers.append(n)
    for n in numbers:

        if n == 'q':
            print('Ending game.')
            break
        else:
            winners_id = newNumber(player_list, n)
            if len(winners_id) > 0:
                for w in winners_id:
                    print('Player(s): {} won!'.format(
                        playerById(player_list, w)))

                n = input('Do you want to continue?(S/N)')
                if n == 'n' or n == 'N':
                    break

    savePlayerData(player_list)
    saveWinners(player_list, 'winners.txt')


if __name__ == '__main__':
    main()
