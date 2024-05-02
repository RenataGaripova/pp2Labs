# Import
from add_data import *
from update_data import *
from check_username import *
import pygame
import random
import time
from color_palette import *

pygame.init()

# Some screen parameters
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((HEIGHT, WIDTH))
font = pygame.font.SysFont("Verdana", 60)

font_over = font.render("Game Over", True, colorBLACK)
font_pause = font.render("Pause", True, colorBLACK)
font_small = pygame.font.SysFont("Verdana", 30)

CELL = 30

LVL = 1 # Level increases each 4 times we get food
SCORE = 0 # Score increases each time we get food

def draw_grid(screen):
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess(screen):
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Function used to check if we have to update level of the game
def check_if_next_lvl():
    global FPS
    global SCORE
    global LVL

    if (SCORE % 4 == 0 and SCORE != 0):
        LVL += 1
        FPS += 5 # Speed increases with each level
        return 1

# Body of the snake consists of points 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    global done
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.body_lists = [[10, 11], [10, 12], [10, 13]]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))
        
    def check_collision(self, food):
        global SCORE
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            self.body_lists.append([head.x, head.y])
            SCORE += 1
            return 1
        else:
            return 0
        
    def is_over(self):
        head = self.body[0]
        if head.x == 20 or head.y == 20 or head.x == -1 or head.y == -1:
            print("GAME OVER!")
            return 1
    
class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    #Function to randomly change the position of Food
    def change_position(self, snake):
        new_x = random.randint(0, 19)
        new_y = random.randint(0, 19)

        new_coordinates = [new_x, new_y]
        while True:
            if new_coordinates not in snake.body_lists:
                self.pos = Point(new_x, new_y)
                break
            else:
                new_x = random.randint(0, 20)
                new_y = random.randint(0, 20)       

    # Drawing the food on our screen
    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

new_username = input("Enter your username: ")

exists = check_username(new_username)

while exists:
    print("This user already exists!")
    new_username = input("Enter your username: ")
    exists = check_username(new_username)
else:
    add_data(new_username)
    screen.fill(colorWHITE)
    screen.blit(font_pause, (150,250))
    pygame.display.flip()
    time.sleep(5)

done = False
pause = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pause == False:
                pause = True
            elif event.key == pygame.K_SPACE and pause == True:
                pause = False
            elif event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    if pause:
        screen.fill(colorWHITE)
        screen.blit(font_pause, (150,250))
        pygame.display.flip()
        continue
    else:

        draw_grid_chess(screen)

        snake.move()

        if snake.check_collision(food):
            food.change_position(snake)
            update_score(SCORE, new_username)

            if check_if_next_lvl():
                update_level(LVL, new_username)

            print(food.pos.x, food.pos.y)
    
        snake.draw()
        food.draw()

        scores = font_small.render("SCORES: " + str(SCORE), True, colorBLACK)
        lvl_now = font_small.render("LVL: " + str(LVL), True, colorBLACK)
        screen.blit(scores, (10,10))
        screen.blit(lvl_now, (490, 10))

        if snake.is_over():
            screen.fill(colorRED)
            screen.blit(font_over, (125,250))
            pygame.display.flip()
            time.sleep(3)
            done = True

        pygame.display.flip()
    clock.tick(FPS)