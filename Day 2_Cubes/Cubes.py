def task1():
    
    games = {}
    compare = {'game':{'red': 12, 'green':13, 'blue':14}}
    
    with open(r'D:\Source\AdventCode\Day 2_Cubes\input.txt') as f:
        data = f.read()
        
    data = data.split('\n')
    
    for i in data:
        game = i.split(':')
        gameid = game[0]
        game_results = game[1].split(';')
        for i in game_results: 
            colors = i.split(',')
            if(gameid not in games.keys()):
                games.update({gameid:{}})
            for j in colors:
                round_results = j.lstrip(' ').split(' ')
                if len(games[gameid].items()) == 0:
                    games[gameid].update({round_results[1]:int(round_results[0])})
                elif round_results[1] not in list(games[gameid].keys()):
                    games[gameid].update({round_results[1]:int(round_results[0])})
                else:
                    if(int(games[gameid][round_results[1]]) < int(round_results[0])):
                        games[gameid][round_results[1]] = int(round_results[0])
    sum = 0 
    possible = []
    for i in list(games.keys()):
        if int(games[i]['red']) <= compare['game']['red'] and int(games[i]['blue']) <= compare['game']['blue'] and int(games[i]['green']) <= compare['game']['green']:
            sum += int(i.split(' ')[1])
            #possible.append(int(i.split(' ')[1]))
    return sum

def task2():
    
    games = {}
    compare = {'game':{'red': 12, 'green':13, 'blue':14}}
    
    with open(r'D:\Source\AdventCode\Day 2_Cubes\input.txt') as f:
        data = f.read()
        
    data = data.split('\n')
    
    for i in data:
        game = i.split(':')
        gameid = game[0]
        game_results = game[1].split(';')
        for i in game_results: 
            colors = i.split(',')
            if(gameid not in games.keys()):
                games.update({gameid:{}})
            for j in colors:
                round_results = j.lstrip(' ').split(' ')
                if len(games[gameid].items()) == 0:
                    games[gameid].update({round_results[1]:int(round_results[0])})
                elif round_results[1] not in list(games[gameid].keys()):
                    games[gameid].update({round_results[1]:int(round_results[0])})
                else:
                    if(int(games[gameid][round_results[1]]) < int(round_results[0])):
                        games[gameid][round_results[1]] = int(round_results[0])
    sum = 0 
    possible = []
    for i in list(games.keys()):
            sum += int(games[i]['red']) * int(games[i]['blue']) * int(games[i]['green'])
            #possible.append(int(i.split(' ')[1]))
    return sum


print(task1())
print(task2())