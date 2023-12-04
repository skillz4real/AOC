
def highlight_digits(word:str):
    valid_digits = {"one": '1', "two": '2', "three": '3', "four": '4',"five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    for d in valid_digits.keys():
        if d in word:
            tmp = word.split(d)
            tmp2 = d.replace(d[0],f"{d[0]}{valid_digits.get(d)}",-1)
            word = tmp2.join(tmp)
    return word


def strip_letters(word:str):
    r = ""
    for char in word:
        if char.isdigit():
            r += char
    return r

with open('raw.txt', 'r') as f:
    l = f.readlines()
    #print(l)
    for i,s in enumerate(l):
        s = highlight_digits(s)
        s = strip_letters(s)
        #print(s)
        print(f"{l[i]}:       {s}")
        #print (f"{l[i]}            {int(s[0] + s[-1])}")
        l[i] = int(s[0] + s[-1])

#print(l)
#print(len(l))
result = sum(l)
print(f"result: {result}")
#"""
