#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ENEMY_SPEED = 5
SPEED = 5
SCORE = 0
COINS = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Change size of coins

ORIG_COIN1 = pygame.image.load("coin1.png")
ORIG_COIN5 = pygame.image.load("coin5.png")
ORIG_COIN10 = pygame.image.load("coin10.png")

coin1_img = pygame.transform.scale(ORIG_COIN1, (ORIG_COIN1.get_width() // 8, ORIG_COIN1.get_height() // 4))
coin5_img = pygame.transform.scale(ORIG_COIN5, (ORIG_COIN5.get_width() // 4, ORIG_COIN5.get_height() // 4))
coin10_img = pygame.transform.scale(ORIG_COIN10, (ORIG_COIN10.get_width() // 4, ORIG_COIN10.get_height() // 4))
randomizer = 1

#class Enemy
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,ENEMY_SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#class Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#class Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def move(self):
        global COINS
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600): #if we did not collect the coin, a new coin appears
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin_1(Coin):
    def __init__(self):
        super().__init__()
        self.num = 1
        self.image = coin1_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(54, SCREEN_WIDTH-54), 0)

class Coin_5(Coin):
    def __init__(self):
        super().__init__()
        self.num = 5
        self.image = coin5_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(54, SCREEN_WIDTH-54), 0)

class Coin_10(Coin):
    def __init__(self):
        super().__init__()
        self.num = 10
        self.image = coin10_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(54, SCREEN_WIDTH-54), 0)


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin_1()
C5 = Coin_5()
C10 = Coin_10()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C5)
coins.add(C10)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              ENEMY_SPEED += 0.5
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coint_amount = font_small.render(str(COINS), True, YELLOW)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coint_amount, (370, 10))

    if randomizer == 1:
        DISPLAYSURF.blit(C1.image, C1.rect)
        C1.move()
    elif randomizer == 5:
        DISPLAYSURF.blit(C5.image, C5.rect)
        C5.move()
    else:
        DISPLAYSURF.blit(C10.image, C10.rect)
        C10.move()

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()

    #To be run if collision occurs between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        if randomizer == 1:
            COINS += 1
            C1.rect.top = 601
            C1.move()
        elif randomizer == 5:
            COINS += 5
            C5.rect.top = 601
            C5.move()
        else:
            COINS += 5
            C10.rect.top = 601
            C10.move()

        if (COINS % 5 == 0 and COINS != 0): # Enemy's speed increases with each 5 coins
            ENEMY_SPEED += 1

        randomizer = random.choice((1, 5, 10))
        
    pygame.display.update()
    FramePerSec.tick(FPS)