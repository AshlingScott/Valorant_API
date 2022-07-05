import requests
import json

# Gets the average stats of the last 5 games for a player
def average_stats_last_5():
    # Player and code for finding a specific player
    player = 'Ambrosia'
    code = 'AMBR'

    # Dictionary of stats, initially set to 0
    stats = {'score' : 0, 'kills' : 0, 'deaths' : 0, 'assists' : 0,
    'bodyshots' : 0, 'headshots' : 0, 'legshots' : 0}

    # Access API
    response = requests.get("https://api.henrikdev.xyz/valorant/v3/matches/na/"
        + player + "/" + code)
    data = json.loads(response.text)

    # Look through the data from each of the 5 games, and extract data
    # matching the chosen player name and code
    for x in range(5):
        player_list = data['data'][x]['players']['all_players']

        # Increment stat totals
        for x in player_list:
            # Check if correct player
            if ((x['name'] == player) and (x['tag'] == code)):
                stats['score'] += x['stats']['score']
                stats['kills'] += x['stats']['kills']
                stats['deaths'] += x['stats']['deaths']
                stats['assists'] += x['stats']['assists']
                stats['bodyshots'] += x['stats']['bodyshots']
                stats['headshots'] += x['stats']['headshots']
                stats['legshots'] += x['stats']['legshots']

    print(player + '\'s Stats')
    stats = get_average(stats, 5)
    print('Score:      ' + str(stats['score']))
    print('KDA:        ' + str(stats['kills']) + '/' + str(stats['deaths']) + '/' + str(stats['assists']))
    total_shots = stats['bodyshots'] + stats['headshots'] + stats['legshots']
    print('Headshot %: ' + str(round(stats['headshots'] / total_shots, 2) * 100))
    print('Legshot %:  ' + str(round(stats['legshots'] / total_shots, 2) * 100))

# Takes a dictionary of stats and converts it to per game averages
def get_average(stats, divisor):
    for key in stats:
        stats[key] = (stats[key]/divisor)

    return stats

average_stats_last_5()
