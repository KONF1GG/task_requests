import requests
import json

url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url)

if response.status_code != 200:
    print(f'Ошибка: {response.status_code}')
else:
    print(f'Запрос выполнен успешно!')

    heros = json.loads(response.text)
    hulk = None
    captain_america = None
    thanos = None

    for hero in heros:
        if hero['name'] == 'Hulk':
            hulk = hero
        if hero['name'] == 'Captain America':
            captain_america = hero
        if hero['name'] == 'Thanos':
            thanos = hero

    most_intelligent = max(hulk["powerstats"]["intelligence"],
                           captain_america["powerstats"]["intelligence"],
                           thanos["powerstats"]["intelligence"])

    if most_intelligent == hulk["powerstats"]["intelligence"]:
        print("Самый умный супергерой - Hulk")
    elif most_intelligent == captain_america["powerstats"]["intelligence"]:
        print("Самый умный супергерой - Captain America")
    elif most_intelligent == thanos["powerstats"]["intelligence"]:
        print("Самый умный супергерой - Thanos")