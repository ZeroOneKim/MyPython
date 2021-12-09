from os import close
import pygame                    
import random                   
import sys                         
import time                            

def paintEntity(entity, x, y) : 
   monitor.blit(entity, (int(x), int(y)))

def levelMessage(level):   #레벨 메시지 출력 함수
    levelfont = pygame.font.Font('NanumGothic.ttf', 25)
    text = levelfont.render(u'레벨 ' + str(level), True, (255-r, 255-g, 255-b))
    monitor.blit(text, (swidth*0.45, sheight*0.01))
    pygame.display.update()

def bombMessage():          #**3** 사망 메시지에 대한 함수
    myfont = pygame.font.Font('NanumGothic.ttf', 30)
    text = myfont.render(u'Game Over!!', True, (255-r, 255-g, 255-b))
    monitor.blit(text, (swidth*0.3, sheight*0.3))
    pygame.display.update()

def writeScore(score) :
    myfont = pygame.font.Font('NanumGothic.ttf', 20)    
    txt = myfont.render(u'파괴한 우주괴물 수 : ' + str(score), True, (255-r, 255-g, 255-b))
    monitor.blit(txt, (10, sheight - 40))   

def playGame() :
    global monitor, ship, monster, missile

    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256) 
    
    shipX = swidth / 2 
    shipY = sheight * 0.8
    dx, dy = 0, 0 
    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size              
    monsterX = random.randrange(0, int(swidth * 0.85))           #1  위에서 내려오게 밑 코드
    monsterY = 0                                                #1  위에서 내려오게
    monsterSpeed = 3

    missileX, missileY = None, None  

    fireCount = 0
    Level = 0 
    while True :
        (pygame.time.Clock()).tick(50) 
        monitor.fill((r, g, b))             

        for e in pygame.event.get() :
            if e.type in [pygame.QUIT]  :
                pygame.quit()
                sys.exit()

            if e.type in [pygame.KEYDOWN] :
                if e.key == pygame.K_LEFT : dx = -5
                elif e.key == pygame.K_RIGHT : dx = +5
                elif e.key == pygame.K_UP : dy = -5
                elif e.key == pygame.K_DOWN : dy = +5

                elif e.key == pygame.K_SPACE : 
                    if missileX == None :                     
                        missileX = shipX + shipSize[0]/2   
                        missileY = shipY

            if e.type in [pygame.KEYUP] :
                 if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                    or e.key == pygame.K_UP or e.key == pygame.K_DOWN : dx, dy = 0, 0

        if (0 < shipX+dx and shipX+dx <= swidth-shipSize[0]) \
            and (sheight/2 < shipY+dy and shipY+dy <= sheight - shipSize[1]) : 
            shipX += dx
            shipY += dy
        paintEntity(ship, shipX, shipY)  

        monsterY += monsterSpeed            #1 Y로 지정해야 내려오게   

        if monsterY > sheight :              #1 만약 Y값이 가로폭보다 크다면??
            monsterX = random.randrange(0, int(swidth * 0.85))   #1 X좌표 아무데서나 떨어지게
            monsterY = 0
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = Level + 1
            
            
        paintEntity(monster, monsterX, monsterY)
        if missileX != None :                         
            missileY -= 10
            if missileY < 0 :
                  missileX, missileY= None, None  
        if missileX != None :          
            paintEntity(missile, missileX, missileY)
            if (monsterX < missileX and missileX < monsterX + monsterSize[0]) and \
                   (monsterY < missileY and missileY < monsterY + monsterSize[1]) :
                fireCount += 1
                if fireCount >= 5:
                    Level = int(fireCount/5) #5점을 획득하면 레벨이 1 증가
                monster = pygame.image.load(random.choice(monsterImage))
                monsterSize = monster.get_rect().size
                monsterX = random.randrange(0, int(swidth * 0.85))   #1 맞았을 때도 변경 해주게끔
                monsterY = 0
                monsterSpeed = Level + 1  # 레벨기능 
                
                missileX, missileY= None, None   
        
        if (monsterX < shipX and shipX < monsterX + monsterSize[0]) and \
            (monsterY < shipY and shipY < monsterY + monsterSize[1]): #**4**
            endgame.play()
            bombMessage()      #터질때,
            time.sleep(5)  
            close()
        writeScore(fireCount)
        levelMessage(Level)

        pygame.display.update()

r, g, b = [0] * 3               
swidth, sheight = 500, 700 
monitor = None 
ship, shipSize = None, 0    

monsterImage = ['monster01.png', 'monster02.png', 'monster03.png', 'monster04.png', \
                'monster05.png', 'monster06.png', 'monster07.png', 'monster08.png', \
                'monster09.png', 'monster10.png']

monster = None 
missile = None   
pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))

pygame.display.set_caption('우주괴물 무찌르기')
endgame = pygame.mixer.Sound('Bang.wav')    #4  endgame에 사운드 넣기
ship = pygame.image.load('ship01.png')
shipSize = ship.get_rect().size

missile = pygame.image.load('missile.png')

playGame()
