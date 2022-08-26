import requests
import json

# List of players to get data from
players = []

# Gets the average stats of the last 5 games for each player in the player list
def stats():
    # Iterate through players in the list
    for player in players:
        # Split player name into name and code
        split = player.split('#')
        # Dictionary of stats, initially set to 0
        statistics = {'score' : 0, 'kills' : 0, 'deaths' : 0, 'assists' : 0,
            'bodyshots' : 0, 'headshots' : 0, 'legshots' : 0,
            'damage_dealt' : 0, 'damage_taken' : 0}

        # Access API for player
        response = requests.get('https://api.henrikdev.xyz/valorant/v3/matches/na/'
            + split[0] + '/' + split[1])
        data = json.loads(response.text)

        # Look through the data from each of the 5 games, and extract data
        # matching the chosen player name and code
        for x in range(4):
            player_list = data['data'][x]['players']['all_players']

            # Increment stat totals
            for x in player_list:
                # Check if correct player and assign statistics
                if ((x['name'] == split[0]) and (x['tag'] == split[1])):
                    statistics['score'] += x['stats']['score']
                    statistics['kills'] += x['stats']['kills']
                    statistics['deaths'] += x['stats']['deaths']
                    statistics['assists'] += x['stats']['assists']
                    statistics['bodyshots'] += x['stats']['bodyshots']
                    statistics['headshots'] += x['stats']['headshots']
                    statistics['legshots'] += x['stats']['legshots']
                    statistics['damage_dealt'] += x['damage_made']
                    statistics['damage_taken'] += x['damage_received']


        # Stat output
        print('\n' + split[0] + '\'s Stats')
        statistics = get_average(statistics, 5)
        print('Score:      ' + str(statistics['score']))
        print('KDA:        ' + str(statistics['kills']) + '/' + str(statistics['deaths']) + '/' + str(statistics['assists']))
        print('Dmg Ratio:  ' + str(round(statistics['damage_dealt'] / statistics['damage_taken'], 2)))
        total_shots = statistics['bodyshots'] + statistics['headshots'] + statistics['legshots']
        print('Headshot %: ' + str(round(statistics['headshots'] / total_shots, 2) * 100))
        print('Legshot %:  ' + str(round(statistics['legshots'] / total_shots, 2) * 100) + '\n')

# Takes a dictionary of stats and converts it to per game averages
def get_average(stats, divisor):
    for key in stats:
        stats[key] = (stats[key]/divisor)

    return stats

# Gets input from the user
# add: Adds name to the list of players to be compared
# stats: Lists out the stats for each player
# compare: Compares stats player by player on the list
# players: Print list of players entered
# quit: Exit program
def input_loop():
    print('Commands: add, stats, compare, players, quit')
    choice = input()
    if (choice == 'add'):
        print('Input: name#code')
        x = input()
        players.append(x)
        print('added ' + x)
    elif (choice == 'stats'):
        stats()
    elif (choice == 'compare'):
        pass
    elif (choice == 'players'):
        print(players)
    elif (choice == 'quit'):
        quit()
    else:
        print('Not a command')

while(True):
    input_loop()
