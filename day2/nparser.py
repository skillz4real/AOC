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



print(parse_lines('./input.txt'))
