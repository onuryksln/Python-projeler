import sys, pygame as pg
import random
import time

#(26, 117, 255) yazı rengi
    
pg.init()

height = 768
width = 1024
screen_size = width,height

screen = pg.display.set_mode(screen_size)

font = pg.font.SysFont(None, 40)  # font = pg.font.SysFont(None, 80)

pg.display.set_caption('Snake')
Icon_name = pg.image.load('snake_icon.png')
pg.display.set_icon(Icon_name)

apple = pg.image.load('apple_icon.png')

snake1sol = pg.image.load('snake1sol_icon.png')
snake1sag = pg.image.load('snake1sag_icon.png')
snake1y = pg.image.load('snake1y_icon.png')
snake1a = pg.image.load('snake1a_icon.png')
snake2 = pg.image.load('snake2_icon.png')
snake3 = pg.image.load('snake3_icon.png')

wall = pg.image.load('wall_16.png')

#font1 = pg.font.SysFont("comicsans", 40)
#font2 = pg.font.SysFont("comicsans", 20)

sayac_ekran = 0
count_first = 0 #tek sefer çalışması için kontrolcu
# x_x ve y_y rasgele konumdan başlarsa 0.6 ile çarpılarak x ve y belirlenecek.
x_x = 0.6
y_y = 0.6
snake_size = 20
enemy_size = 20
wall_size = 20
c_memory_enemy_center = []
c_memory_enemy = []
c_memory_snake = []
score = 0
speed1 = 0.158  # snake hızı - başlangıc hızı 0.228 0.100 er düşererek hızlandır

count_pause = 0
pause = 0

flag1 = 0
flag2 = 0

snake_color_first = (255, 51, 0) 
snake_color_other = (204, 0, 0) 
enemy_color = (255, 128, 170)
wall_color = (102, 102, 102) 
background_color = (242, 242, 242)

zaman1 = time.strftime('%X')
saat1 = zaman1[0]+zaman1[1]
dk1 = zaman1[3]+zaman1[4]
sn1 = zaman1[6]+zaman1[7]
time_sn1 = int(saat1)*3600 + int(dk1)*60 + int(sn1)

def reset():
    global sayac_ekran, count_first, x_x, y_y, snake_size, enemy_size, flag1, flag2
    global c_memory_enemy, c_memory_snake, score, speed1, count_pause, pause
    sayac_ekran = 0
    count_first = 0 
    x_x = 0.6
    y_y = 0.6
    snake_size = 20
    enemy_size = 20
    c_memory_enemy = []
    c_memory_snake = []
    score = 0
    speed1 = 0.158 
    count_pause = 0
    pause = 0
    flag1 = 0
    flag2 = 0

def random_snake_location(): #50,37 sınır kare sayılari snake için
    global x_x, y_y
    ax = random.randint(0, int((width-20)/20)-1 )
    by = random.randint(0, int((height-20)/20)-1 )
    x_x = 0.6 + ax
    y_y = 0.6 + by
    #print('ax,by',int((width-20)/20),int((height-20)/20))
    
def random_enemy_location():
    global c_memory_enemy, time_enemy1, c_memory_enemy_center
    #min_x = 22 min_y = 22 max_x = 1002 max_y = 742
    # enemy sınırları
    c_memory_enemy = []
    #ax = random.randrange(22, int( 1002 ),20 )
    #by = random.randrange(22, int( 742 ),20 )
    ax = random.randint(0, int((width-20)/20)-1 )
    by = random.randint(0, int((height-20)/20)-1 )
    ax = ax + 0.6
    by = by + 0.6
    c_memory_enemy_center = []
    c_memory_enemy_center.append( (ax*20+(enemy_size/2)) )
    c_memory_enemy_center.append( (by*20+(enemy_size/2)) )
    c_memory_enemy.append(ax)
    c_memory_enemy.append(by)
    z_enemy1 = time.strftime('%X')
    saat_enemy1 = z_enemy1[0]+z_enemy1[1]
    dk_enemy1 = z_enemy1[3]+z_enemy1[4]
    sn_enemy1 = z_enemy1[6]+z_enemy1[7]
    time_enemy1 = int(saat_enemy1)*3600 + int(dk_enemy1)*60 + int(sn_enemy1)

def location_limited():
    global x_x,y_y,flag1
    if flag1 == 1:
        x_x-= 1
    elif flag1 == 2:
        x_x+= 1
    elif flag1 == 3:
        y_y-= 1
    elif flag1 == 4:
        y_y+= 1

"""    
    #otomatik oynama kısmı silinecek daha sonra ---
    x_u_limit = 1002 #int((width-20)/20) 
    y_u_limit = 742  #int((height-20)/20) 
    kontrol_f = 0
    if x_x >= x_u_limit: # flag1 = 1 olcak
        flag1 = 1
        kontrol_f = 1
    if x_x < 22: # flag1 = 2 olcak
        flag1 = 2
        kontrol_f = 1
    if y_y >= y_u_limit: # flag1 = 4 olcak
        flag1 = 3
        kontrol_f = 1
    if y_y < 22: # flag1 = 3 olcak
        flag1 = 4
        kontrol_f = 1
    if kontrol_f == 1:
        if flag1 == 1:
            x_x-= 20
        elif flag1 == 2:
            x_x+= 20
        elif flag1 == 3:
            y_y-= 20
        elif flag1 == 4:
            y_y+= 20        
    # ---
"""
def snake_crash():
    finish = 0
    x_u_limit = int((width-20)/20) 
    y_u_limit = int((height-20)/20) 
    kontrol_f = 0
    if x_x > x_u_limit: 
        finish = 1
    if x_x < 0.5: 
        finish = 1
    if y_y > y_u_limit:
        finish = 1
    if y_y < 0.5: 
        finish = 1
    if len(c_memory_snake) > 0:
        if c_memory_snake.count(c_memory_snake[0]) > 1:
            finish = 1   
    return finish
    
def snake_bait():  
    global score,speed1
    # snake ile enemy konumları çakıştı mı kontrol ve skor oluşturma
    # snake - x,y 20 ekle , x ve y başlangıc konumları
    # x*20 ve y*20 snake başlangıc konumları
    # enemy ax ve by merkez konumları 10 cıkar 10 topla toplam alan bulunur
    change_bait = 0
    # yem yeme kısmı
    if x_x*20 < c_memory_enemy_center[0] < x_x*20 + 20 and y_y*20 < c_memory_enemy_center[1] < y_y*20 + 20:
        score += 1
        random_enemy_location()
        #if score%10 == 0 and 9 < score < 41:
        #    speed1 = speed1 - 0.030
        if score%5 == 0 and 4 < score < 16:
            speed1 = speed1 - 0.020
    return change_bait
    
def draw_snake_enemy(bait):
    global speed1,c_memory_snake,flag2
    if flag2 == 0:
        location_limited()
    if flag2 == 1:
        flag2 = 0
    time.sleep(speed1) # snake hızı 

    
    if flag1 == 1: # sola
        Snake_rect = pg.Rect( x_x*20, y_y*20, snake_size, snake_size)
        screen.blit(snake1sol, Snake_rect)
        #pg.draw.rect(screen, pg.Color(snake_color_first),pg.Rect(x_x*20, y_y*20, snake_size, snake_size ) ) # yılan baş kısmı
        snake_liste2 = []
        for c in range(score):
            snake_list = []
            #ax1 = ( c_memory_snake[c][0] + snake_size )
            ax1 = ( c_memory_snake[c][0] )
            by1 = ( c_memory_snake[c][1] )
            snake_list.append(ax1)
            snake_list.append(by1)
            Snake_rect = pg.Rect( ax1, by1, snake_size, snake_size)
            screen.blit(snake2, Snake_rect)
            #pg.draw.rect(screen, pg.Color(snake_color_other),pg.Rect(ax1, by1, snake_size, snake_size ) ) # yılan kuyruk kısım
            ##
            #pg.draw.circle(screen, pg.Color(snake_color_other), ( ax1, by1 ), 10 ) # yılan kuyruk kısım
            snake_liste2.append(snake_list)          
        c_memory_snake = []
        snake_list = []
        snake_list.append( (x_x*20) )
        snake_list.append( (y_y*20) )       
        c_memory_snake.append(snake_list)
        for c in snake_liste2:
            c_memory_snake.append(c)
            
    if flag1 == 2: # saga
        Snake_rect = pg.Rect( x_x*20, y_y*20, snake_size, snake_size)
        screen.blit(snake1sag, Snake_rect)
        #pg.draw.rect(screen, pg.Color(snake_color_first),pg.Rect(x_x*20, y_y*20, snake_size, snake_size ) ) # yılan baş kısmı
        snake_liste2 = []
        for c in range(score):
            snake_list = []
            #ax1 = ( c_memory_snake[c][0] - snake_size )
            ax1 = ( c_memory_snake[c][0] )
            by1 = ( c_memory_snake[c][1] )
            snake_list.append(ax1)
            snake_list.append(by1)
            Snake_rect = pg.Rect( ax1, by1, snake_size, snake_size)
            screen.blit(snake2, Snake_rect)
            #pg.draw.rect(screen, pg.Color(snake_color_other),pg.Rect(ax1, by1, snake_size, snake_size ) ) # yılan kuyruk kısım
            #pg.draw.circle(screen, pg.Color(snake_color_other), ( ax1, by1 ), 10 ) # yılan kuyruk kısım
            snake_liste2.append(snake_list)       
        c_memory_snake = []
        snake_list = []
        snake_list.append( (x_x*20) )
        snake_list.append( (y_y*20) )     
        c_memory_snake.append(snake_list)
        for c in snake_liste2:
            c_memory_snake.append(c)
            
    if flag1 == 3: # yukarı
        Snake_rect = pg.Rect( x_x*20, y_y*20, snake_size, snake_size)
        screen.blit(snake1y, Snake_rect)
        #pg.draw.rect(screen, pg.Color(snake_color_first),pg.Rect(x_x*20, y_y*20, snake_size, snake_size ) ) # yılan baş kısmı
        snake_liste2 = []
        for c in range(score):
            snake_list = []
            ax1 = ( c_memory_snake[c][0] )
            by1 = ( c_memory_snake[c][1] )
            #by1 = ( c_memory_snake[c][1] + snake_size )
            snake_list.append(ax1)
            snake_list.append(by1)
            Snake_rect = pg.Rect( ax1, by1, snake_size, snake_size)
            screen.blit(snake2, Snake_rect)
            #pg.draw.rect(screen, pg.Color(snake_color_other),pg.Rect(ax1, by1, snake_size, snake_size ) ) # yılan kuyruk kısım
            #pg.draw.circle(screen, pg.Color(snake_color_other), ( ax1, by1 ), 10 ) # yılan kuyruk kısım
            snake_liste2.append(snake_list)   
        c_memory_snake = []
        snake_list = []
        snake_list.append( (x_x*20) )
        snake_list.append( (y_y*20) )     
        c_memory_snake.append(snake_list)
        for c in snake_liste2:
            c_memory_snake.append(c)
            
    if flag1 == 4: # asagı
        Snake_rect = pg.Rect( x_x*20, y_y*20, snake_size, snake_size)
        screen.blit(snake1a, Snake_rect)
        #pg.draw.rect(screen, pg.Color(snake_color_first),pg.Rect(x_x*20, y_y*20, snake_size, snake_size ) ) # yılan baş kısmı
        snake_liste2 = []
        for c in range(score):
            snake_list = []
            ax1 = ( c_memory_snake[c][0] )
            by1 = ( c_memory_snake[c][1] )
            #by1 = ( c_memory_snake[c][1] - snake_size )
            snake_list.append(ax1)
            snake_list.append(by1)
            Snake_rect = pg.Rect( ax1, by1, snake_size, snake_size)
            screen.blit(snake2, Snake_rect)
            #pg.draw.rect(screen, pg.Color(snake_color_other),pg.Rect(ax1, by1, snake_size, snake_size ) ) # yılan kuyruk kısım
            #pg.draw.circle(screen, pg.Color(snake_color_other), ( ax1, by1 ), 10 ) # yılan kuyruk kısım
            snake_liste2.append(snake_list)      
        c_memory_snake = []
        snake_list = []
        snake_list.append( (x_x*20) )
        snake_list.append( (y_y*20) )  
        c_memory_snake.append(snake_list)
        for c in snake_liste2:
            c_memory_snake.append(c)
            
    if flag1 == 0:
        Snake_rect = pg.Rect( x_x*20, y_y*20, snake_size, snake_size)
        screen.blit(snake1sol, Snake_rect)
        # pg.draw.rect(screen, pg.Color(snake_color_first),pg.Rect(x_x*20, y_y*20, snake_size, snake_size ) ) # yılan baş kısmı
        c_memory_snake = []
        snake_list = []
        snake_list.append( (x_x*20) )
        snake_list.append( (y_y*20) )        
        c_memory_snake.append(snake_list)

    if bait == 1: # 1 sefer çalışır
        random_enemy_location()
    if flag1 != 0:
        time_enemy2 = time_control()
        time_enemy3 = time_enemy2 - time_enemy1
        #print('time_enemy3 ',time_enemy3)
        if time_enemy3 > 12:
            random_enemy_location()     
    ax = float(c_memory_enemy[0])
    by = float(c_memory_enemy[1])

    # enemy çizdirme
    fruit_rect = pg.Rect( ax*20, by*20, enemy_size, enemy_size)
    screen.blit(apple, fruit_rect)
    #pg.draw.rect(screen, pg.Color(enemy_color),pg.Rect(ax*20, by*20, enemy_size, enemy_size ) )
    #print('x,y',x_x*20,y_y*20)
    #print('ax,by',ax,by)

    #score çizdirme
    text = font.render(' Score ', True, (26, 117, 255))  
    textRect = text.get_rect()
    textRect.center = (int(width*10/100), int(height*10/100))
    screen.blit(text, textRect)
    text = font.render(str(score), True, (26, 117, 255))
    textRect.center = (int(width*20/100), int(height*10/100))
    screen.blit(text, textRect)

    information()
    
def draw_background():
    screen.fill(pg.Color(background_color))
    #pg.draw.rect(screen, pg.Color( wall_color ),pg.Rect(0,0,width,height),20) # kenar çizdirme (179, 0, 0)
    for x in range(0,int(width/20)+1):
        wall_rect = pg.Rect( x*20, 0, wall_size*(x+1), wall_size)
        screen.blit(wall, wall_rect)
        wall_rect = pg.Rect( x*20, 748, wall_size*(x+1), height)
        screen.blit(wall, wall_rect)
    for x in range(1,int((height-40)/20)+1):
        wall_rect = pg.Rect( 0, x*20, wall_size, wall_size*(x+1))
        screen.blit(wall, wall_rect)
        wall_rect = pg.Rect( 1004, x*20, width, wall_size*(x+1))
        screen.blit(wall, wall_rect)
        
def game_over():
    font = pg.font.SysFont(None, 100)
    text = font.render(' Game Over ', True, (26, 117, 255))  
    textRect = text.get_rect()
    textRect.center = (int(width*50/100), int(height*40/100))
    screen.blit(text, textRect)
    font = pg.font.SysFont(None, 40)

    difficulty = "emty"
    font = pg.font.SysFont(None, 70)
    surf_again_play = font.render(' Play Again ',True,'white')
    surf_quit = font.render(' Quit ',True,'white')
    button_again_play = pg.Rect( int(width*35/100), int(height*55/100), 320, 80)
    button_quit = pg.Rect( int(width*35/100), int(height*70/100), 320, 80)
    font = pg.font.SysFont(None, 40) 
    for events in pg.event.get():
        if events.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if events.type == pg.MOUSEBUTTONDOWN:
            if button_again_play.collidepoint(events.pos):
                difficulty = "again_play"
            if button_quit.collidepoint(events.pos):
                difficulty = "quit"
                
    a,b = pg.mouse.get_pos()
    if button_again_play.x <= a <= button_again_play.x + 320 and button_again_play.y <= b <= button_again_play.y + 80:
        pg.draw.rect(screen,(77, 255, 77),button_again_play)
        screen.blit(surf_again_play,(button_again_play.x + 32, button_again_play.y + 15))
    else:
        pg.draw.rect(screen,(255, 51, 0),button_again_play)
        screen.blit(surf_again_play,(button_again_play.x + 32, button_again_play.y + 15))

    if button_quit.x <= a <= button_quit.x + 320 and button_quit.y <= b <= button_quit.y + 80:
        pg.draw.rect(screen,(77, 255, 77),button_quit)
        screen.blit(surf_quit,(button_quit.x + 100, button_quit.y + 15))
    else:
        pg.draw.rect(screen,(255, 51, 0),button_quit)
        screen.blit(surf_quit,(button_quit.x + 100, button_quit.y + 15))
        
    pg.display.update()
    return difficulty
def time_control():
    global saat2,dk2,sn2
    zaman2 = time.strftime('%X')
    saat2 = zaman2[0]+zaman2[1]
    dk2 = zaman2[3]+zaman2[4]
    sn2 = zaman2[6]+zaman2[7]
    time_sn = int(saat2)*3600 + int(dk2)*60 + int(sn2)
    return time_sn

def information():
    time_sn2 = time_control()
    control_t = time_sn2 - time_sn1
    if control_t < 91:
        font = pg.font.SysFont(None, 30)
        text = font.render(' F2 Press for Options and Pause ', True, (140, 140, 140))  
        textRect = text.get_rect()
        textRect.center = (int(width*82/100), int(height*5/100))
        screen.blit(text, textRect)
        font = pg.font.SysFont(None, 40)

def game_loop():
    global sayac_ekran,x_x,y_y,screen,flag1,count_first
    global pause,count_pause,c_memory_snake,flag2
    flag2 = 0
    bait = 0
    if count_first == 0:
        bait = 1
        count_first = 1
       
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()        
        if pause == 0:    
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if flag1 != 2:
                        x_x-= 1
                        flag1 = 1
                        flag2 = 1
                        snake_bait()
                if event.key == pg.K_RIGHT:
                    if flag1 != 1:
                        x_x+= 1
                        flag1 = 2
                        flag2 = 1
                        snake_bait()
                if event.key == pg.K_UP:
                    if flag1 != 4:
                        y_y-= 1
                        flag1 = 3
                        flag2 = 1
                        snake_bait()
                if event.key == pg.K_DOWN:
                    if flag1 != 3:
                        y_y+= 1
                        flag1 = 4
                        flag2 = 1
                        snake_bait()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_F10:
                sayac_ekran += 1
                if sayac_ekran%2 == 1:
                    screen = pg.display.set_mode(screen_size,pg.FULLSCREEN)
                    #screen = pg.display.set_mode(screen_size1)
                if sayac_ekran%2 == 0:
                    screen = pg.display.set_mode(screen_size)
            if event.key == pg.K_F2:
                count_pause += 1
                if count_pause % 2 == 1:
                    pause = 1
                if count_pause % 2 == 0:
                    pause = 0
            if event.key == pg.K_ESCAPE:
                # kullanıcıya cıkılsın mı diye sorulacak
                pg.quit()
                sys.exit()
                    
                    
    if pause == 0:
        draw_background()
        draw_snake_enemy(bait)
        snake_bait()
               
        pg.display.update()
        
    if pause == 1:
        font = pg.font.SysFont(None, 80)
        text = font.render(' Pause ', True, (26, 117, 255))  
        textRect = text.get_rect()
        textRect.center = (int(width*50/100), int(height*50/100))
        screen.blit(text, textRect)
        font = pg.font.SysFont(None, 40)
        pg.display.update()
        
random_snake_location()
while 1 :
    if snake_crash() == 0: 
        game_loop()
        
    if snake_crash() == 1:  # gameover kısmı
        make = game_over()
        time.sleep(0.1)     
        if make == "quit":
            pg.quit()
            sys.exit()
        if make == "again_play":
            reset()
            random_snake_location()














    
