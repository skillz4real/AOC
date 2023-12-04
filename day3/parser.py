def parse_lines(file):
    with open (file, 'r') as f:
        lines = f.readlines()
        return lines

def tracker(lines):
    """track 3 lines at the time and keep the next and the previous values in tmp variables"""
    rlist = []
    for i,line in enumerate(lines):
        #print(f"{i} : {line}")
        for j,char in enumerate(line):
            #edge cases
            if char.isdigit():
                if i == 0 and j == 0: #top left

                    if not lines[i][j+1].isdigit() and lines[i][j+1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j].isdigit() and lines[i+1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j+1].isdigit() and lines[i+1][j+1] != '.':
                        rlist.append((char,i,j))
                    else:
                        pass
    
                elif j == 0 and i == len(lines)-1: #bottom left
                    
                    if not lines[i][j+1].isdigit() and lines[i][j+1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j].isdigit() and lines[i-1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j+1].isdigit() and lines[i-1][j+1] != '.':
                        rlist.append((char,i,j))
                    else:
                        pass

                elif i == len(lines)-1 and j == len(line)-1: #bottom right
                    
                    if not lines[i][j-1].isdigit() and lines[i][j-1] != '.':
                        rlist.append((char,i,j)) 
                    elif not lines[i-1][j].isdigit() and lines[i-1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j-1].isdigit() and lines[i-1][j-1] != '.':
                        rlist.append((char,i,j))
                    else:
                        pass

                elif i == 0 and j == len(line)-1:   #top right
                    
                    if not lines[i][j-1].isdigit() and lines[i][j-1] != '.':
                        rlist.append((char,i,j)) 
                    elif not lines[i+1][j].isdigit() and lines[i+1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j-1].isdigit() and lines[i+1][j-1] != '.':
                        rlist.append((char,i,j))
                    else:
                        pass

                elif j == len(line) - 1:
                    if not lines[i][j-1].isdigit() and lines[i][j-1] != '.':
                        rlist.append((char,i,j)) 
                    elif not lines[i-1][j].isdigit() and lines[i-1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j].isdigit() and lines[i+1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j-1].isdigit() and lines[i-1][j-1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j-1].isdigit() and lines[i+1][j-1] != '.':
                        rlist.append((char,i,j))
                    else:
                        pass
                    
                elif j == 0:
                    if not lines[i][j+1].isdigit() and lines[i][j+1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j].isdigit() and lines[i-1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j].isdigit() and lines[i+1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j+1].isdigit() and lines[i-1][j+1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j+1].isdigit() and lines[i+1][j+1] != '.':
                        rlist.append((char,i,j))
                    else:
                        pass
                    
                elif i == 0:
                    if not lines[i][j-1].isdigit() and lines[i][j-1] != '.':
                        rlist.append((char,i,j)) 
                    elif not lines[i][j+1].isdigit() and lines[i][j+1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j].isdigit() and lines[i+1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j-1].isdigit() and lines[i+1][j-1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j+1].isdigit() and lines[i+1][j+1] != '.':
                        rlist.append((char,i,j))
                    else:
                        pass
                    
                elif i == len(lines)-1:
                    if not lines[i][j-1].isdigit() and lines[i][j-1] != '.':
                        rlist.append((char,i,j)) 
                    elif not lines[i][j+1].isdigit() and lines[i][j+1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j].isdigit() and lines[i-1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j-1].isdigit() and lines[i-1][j-1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j+1].isdigit() and lines[i-1][j+1] != '.':
                        rlist.append((char,i,j))
                    else:
                        pass
            
                else:   #normal cases         
                    if not lines[i][j-1].isdigit() and lines[i][j-1] != '.':
                        rlist.append((char,i,j)) 
                    elif not lines[i][j+1].isdigit() and lines[i][j+1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j].isdigit() and lines[i-1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j].isdigit() and lines[i+1][j] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j-1].isdigit() and lines[i-1][j-1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j-1].isdigit() and lines[i+1][j-1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i-1][j+1].isdigit() and lines[i-1][j+1] != '.':
                        rlist.append((char,i,j))
                    elif not lines[i+1][j+1].isdigit() and lines[i+1][j+1] != '.':
                        rlist.append((char,i,j))
                    else:
                        pass
    return rlist

def get_full_num(l:list, raw:list[list])-> list:
    rlist = []
    for t in l:
        lead,y,x = t
        llead = ""
        rlead = ""
        #if raw[y][x] == lead:
            #print("Working well")
        #else:
        #    print("U made a mistake")
        while raw[y][x].isdigit():
            rlead += raw[y][x]
            x+=1
        lead,_,x = t
        while raw[y][x].isdigit():
            llead += raw[y][x]
            x-=1
        full_num = llead[::-1] + rlead[1:]
        rlist.append((int(full_num),x,y))
    return rlist

def clean_data(l:list)->list:
    return list(set(l))


if __name__ == "__main__":
    data = parse_lines('./input.txt')
    
    #print(tracker(data))

    get_full_num(tracker(data),data)


    res = get_full_num(tracker(data),data)
    
    print(clean_data(res))
    #print(sum(res)) 
