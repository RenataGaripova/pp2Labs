import pygame

pygame.init()

screen = pygame.display.set_mode((700, 600))
color_screen = (250, 250, 250)
color_circle = (250, 0, 0)

done = False
x = 350
y = 300

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and (0 <= y - 25 - 20): y -= 20
    if pressed[pygame.K_DOWN] and (y + 25 + 20 <= 600): y += 20
    if pressed[pygame.K_RIGHT] and (x + 25 + 20 <= 700): x += 20
    if pressed[pygame.K_LEFT] and (0 <= x - 25 - 20): x -= 20

    screen.fill(color_screen)

    pygame.draw.circle(screen, color_circle, (x, y), 25)
    pygame.display.flip()
    clock.tick(60)