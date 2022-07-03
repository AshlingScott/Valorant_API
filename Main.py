import requests
import json

def average_stats_last_5():
    player = 'Ambrosia'
    code = 'AMBR'
    stats = {}
    stats['score'] = 0
    stats['kills'] = 0
    stats['deaths'] = 0
    stats['assists'] = 0
    stats['bodyshots'] = 0
    stats['headshots'] = 0
    stats['legshots'] = 0

    response = requests.get("https://api.henrikdev.xyz/valorant/v3/matches/na/"
    + player + "/" + code)

    data = json.loads(response.text)

    for x in range(5):
        player_list = data['data'][x]['players']['all_players']

        for x in player_list:
            if ((x['name'] == player) and (x['tag'] == code)):
                stats['score'] += x['stats']['score']
                stats['kills'] += x['stats']['kills']
                stats['deaths'] += x['stats']['deaths']
                stats['assists'] += x['stats']['assists']
                stats['bodyshots'] += x['stats']['bodyshots']
                stats['headshots'] += x['stats']['headshots']
                stats['legshots'] += x['stats']['legshots']

    print(player + '\'s Stats')
    stats = get_average(stats)
    print(stats)

def get_average(stats):
    for key in stats:
        stats[key] = (stats[key]/5)

    return stats

average_stats_last_5()
