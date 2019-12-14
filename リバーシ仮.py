import copy

lst = [[' ','a','b','c','d','e','f','g','h',' '],
       ['1',' ',' ',' ',' ',' ',' ',' ',' ','1'],
       ['2',' ',' ',' ',' ',' ',' ',' ',' ','2'],
       ['3',' ',' ',' ',' ',' ',' ',' ',' ','3'],
       ['4',' ',' ',' ','O','X',' ',' ',' ','4'],
       ['5',' ',' ',' ','X','O',' ',' ',' ','5'],
       ['6',' ',' ',' ',' ',' ',' ',' ',' ','6'],
       ['7',' ',' ',' ',' ',' ',' ',' ',' ','7'],
       ['8',' ',' ',' ',' ',' ',' ',' ',' ','8'],
       [' ','a','b','c','d','e','f','g','h',' ']]

def hantei_migiue(y,x,lst,turn,flag):
    if lst[y][x] == ' ':
        count = 1
        if turn == 1:
            x += 1
            y -= 1
            if lst[y][x] == 'X':
                hamideru = 0
                while hamideru == 0:
                    count += 1
                    x += 1
                    y -= 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'O':
                            while count > 0:
                                lst[y][x] = 'O'
                                count -= 1
                                hamideru = 1
                                x -= 1
                                y += 1
                                flag = 1
                    else:
                        hamideru = 1
        else:
            x += 1
            y -= 1
            if lst[y][x] == 'O':
                hamideru = 0
                while hamideru == 0:
                    x += 1
                    y -= 1
                    count += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'X':
                            while count > 0:
                                lst[y][x] = 'X'
                                hamideru = 1
                                count -= 1
                                x -= 1
                                y += 1
                                flag = 1
                    else:
                        hamideru = 1
    return lst,flag

def hantei_migi(y,x,lst,turn,flag):
    if lst[y][x] == ' ':
        count = 1
        if turn == 1:
            x += 1
            if lst[y][x] == 'X':
                hamideru = 0
                while hamideru == 0:
                    count += 1
                    x += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'O':
                            while count > 0:
                                lst[y][x] = 'O'
                                count -= 1
                                hamideru = 1
                                x -= 1
                                flag = 1
                    else:
                        hamideru = 1
        else:
            x += 1
            if lst[y][x] == 'O':
                hamideru = 0
                while hamideru == 0:
                    x += 1
                    count += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'X':
                            while count > 0:
                                lst[y][x] = 'X'
                                count -= 1
                                hamideru = 1
                                x -= 1
                                flag = 1
                    else:
                        hamideru = 1
    return lst,flag

def hantei_migisita(y,x,lst,turn,flag):
    if lst[y][x] == ' ':
        count = 1
        if turn == 1:
            x += 1
            y += 1
            if lst[y][x] == 'X':
                hamideru = 0
                while hamideru == 0:
                    count += 1
                    x += 1
                    y += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'O':
                            while count > 0:
                                lst[y][x] = 'O'
                                count -= 1
                                hamideru = 1
                                x -= 1
                                y -= 1
                                flag = 1
                    else:
                        hamideru = 1
        else:
            x += 1
            y += 1
            if lst[y][x] == 'O':
                hamideru = 0
                while hamideru == 0:
                    x += 1
                    y += 1
                    count += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'X':
                            while count > 0:
                                lst[y][x] = 'X'
                                count -= 1
                                hamideru = 1
                                x -= 1
                                y -= 1
                                flag = 1
                    else:
                        hamideru = 1
    return lst,flag

def hantei_sita(y,x,lst,turn,flag):
    if lst[y][x] == ' ':
        count = 1
        if turn == 1:
            y += 1
            if lst[y][x] == 'X':
                hamideru = 0
                while hamideru == 0:
                    count += 1
                    y += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'O':
                            while count > 0:
                                lst[y][x] = 'O'
                                count -= 1
                                hamideru = 1
                                y -= 1
                                flag = 1
                    else:
                        hamideru = 1

        else:
            y += 1
            if lst[y][x] == 'O':
                hamideru = 0
                while hamideru == 0:
                    y += 1
                    count += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'X':
                            while count > 0:
                                lst[y][x] = 'X'
                                hamideru = 1
                                count -= 1
                                y -= 1
                                flag = 1
                    else:
                        hamideru = 1
    return lst,flag

def hantei_hidarisita(y,x,lst,turn,flag):
    if lst[y][x] == ' ':
        count = 1
        if turn == 1:
            x -= 1
            y += 1
            if lst[y][x] == 'X':
                hamideru = 0
                while hamideru == 0:
                    count += 1
                    x -= 1
                    y += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'O':
                            while count > 0:
                                lst[y][x] = 'O'
                                count -= 1
                                hamideru = 1
                                x += 1
                                y -= 1
                                flag = 1
                    else:
                        hamideru = 1
        else:
            x -= 1
            y += 1
            if lst[y][x] == 'O':
                hamideru = 0
                while hamideru == 0:
                    x -= 1
                    y += 1
                    count += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'X':
                            while count > 0:
                                lst[y][x] = 'X'
                                count -= 1
                                hamideru = 1
                                x += 1
                                y -= 1
                                flag = 1
                    else:
                        hamideru = 1
    return lst,flag

def hantei_hidari(y,x,lst,turn,flag):
    if lst[y][x] == ' ':
        count = 1
        if turn == 1:
            x -= 1
            if lst[y][x] == 'X':
                hamideru = 0
                while hamideru == 0:
                    count += 1
                    x -= 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'O':
                            while count > 0:
                                lst[y][x] = 'O'
                                count -= 1
                                hamideru = 1
                                x += 1
                                flag = 1
                    else:
                        hamideru = 1
        else:
            x -= 1
            if lst[y][x] == 'O':
                hamideru = 0
                while hamideru == 0:
                    x -= 1
                    count += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'X':
                            while count > 0:
                                lst[y][x] = 'X'
                                count -= 1
                                hamideru = 1
                                x += 1
                                flag = 1
                    else:
                        hamideru = 1
    return lst,flag

def hantei_hidariue(y,x,lst,turn,flag):
    if lst[y][x] == ' ':
        count = 1
        if turn == 1:
            x -= 1
            y -= 1
            if lst[y][x] == 'X':
                hamideru = 0
                while hamideru == 0:
                    count += 1
                    x -= 1
                    y -= 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'O':
                            while count > 0:
                                lst[y][x] = 'O'
                                count -= 1
                                hamideru = 1
                                x += 1
                                y += 1
                                flag = 1
                    else:
                        hamideru = 1
        else:
            x -= 1
            y -= 1
            if lst[y][x] == 'O':
                hamideru = 0
                while hamideru == 0:
                    x -= 1
                    y -= 1
                    count += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'X':
                            while count > 0:
                                lst[y][x] = 'X'
                                count -= 1
                                hamideru = 1
                                x += 1
                                y += 1
                                flag = 1
                    else:
                        hamideru = 1
    return lst,flag

def hantei_ue(y,x,lst,turn,flag):
    if lst[y][x] == ' ':
        count = 1
        if turn == 1:
            y -= 1
            if lst[y][x] == 'X':
                hamideru = 0
                while hamideru == 0:
                    count += 1
                    y -= 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'O':
                            while count > 0:
                                lst[y][x] = 'O'
                                count -= 1
                                hamideru = 1
                                y += 1
                                flag = 1
                    else:
                        hamideru = 1
        else:
            y -= 1
            if lst[y][x] == 'O':
                hamideru = 0
                while hamideru == 0:
                    y -= 1
                    count += 1
                    if lst[y][x] == 'O' or lst[y][x] == 'X':
                        if lst[y][x] == 'X':
                            while count > 0:
                                lst[y][x] = 'X'
                                count -= 1
                                hamideru = 1
                                y += 1
                                flag = 1
                    else:
                        hamideru = 1
    return lst,flag

def hantei(lst):
    P1 = 0
    P2 = 0
    for i in lst:
        for x in range(len(i)):
            if i[x] == 'O':
                P1 += 1
            if i[x] == 'X':
                P2 += 1
    return P1,P2

def error_decision(lst,turn,switch):
    x = 0
    y = 0
    try:
        if turn == 1:
            y,x = input('1Pのターン どこに置きますか？入力例1,a  ').split(',')
            if y + ',' + x not in arrangement_lst:
                switch = 1
                print('そこには置けません')
        else:
            y,x = input('2Pのターン どこに置きますか？入力例1,a  ').split(',')
            if y + ',' + x not in arrangement_lst:
                switch = 1
                print('そこには置けません')
        y = int(y)
        if x == 'a':
            x = 1
        elif x == 'b':
            x = 2
        elif x == 'c':
            x = 3
        elif x == 'd':
            x = 4
        elif x == 'e':
            x = 5
        elif x == 'f':
            x = 6
        elif x == 'g':
            x = 7
        elif x == 'h':
            x = 8
    except:
        print('入力値が間違っています')
        switch = 1
    return x,y,switch

def hantei_all(lst,turn):
    arrangement_lst = []
    for y in range(8):
        for x in range(8):
            flag = 0
            if turn == 1:
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_migiue(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_migi(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_migisita(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_sita(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_hidarisita(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_hidari(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_hidariue(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_ue(y+1,x+1,workbench,turn,flag)
                if flag == 1:
                    if x == 0:
                        index = 'a'
                    elif x == 1:
                        index = 'b'
                    elif x == 2:
                        index = 'c'
                    elif x == 3:
                        index = 'd'
                    elif x == 4:
                        index = 'e'
                    elif x == 5:
                        index = 'f'
                    elif x == 6:
                        index = 'g'
                    elif x == 7:
                        index = 'h'
                    workbench = str(y+1) + ',' + index
                    arrangement_lst.append(workbench)
            else:
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_migiue(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_migi(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_migisita(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_sita(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_hidarisita(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_hidari(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_hidariue(y+1,x+1,workbench,turn,flag)
                workbench = copy.deepcopy(lst)
                workbench,flag = hantei_ue(y+1,x+1,workbench,turn,flag)
                if flag == 1:
                    if x == 0:
                        index = 'a'
                    elif x == 1:
                        index = 'b'
                    elif x == 2:
                        index = 'c'
                    elif x == 3:
                        index = 'd'
                    elif x == 4:
                        index = 'e'
                    elif x == 5:
                        index = 'f'
                    elif x == 6:
                        index = 'g'
                    elif x == 7:
                        index = 'h'
                    workbench = str(y+1) + ',' + index
                    arrangement_lst.append(workbench)
    return arrangement_lst

turn = 1
game = 0
flag = 0
num_1 = 0
num_2 = 0
end_condition = 0
print('1PがOで2PがXです')
while game == 0:
    for i in lst:   #盤の出力
        print(i)
    workbench = copy.deepcopy(lst)
    arrangement_lst = hantei_all(lst,turn)
    print('置ける場所は・・・')
    for i in arrangement_lst:
        print(i)
    if arrangement_lst == []:
        end_condition += 1
        turn += 1
        if end_condition == 2:
            game = 1
            break
        print('置ける場所がありません')
    flag = 0
    turn = turn % 2
    switch = 1
    if arrangement_lst != []:
        end_condition = 0
        if turn == 1:
            while switch == 1:
                switch = 0
                P1_x,P1_y,switch = error_decision(lst,turn,switch)
        else:
            while switch == 1:
                switch = 0
                P2_x,P2_y,switch = error_decision(lst,turn,switch)

        if turn == 1:
            lst,flag = hantei_migiue(P1_y,P1_x,lst,turn,flag)
            lst,flag = hantei_migi(P1_y,P1_x,lst,turn,flag)
            lst,flag = hantei_migisita(P1_y,P1_x,lst,turn,flag)
            lst,flag = hantei_sita(P1_y,P1_x,lst,turn,flag)
            lst,flag = hantei_hidarisita(P1_y,P1_x,lst,turn,flag)
            lst,flag = hantei_hidari(P1_y,P1_x,lst,turn,flag)
            lst,flag = hantei_hidariue(P1_y,P1_x,lst,turn,flag)
            lst,flag = hantei_ue(P1_y,P1_x,lst,turn,flag)
            if flag == 1:
                lst[P1_y][P1_x] = 'O'
                turn += 1
        else:
            lst,flag = hantei_migiue(P2_y,P2_x,lst,turn,flag)
            lst,flag = hantei_migi(P2_y,P2_x,lst,turn,flag)
            lst,flag = hantei_migisita(P2_y,P2_x,lst,turn,flag)
            lst,flag = hantei_sita(P2_y,P2_x,lst,turn,flag)
            lst,flag = hantei_hidarisita(P2_y,P2_x,lst,turn,flag)
            lst,flag = hantei_hidari(P2_y,P2_x,lst,turn,flag)
            lst,flag = hantei_hidariue(P2_y,P2_x,lst,turn,flag)
            lst,flag = hantei_ue(P2_y,P2_x,lst,turn,flag)
            if flag == 1:
                lst[P2_y][P2_x] = 'X'
                turn += 1

P1,P2 = hantei(lst)
print('ゲームを終了します！')
if P1 > P2:
    print('P1 =',P1,'対 P2 =',P2,'でP1の勝ち')
elif P1 == P2:
    p
    rint('P1 =',P1,'対 P2 =',P2,'で引き分け')
else:
    print('P1 =',P1,'対 P2 =',P2,'でP2の勝ち')
