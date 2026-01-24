




def is_there_7_players(players: list[str]):
    counter = 1

    for i in range(1, len(players)):
        if players[i] == players[i - 1]:
            counter += 1
            if counter >= 7:
                return True
        else:
            counter = 1
    return False


players = list(map(str, input()))

if is_there_7_players(players):
    print('YES')
else:
    print('NO')