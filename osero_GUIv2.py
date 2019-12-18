import pygame
import sys
from pygame.locals import *
import copy
import multiprocessing


WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,51,0)
BLUE = (0,102,255)

def hantei_migiue(y,x,lst,turn,flag):
    if lst[y][x] == ' ':
        count = 0
        if turn == 1:
            if lst[y-1][x+1] == 'X':
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
            if lst[y-1][x+1] == 'O':
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
        count = 0
        if turn == 1:
            if lst[y][x+1] == 'X':
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
            if lst[y][x+1] == 'O':
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
        count = 0
        if turn == 1:
            if lst[y+1][x+1] == 'X':
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
            if lst[y+1][x+1] == 'O':
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
        count = 0
        if turn == 1:
            if lst[y+1][x] == 'X':
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
            if lst[y+1][x] == 'O':
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
        count = 0
        if turn == 1:
            if lst[y+1][x-1] == 'X':
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
            if lst[y+1][x-1] == 'O':
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
        count = 0
        if turn == 1:
            if lst[y][x-1] == 'X':
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
            if lst[y][x-1] == 'O':
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
        count = 0
        if turn == 1:
            if lst[y-1][x-1] == 'X':
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
            if lst[y-1][x-1] == 'O':
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
        count = 0
        if turn == 1:
            if lst[y-1][x] == 'X':
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
            if lst[y-1][x] == 'O':
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

def error_decision(arrangement_lst,mouseX,mouseY,turn,pygame):
    x = 10
    y = 10
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            selectionX,selectionY = mouseX,mouseY
            if selectionX > 650 and selectionX < 700 :
                if selectionY > 50 and selectionY < 100:
                    x = 1
                    y = 1
                elif selectionY > 100 and selectionY < 150:
                    x = 1
                    y = 2
                elif selectionY > 150 and selectionY < 200:
                    x = 1
                    y = 3
                elif selectionY > 200 and selectionY < 250:
                    x = 1
                    y = 4
                elif selectionY > 250 and selectionY < 300:
                    x = 1
                    y = 5
                elif selectionY > 300 and selectionY < 350:
                    x = 1
                    y = 6
                elif selectionY > 350 and selectionY < 400:
                    x = 1
                    y = 7
                elif selectionY > 400 and selectionY < 450:
                    x = 1
                    y = 8
            elif selectionX > 700 and selectionX < 750 :
                if selectionY > 50 and selectionY < 100:
                    x = 2
                    y = 1
                elif selectionY > 100 and selectionY < 150:
                    x = 2
                    y = 2
                elif selectionY > 150 and selectionY < 200:
                    x = 2
                    y = 3
                elif selectionY > 200 and selectionY < 250:
                    x = 2
                    y = 4
                elif selectionY > 250 and selectionY < 300:
                    x = 2
                    y = 5
                elif selectionY > 300 and selectionY < 350:
                    x = 2
                    y = 6
                elif selectionY > 350 and selectionY < 400:
                    x = 2
                    y = 7
                elif selectionY > 400 and selectionY < 450:
                    x = 2
                    y = 8
            elif selectionX > 750 and selectionX < 800 :
                if selectionY > 50 and selectionY < 100:
                    x = 3
                    y = 1
                elif selectionY > 100 and selectionY < 150:
                    x = 3
                    y = 2
                elif selectionY > 150 and selectionY < 200:
                    x = 3
                    y = 3
                elif selectionY > 200 and selectionY < 250:
                    x = 3
                    y = 4
                elif selectionY > 250 and selectionY < 300:
                    x = 3
                    y = 5
                elif selectionY > 300 and selectionY < 350:
                    x = 3
                    y = 6
                elif selectionY > 350 and selectionY < 400:
                    x = 3
                    y = 7
                elif selectionY > 400 and selectionY < 450:
                    x = 3
                    y = 8
            elif selectionX > 800 and selectionX < 850 :
                if selectionY > 50 and selectionY < 100:
                    x = 4
                    y = 1
                elif selectionY > 100 and selectionY < 150:
                    x = 4
                    y = 2
                elif selectionY > 150 and selectionY < 200:
                    x = 4
                    y = 3
                elif selectionY > 200 and selectionY < 250:
                    x = 4
                    y = 4
                elif selectionY > 250 and selectionY < 300:
                    x = 4
                    y = 5
                elif selectionY > 300 and selectionY < 350:
                    x = 4
                    y = 6
                elif selectionY > 350 and selectionY < 400:
                    x = 4
                    y = 7
                elif selectionY > 400 and selectionY < 450:
                    x = 4
                    y = 8
            elif selectionX > 850 and selectionX < 900 :
                if selectionY > 50 and selectionY < 100:
                    x = 5
                    y = 1
                elif selectionY > 100 and selectionY < 150:
                    x = 5
                    y = 2
                elif selectionY > 150 and selectionY < 200:
                    x = 5
                    y = 3
                elif selectionY > 200 and selectionY < 250:
                    x = 5
                    y = 4
                elif selectionY > 250 and selectionY < 300:
                    x = 5
                    y = 5
                elif selectionY > 300 and selectionY < 350:
                    x = 5
                    y = 6
                elif selectionY > 350 and selectionY < 400:
                    x = 5
                    y = 7
                elif selectionY > 400 and selectionY < 450:
                    x = 5
                    y = 8
            elif selectionX >900 and selectionX < 950 :
                if selectionY > 50 and selectionY < 100:
                    x = 6
                    y = 1
                elif selectionY > 100 and selectionY < 150:
                    x = 6
                    y = 2
                elif selectionY > 150 and selectionY < 200:
                    x = 6
                    y = 3
                elif selectionY > 200 and selectionY < 250:
                    x = 6
                    y = 4
                elif selectionY > 250 and selectionY < 300:
                    x = 6
                    y = 5
                elif selectionY > 300 and selectionY < 350:
                    x = 6
                    y = 6
                elif selectionY > 350 and selectionY < 400:
                    x = 6
                    y = 7
                elif selectionY > 400 and selectionY < 450:
                    x = 6
                    y = 8
            elif selectionX > 950 and selectionX < 1000 :
                if selectionY > 50 and selectionY < 100:
                    x = 7
                    y = 1
                elif selectionY > 100 and selectionY < 150:
                    x = 7
                    y = 2
                elif selectionY > 150 and selectionY < 200:
                    x = 7
                    y = 3
                elif selectionY > 200 and selectionY < 250:
                    x = 7
                    y = 4
                elif selectionY > 250 and selectionY < 300:
                    x = 7
                    y = 5
                elif selectionY > 300 and selectionY < 350:
                    x = 7
                    y = 6
                elif selectionY > 350 and selectionY < 400:
                    x = 7
                    y = 7
                elif selectionY > 400 and selectionY < 450:
                    x = 7
                    y = 8
            elif selectionX > 1000 and selectionX < 1050 :
                if selectionY > 50 and selectionY < 100:
                    x = 8
                    y = 1
                elif selectionY > 100 and selectionY < 150:
                    x = 8
                    y = 2
                elif selectionY > 150 and selectionY < 200:
                    x = 8
                    y = 3
                elif selectionY > 200 and selectionY < 250:
                    x = 8
                    y = 4
                elif selectionY > 250 and selectionY < 300:
                    x = 8
                    y = 5
                elif selectionY > 300 and selectionY < 350:
                    x = 8
                    y = 6
                elif selectionY > 350 and selectionY < 400:
                    x = 8
                    y = 7
                elif selectionY > 400 and selectionY < 450:
                    x = 8
                    y = 8

    return x,y

def hantei_all(lst,turn):
    arrangement_lst = []
    for y in range(8):
        for x in range(8):
            flag = 0
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
                workbench = str(y+1) + str(x+1)
                arrangement_lst.append(workbench)

    return arrangement_lst

def GUI_output(lst,screen):
    global WHITE,BLACK,GREEN
    for y in range(8):
        for x in range(8):
            if lst[y+1][x+1] == 'O':
                pygame.draw.circle(screen,WHITE,[50*x+675,50*y+75],20)
            elif lst[y+1][x+1] == 'X':
                pygame.draw.circle(screen,BLACK,[50*x+675,50*y+75],20)

def GUI_assist(okerubasyo_lst,screen,assist_img):
    for i in okerubasyo_lst:
        assist_y = str(i)[0]
        assist_x = str(i)[1]
        screen.blit(assist_img, (50*int(assist_x)+600,50*int(assist_y)))

def GUI_assist_kesi(okerubasyo_lst,screen,pygame):
    global GREEN
    for i in okerubasyo_lst:
        assist_y = str(i)[0]
        assist_x = str(i)[1]
        pygame.draw.rect(screen, GREEN, [50*int(assist_x)+600,50*int(assist_y),50,50])
        for y in range(8):
            for x in range(8):
                pygame.draw.rect(screen,BLACK, [50*(x+1)+600,50*(y+1),50,50],5)

def count(lst):
    P1 = 0
    P2 = 0
    for i in lst:
        for x in range(len(i)):
            if i[x] == 'O':
                P1 += 1
            if i[x] == 'X':
                P2 += 1
    return P1,P2

def end(queue):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

def main(screen):
    pygame.init()
    lst = [['N','N','N','N','N','N','N','N','N','N'],
           ['N',' ',' ',' ',' ',' ',' ',' ',' ','N'],
           ['N',' ',' ',' ',' ',' ',' ',' ',' ','N'],
           ['N',' ',' ',' ',' ',' ',' ',' ',' ','N'],
           ['N',' ',' ',' ','O','X',' ',' ',' ','N'],
           ['N',' ',' ',' ','X','O',' ',' ',' ','N'],
           ['N',' ',' ',' ',' ',' ',' ',' ',' ','N'],
           ['N',' ',' ',' ',' ',' ',' ',' ',' ','N'],
           ['N',' ',' ',' ',' ',' ',' ',' ',' ','N'],
           ['N','N','N','N','N','N','N','N','N','N']]

    tmr = 1
    turn = 1
    gameover = 0
    font1 = pygame.font.SysFont("hg正楷書体pro", 50)
    turn_1P = font1.render("1Pのターンです！", True, (0,0,0))
    turn_2P = font1.render("2Pのターンです！", True, (0,0,0))

    pygame.init()
    pygame.display.set_caption("お・せ・ろ")
    clock = pygame.time.Clock()

    # 盤つくり
    screen.fill(WHITE)
    ban = pygame.Rect(650,50,400,400)
    pygame.draw.rect(screen, BLACK, [630,30,440,440])
    pygame.draw.rect(screen, GREEN, ban)
    for y in range(8):
        for x in range(8):
            pygame.draw.rect(screen,BLACK, [50*(x+1)+600,50*(y+1),50,50],5)

    while True: #ゲーム開始
        girl_img = pygame.image.load("girl.png")
        assist_img = pygame.image.load("neko_cursor.png")
        assist_img = pygame.transform.scale(assist_img,(50,50))
        screen.blit(girl_img,(0,0))
        flag = 0
        mBtn1,mBtn2,mBtn3 = pygame.mouse.get_pressed() #マウスボタン
        tmr += 1
        for event in pygame.event.get(): #ゲーム終了
            if event.type == pygame.QUIT:
                owari = 1
                pygame.quit()
                sys.exit()
        okerubasyo_lst = hantei_all(lst,turn) #置ける場所リスト
        GUI_output(lst,screen)
        GUI_assist(okerubasyo_lst,screen,assist_img)

        pygame.draw.rect(screen,WHITE,[250,50,30,50])
        if turn == 1:
            screen.blit(turn_1P,(250,50))
        elif turn == 0:
            screen.blit(turn_2P,(250,50))

        mouseX,mouseY = pygame.mouse.get_pos()
        x,y = error_decision(lst,mouseX,mouseY,turn,pygame)
        yx = str(y)+str(x)
        if yx in okerubasyo_lst:
            pygame.draw.rect(screen, WHITE, [350,200,150,50])
            pygame.draw.rect(screen, WHITE, [350,250,150,50])
            GUI_assist_kesi(okerubasyo_lst,screen,pygame)
            lst,flag = hantei_migiue(y,x,lst,turn,flag)
            lst,flag = hantei_migi(y,x,lst,turn,flag)
            lst,flag = hantei_migisita(y,x,lst,turn,flag)
            lst,flag = hantei_sita(y,x,lst,turn,flag)
            lst,flag = hantei_hidari(y,x,lst,turn,flag)
            lst,flag = hantei_hidariue(y,x,lst,turn,flag)
            lst,flag = hantei_hidarisita(y,x,lst,turn,flag)
            lst,flag = hantei_ue(y,x,lst,turn,flag)
            if flag == 1:
                if turn % 2 == 1:
                    lst[y][x] = "O"
                    turn += 1
                    turn = turn % 2
                    gameover = 0
                else:
                    lst[y][x] = "X"
                    turn += 1
                    turn = turn % 2
                    gameover = 0
        elif okerubasyo_lst == []:
            turn = (turn + 1) % 2
            gameover += 1
        count_1P, count_2P = count(lst)
        if gameover == 2:
            pygame.draw.rect(screen,WHITE,[250,50,360,50])
            if count_1P > count_2P:
                result_text = font1.render("1Pの勝利", True, (0,0,0))
            else:
                result_text = font1.render("2Pの勝利", True, (0,0,0))
            screen.blit(result_text, (250, 50))
            break
        count_1P, count_2P = count(lst)
        pygame.draw.rect(screen, RED, [300,230,170,10])
        pygame.draw.rect(screen, BLUE, [300,280,170,10])
        text_1P = font1.render("1P："+str(count_1P), True, (0,0,0))
        text_2P = font1.render("2P："+str(count_2P), True, (0,0,0))
        screen.blit(text_1P,(300,200))
        screen.blit(text_2P,(300,250))
        pygame.display.update()
        clock.tick(10000)



if __name__ == "__main__":
    screen = pygame.display.set_mode((1100,600))
    global owari
    owari = 0
    main(screen)
    while True:
        if owari == 1:
            pygame.quit()
            sys.exit()
        retry = pygame.Rect(300, 400, 150, 100)
        pygame.draw.rect(screen, (192, 192, 192), retry)
        font = pygame.font.SysFont("hg正楷書体pro", 25)
        retry_text = font.render("もう一回", True, (0,0,0))
        screen.blit(retry_text, (320, 440))
        pygame.display.update()
        for event in pygame.event.get(): #ゲーム終了
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #リスタート
                if retry.collidepoint(event.pos):
                    pygame.draw.rect(screen, (255,255,255), retry)
                    pygame.draw.rect(screen,WHITE,[250,50,360,50])
                    main(screen)
