def parse_lines(file):
    data = dict()
    with open (file, 'r') as f:
        lines = f.readlines()
        games = list(map(lambda s: s.strip().split(" "), lines))
        for game in games:
            #print(game)
            hands = []
            results = game[2:]
            #print(results)
            for i,token in enumerate(results):
                if i % 2 == 0:
                    hand = tuple ()
                    num = int(token)

                else:
                    color = token.removesuffix(':')
                    color = color.removesuffix(';')
                    color = color.removesuffix(',')
                    hand = (num, color)
                    hands.append(hand)
            key = int(game[1].removesuffix(':'))
            data.setdefault(key, hands)
    return data

def is_game_valid(game:list)->bool:
    for hand in game:
        num,color = hand
        if num > 12 and color == 'red' or num > 13 and color == "green" or num > 14 and color == "blue":
            return False
    return True

def max_colors(game:list)->list[tuple]:
    bnum,gnum,rnum = 0,0,0
    result = []
    #print(game)
    for hand in game:
        #print(f"New gam \n hand: {hand}")
        num,color = hand
        if color == 'red' and num > rnum:
            rnum = num
            #print(f"red {rnum}")
        if color == 'green' and num > gnum:
            gnum = num
            #print(f"green {gnum}")
        if color == 'blue' and num > bnum:
            bnum = num
            #print(f"blue {bnum}")
    result.append(('green',gnum))
    result.append(('red',rnum))
    result.append(('blue',bnum))
    return result


def compute_min_set_power(min_set:list)->list[int]:
    result = 1
    for hand in min_set:
        color,num = hand
        result *= num
    return result


list_min_set = []
rlist = []
games = parse_lines('./input.txt')
#print(games)
for game in games:
    list_min_set.append(max_colors(games[game]))
#print(list_min_set)
for min_set in list_min_set:
    rlist.append(compute_min_set_power(min_set))

print(rlist)
print(sum(rlist))






#input = [line1,"lin2"]
