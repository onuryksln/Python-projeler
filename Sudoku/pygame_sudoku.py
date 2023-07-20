import sys, pygame as pg
import random
import time

#(26, 117, 255) yazı rengi
    
pg.init()

height = 750
width = 960
screen_size = width,height
#screen_size1 = 1080,750
sayac_ekran = 0
count_first = 0
# screen = pg.display.set_mode(screen_size,pg.FULLSCREEN) # fullscreen
screen = pg.display.set_mode(screen_size)

font = pg.font.SysFont(None, 80)

pg.display.set_caption('SUDOKU')
#Icon_name = pg.image.load('sudoku_icon.png')
#pg.display.set_icon(Icon_name)


number_grid_first = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
number_grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
number_grid_original = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]

x_x = 0
y_y = 0
dif = (750-30) / 9 # dif = 80
val = 0
flag1 = 0
flag2 = 0
font1 = pg.font.SysFont("comicsans", 40)
font2 = pg.font.SysFont("comicsans", 20)

sudoku_cesitleri = []
def dosya_okuma_map():
    global sudoku_cesitleri
    satir_tut = []
    with open("sudoku_harita.txt", 'r') as dosya:
        count = 0
        for satir in dosya:
            count += 1
    with open("sudoku_harita.txt", 'r') as dosya:
        count1 = 0
        satir = ""
        for satir in dosya:
            count1 += 1
            satir=satir.rstrip()
            satir_tut.append(satir)
            if str(satir) == '' or count == count1 :
                sudoku_cesitleri.append(satir_tut)
                satir_tut = []       
        #print(count)
    #for x in range(len(sudoku_cesitleri)):
    #    for y in range(len(sudoku_cesitleri[x])):
    #        print(sudoku_cesitleri[x][y])
            
def map_choose(difficulty):
    # dosyadan map secme islemleri
    choice_map1 = random.choice(sudoku_cesitleri)
    a = 0
    choice_map = []
    for x in choice_map1:
        satir = []
        for y in x:
            try:
                a = int(y)
            except:
                a = 0
            if a != 0:
                satir.append(a)
        if len(satir) != 0:
            choice_map.append(satir)
    #print('\n son hal \n')
    #for x in range(len(choice_map)):
    #    print(choice_map[x])
    # choice_map de sudoku haritasi secildi numaraların nerde olucagı belirli

    # number_grid_original da choice_map i yükleme
    for x in range(len(choice_map)):
        for y in range(len(choice_map[x])):
            number_grid_original[x][y] = choice_map[x][y]
    #----------------------------------------
    # zorluk belirleme işlemleri
    for x in range(0, 9):
        listeb = []
        for y in range(0, 9):
            # listeb.append(str(x)+','+str(y))
            listeb.append(x * 10 + y)
        #print(listeb)

    #print('\n\n')
    boxxc = []
    for z in range(30, 91, 30):
        listeb = []
        t = z - 30
        for c in range(t, t + 9, 3):
            listeb = []
            for y in range(c, z, 10):
                for x in range(y, y + 3):
                    listeb.append(x)
            boxxc.append(listeb)
            #print(listeb)
            
    if difficulty == "easy":
        # 34 ile 44 arası kutu verilecek
        # her karede en az 2 tane sayi verilmiş olucak en çok 6 tane olucak
        liste_given_location = []
        listeb_secim_sayilari = [2,3,3,4,4,4,4,4,6,6,6,6] # min 34 - max 44
        hide2 = len(boxxc)
        for y in range(hide2):
            if len(boxxc) != 0:
                choice_mapp2 = random.choice(boxxc)
                choice_mapp_number = 0
                choice_mapp_number = random.choice(listeb_secim_sayilari)
                if choice_mapp_number != 0:
                    for x in range(choice_mapp_number):
                        hide1 = random.choice(choice_mapp2)
                        liste_given_location.append(hide1)
                        choice_mapp2.remove(hide1)  
                    boxxc.remove(choice_mapp2)
                    listeb_secim_sayilari.remove(choice_mapp_number)
        #print('liste_given_location ',liste_given_location)
        # konum indis adresleri liste_given_location da tutuluyor.
        # tutlan adresler onlar basamagı x birler basamagı y olucak formda
        for z in liste_given_location:
            x = int(z/10)
            y = int(z%10)
            number_grid[x][y] = number_grid_original[x][y]
            number_grid_first[x][y] = number_grid_original[x][y]
        # ekran gösterme kontrol amaclı
        print('\nnumber_grid_original\n')
        for c in range(len(number_grid_original)):
            print(number_grid_original[c])
        print('\n')
        print('\nnumber_grid_first\n')
        for c in range(len(number_grid_first)):
            print(number_grid_first[c])
        print('\n')
        print('\nnumber_grid\n')
        for c in range(len(number_grid)):
            print(number_grid[c])
        print('\n')
    if difficulty == "normal":
        # 28 ile 36 arası kutu verilecek
        # her karede en az 2 tane sayi verilmiş olucak en çok 6 tane olucak
        liste_given_location = []
        listeb_secim_sayilari = [2,2,3,3,3,3,4,4,4,4,5,6] # min 28 - max 36
        hide2 = len(boxxc)
        for y in range(hide2):
            if len(boxxc) != 0:
                choice_mapp2 = random.choice(boxxc)
                choice_mapp_number = 0
                choice_mapp_number = random.choice(listeb_secim_sayilari)
                if choice_mapp_number != 0:
                    for x in range(choice_mapp_number):
                        hide1 = random.choice(choice_mapp2)
                        liste_given_location.append(hide1)
                        choice_mapp2.remove(hide1)  
                    boxxc.remove(choice_mapp2)
                    listeb_secim_sayilari.remove(choice_mapp_number)
        #print('liste_given_location ',liste_given_location)
        # konum indis adresleri liste_given_location da tutuluyor.
        # tutlan adresler onlar basamagı x birler basamagı y olucak formda
        for z in liste_given_location:
            x = int(z/10)
            y = int(z%10)
            number_grid[x][y] = number_grid_original[x][y]
            number_grid_first[x][y] = number_grid_original[x][y]
        # ekran gösterme kontrol amaclı
        print('\nnumber_grid_original\n')
        for c in range(len(number_grid_original)):
            print(number_grid_original[c])
        print('\n')
        print('\nnumber_grid_first\n')
        for c in range(len(number_grid_first)):
            print(number_grid_first[c])
        print('\n')
        print('\nnumber_grid\n')
        for c in range(len(number_grid)):
            print(number_grid[c])
        print('\n')
    if difficulty == "hard":
        # 22 ile 36 arası kutu verilecek
        # her karede en az 2 tane sayi verilmiş olucak en çok 6 tane olucak
        liste_given_location = []
        listeb_secim_sayilari = [2,2,2,2,2,3,3,3,3,3,4,5] # min 22 - max 28
        hide2 = len(boxxc)
        for y in range(hide2):
            if len(boxxc) != 0:
                choice_mapp2 = random.choice(boxxc)
                choice_mapp_number = 0
                choice_mapp_number = random.choice(listeb_secim_sayilari)
                if choice_mapp_number != 0:
                    for x in range(choice_mapp_number):
                        hide1 = random.choice(choice_mapp2)
                        liste_given_location.append(hide1)
                        choice_mapp2.remove(hide1)  
                    boxxc.remove(choice_mapp2)
                    listeb_secim_sayilari.remove(choice_mapp_number)
        #print('liste_given_location ',liste_given_location)
        # konum indis adresleri liste_given_location da tutuluyor.
        # tutlan adresler onlar basamagı x birler basamagı y olucak formda
        for z in liste_given_location:
            x = int(z/10)
            y = int(z%10)
            number_grid[x][y] = number_grid_original[x][y]
            number_grid_first[x][y] = number_grid_original[x][y]
        # ekran gösterme kontrol amaclı
        print('\nnumber_grid_original\n')
        for c in range(len(number_grid_original)):
            print(number_grid_original[c])
        print('\n')
        print('\nnumber_grid_first\n')
        for c in range(len(number_grid_first)):
            print(number_grid_first[c])
        print('\n')
        print('\nnumber_grid\n')
        for c in range(len(number_grid)):
            print(number_grid[c])
        print('\n')
        
def get_cord(pos):
    global x_x
    x_x = pos[0]//dif
    global y_y
    y_y = pos[1]//dif

# Highlight the cell selected
# kırmızı kutu gösterme
def draw_box():
    global x_x,y_y
    if x_x > 8:
        x_x = 0
    if y_y > 8:
        y_y = 0
    if x_x < 0:
        x_x = 8
    if y_y < 0:
        y_y = 8
    for i in range(2):
        #pg.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 5)
        #pg.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 5)

        #pg.draw.line(screen, (255, 0, 0), ( (x_x+i)*dif+15, (y_y)*dif+15 ), ( (x_x+i)*dif+15, (y_y+1)*dif+15 ), 5) # dikey
        #pg.draw.line(screen, (255, 0, 0), ( (x_x)*dif+15, (y_y+i)*dif+15 ), ( (x_x+1)*dif+15, (y_y+i)*dif+15 ), 5) # yatay
            
        pg.draw.line(screen, (255, 0, 0), ( (x_x+i)*dif+15, (y_y)*dif+15 ), ( (x_x+i)*dif+15, (y_y+1)*dif+15 ), 5) # dikey
        pg.draw.line(screen, (255, 0, 0), ( (x_x)*dif+15, (y_y+i)*dif+15 ), ( (x_x+1)*dif+15, (y_y+i)*dif+15 ), 5) # yatay
    #print(x,y)

def draw_background():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"),pg.Rect(15,15,720,720),10)
    # çizgi çizcez 720 /9 = 80 eder pixelde çalışılıyor.
    i = 1
    while (i*dif)<720:
        line_width = 5 if i % 3 > 0 else 10
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i*dif)+15,15),pg.Vector2((i*dif)+15,735),line_width) # dikey
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15,(i*dif)+15),pg.Vector2(735,(i*dif)+15),line_width) #yatay
        i += 1

def draw_numbers():
    row = 0
    offset = 35
    while row < 9:
        col = 0
        while col < 9:
            if number_grid_first[row][col] !=0:
                output = number_grid_first[row][col]
                n_text = font.render(str(output), True, pg.Color('black'))
                screen.blit(n_text, pg.Vector2((col*80) + offset+4,(row*80) + offset-3))
            elif number_grid[row][col] != 0:
                output = number_grid[row][col]
                n_text = font.render(str(output), True, pg.Color(204, 102, 153)) #red
                screen.blit(n_text, pg.Vector2((col*80) + offset+4,(row*80) + offset-3))
            col += 1
        row += 1
    
# Fill value entered in cell
# secili kutuya deger gir
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x_x * dif + 15, y_y * dif + 15))

def clear_matris():
    global number_grid_first,number_grid,number_grid_original
    number_grid_first = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
        ]
    number_grid = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
        ]
    number_grid_original = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
        ]    
def first_matris(): # kontrol edilecek
    global number_grid
    number_grid = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
        ]
    

def game_loop():
    global flag1,flag2,flag3,x_x,y_y,val
    global sayac_ekran,screen,count_first,difficulty,saat1,dk1,sn1
    # new game and ekran temizle
    font = pg.font.SysFont(None, 50)
    surf_again = font.render('New Game',True,(26, 117, 255))
    button_again = pg.Rect( int(width*94/120), int(height*88/100),200, 40)
    surf_clear = font.render('Clear ',True,(26, 117, 255))
    button_clear = pg.Rect( int(width*94/120), int(height*78/100),200, 40) 
    font = pg.font.SysFont(None, 80)
    
    if count_first == 0: # tek sefer yapılacak işlemler
        flag3 = 1
        count_first += 1
        zaman1 = time.strftime('%X')
        saat1 = zaman1[0]+zaman1[1]
        dk1 = zaman1[3]+zaman1[4]
        sn1 = zaman1[6]+zaman1[7]

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            flag1 = 1
            flag2 = 0
            pos = pg.mouse.get_pos()
            get_cord(pos)
            if pos[0] >= 735 or pos[0] <= 15 :
                flag3 = 0
            else:
                flag3 = 1
            print(pos)
            if button_again.collidepoint(event.pos): #ekranda tasarlanan tus basılması
                difficulty = "emty"
                clear_matris()
            if button_clear.collidepoint(event.pos):
                first_matris()
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_x-= 1
                flag1 = 1
                flag3 = 1
            if event.key == pg.K_RIGHT:
                x_x+= 1
                flag1 = 1
                flag3 = 1
            if event.key == pg.K_UP:
                y_y-= 1
                flag1 = 1
                flag3 = 1
            if event.key == pg.K_DOWN:
                y_y+= 1
                flag1 = 1
                flag3 = 1
            if event.key == pg.K_1:
                if flag3 == 1:
                    val = 1
            if event.key == pg.K_2:
                if flag3 == 1:
                    val = 2   
            if event.key == pg.K_3:
                if flag3 == 1:
                    val = 3
            if event.key == pg.K_4:
                if flag3 == 1:
                    val = 4
            if event.key == pg.K_5:
                if flag3 == 1:
                    val = 5
            if event.key == pg.K_6:
                if flag3 == 1:
                    val = 6
            if event.key == pg.K_7:
                if flag3 == 1:
                    val = 7
            if event.key == pg.K_8:
                if flag3 == 1:
                    val = 8
            if event.key == pg.K_9:
                if flag3 == 1:
                    val = 9 
            if event.key == pg.K_RETURN:
                flag2 = 1
                
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_F10:
                sayac_ekran += 1
                if sayac_ekran%2 == 1:
                    screen = pg.display.set_mode(screen_size,pg.FULLSCREEN)
                    #screen = pg.display.set_mode(screen_size1)
                if sayac_ekran%2 == 0:
                    screen = pg.display.set_mode(screen_size) 
    
    if val != 0:
        print('val',val)
        #draw_val(val)
        #print("val  number_grid kayit adresi --- ",x_x,y_y)
        number_grid[int(y_y)][int(x_x)]= val
        flag1 = 0
        #number_grid[int(x)][int(y)]= 0
        val = 0
        #for t in range(9):
        #    print(number_grid[t])
        kontrol_mappp = []
        hide3 = -1
        for x in number_grid:
            for y in x:
                kontrol_mappp.append(y)
        hide3 = kontrol_mappp.count(0)
        if hide3 == 0: # tablo dolduruldu dogrumu diye bak
            for x in range(len(number_grid_first)):
                for y in range(len(number_grid_first)):
                    if number_grid_first[x][y] != 0:
                        number_grid[x][y] = number_grid_first[x][y]
            error1 = 0
            for y in range(len(number_grid_original)):
                for z in range(len(number_grid_original)): 
                    if number_grid_original[y][z] != number_grid[y][z]:
                        error1 += 1
            if error1 == 0:
                print('Hepsi Dogru.')
                difficulty = "emty"
                clear_matris()
            else:
                print('Hatalı Çözüm')
            print('\nNew number_grid\n')
            for c in range(len(number_grid)):
                print(number_grid[c])
            print('\n')

    draw_background()
    if flag1 == 1 and flag3 == 1:
        draw_box()
    draw_numbers()
    
    font = pg.font.SysFont(None, 40)
    text = font.render(difficulty+' mode', True, (26, 117, 255))  # text = font.render('GeeksForGeeks', True, green, blue) blue arka plan
    textRect = text.get_rect()
    textRect.center = (int(width*88/100), int(height*8/100))
    screen.blit(text, textRect)
    font = pg.font.SysFont(None, 80)
    
    a,b = pg.mouse.get_pos()
    # new game
    if button_again.x <= a <= button_again.x + 200 and button_again.y <= b <= button_again.y + 40:
        pg.draw.rect(screen,(77, 255, 77),button_again)
        screen.blit(surf_again,(button_again.x + 10, button_again.y + 5)) 
    else:
        pg.draw.rect(screen,('white'),button_again) # (204, 255, 230)   (153, 235, 255)
        screen.blit(surf_again,(button_again.x + 10, button_again.y + 5))
    # ekrani temizleme
    if button_clear.x <= a <= button_clear.x + 200 and button_clear.y <= b <= button_clear.y + 40:
        pg.draw.rect(screen,(77, 255, 77),button_clear)
        screen.blit(surf_clear,(button_clear.x + 10, button_clear.y + 5)) 
    else:
        pg.draw.rect(screen,('white'),button_clear) # (204, 255, 230)   (153, 235, 255)
        screen.blit(surf_clear,(button_clear.x + 10, button_clear.y + 5)) 

    zaman2 = time.strftime('%X')
    saat2 = zaman2[0]+zaman2[1]
    dk2 = zaman2[3]+zaman2[4]
    sn2 = zaman2[6]+zaman2[7]
    sure = ( ( float(saat2) - float(saat1) )*60*60 ) + ( (float(dk2) - float(dk1))*60 ) + (float(sn2) - float(sn1))
    saat3 = 0
    dk3 = 0
    sn3 = 0
    if sure >= 60:
        saat3 = int(sure/3600)
        dk3 = int((sure%3600)/60)
        sn3 = int(sure)%60
    else:
        sn3 = int(sure)%60
    sure_str = str(saat3)+':'+str(dk3)+':'+str(sn3)
    font = pg.font.SysFont(None, 40)
    #text = font.render(' Süre '+str(sure), True, (26, 117, 255))
    text = font.render(' Süre ', True, (26, 117, 255))  
    textRect = text.get_rect()
    textRect.center = (int(width*88/100), int(height*20/100))
    screen.blit(text, textRect)
    text = font.render(sure_str, True, (26, 117, 255))
    textRect.center = (int(width*90/100), int(height*27/100))
    screen.blit(text, textRect)
    font = pg.font.SysFont(None, 80)
    
    pg.display.update()
    



def difficulty_options():
    difficulty = "emty"
    screen.fill(pg.Color("white"))
    surf_easy = font.render(' Easy ',True,'black')
    surf_normal = font.render(' Normal ',True,'black')
    surf_difficult = font.render(' Difficult ',True,'black')
    button_easy = pg.Rect( int(width*6/20), int(height/6), 320, 80) # ilk iki basşangıc konumu son iki en boy
    button_normal = pg.Rect( int(width*6/20), int(height/6)+150,320, 80)
    button_difficult = pg.Rect( int(width*6/20), int(height/6)+300, 320, 80)
    for events in pg.event.get():
        if events.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if events.type == pg.MOUSEBUTTONDOWN:
            if button_easy.collidepoint(events.pos):
                difficulty = "easy"
            if button_normal.collidepoint(events.pos):
                difficulty = "normal"
            if button_difficult.collidepoint(events.pos):
                difficulty = "hard"
    a,b = pg.mouse.get_pos()
    if button_easy.x <= a <= button_easy.x + 320 and button_easy.y <= b <= button_easy.y + 80:
        pg.draw.rect(screen,(77, 255, 77),button_easy)
        screen.blit(surf_easy,(button_easy.x + 70, button_easy.y + 15))
    else:
        pg.draw.rect(screen,(153, 235, 255),button_easy)
        screen.blit(surf_easy,(button_easy.x + 70, button_easy.y + 15))

    if button_normal.x <= a <= button_normal.x + 320 and button_normal.y <= b <= button_normal.y + 80:
        pg.draw.rect(screen,(77, 255, 77),button_normal)
        screen.blit(surf_normal,(button_normal.x + 40, button_normal.y + 15))
    else:
        pg.draw.rect(screen,(153, 235, 255),button_normal)
        screen.blit(surf_normal,(button_normal.x + 40, button_normal.y + 15))

    if button_difficult.x <= a <= button_difficult.x + 320 and button_difficult.y <= b <= button_difficult.y + 80:
        pg.draw.rect(screen,(77, 255, 77),button_difficult)
        screen.blit(surf_difficult,(button_difficult.x + 40, button_difficult.y + 15))
    else:
        pg.draw.rect(screen,(153, 235, 255),button_difficult)
        screen.blit(surf_difficult,(button_difficult.x + 40, button_difficult.y + 15))
    pg.display.update()
    #print(difficulty)
    return difficulty



difficulty = "emty"
dosya_okuma_map()
#map_choose(difficulty)
while 1:
    if difficulty == "emty":
        difficulty = difficulty_options()
        map_choose(difficulty)
        count_first = 0
    if difficulty != "emty":
        game_loop()




