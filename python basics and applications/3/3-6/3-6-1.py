import requests as rqst

with open('dataset_24476_3.txt') as file:
    for num in file:
        response = rqst.get('http://numbersapi.com/{number}/math?json=true'.format( number=num.rstrip() )).json()
        print('Interesting') if response['found'] else print('Boring')