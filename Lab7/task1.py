import pygame
import datetime

pygame.init()


screen = pygame.display.set_mode((800, 600))

done = False

clock = pygame.time.Clock()

img_mouse = pygame.image.load("mainclock.png")
img_leftarm = pygame.image.load("leftarm.png")
img_rightarm = pygame.image.load("rightarm.png")

img_mouse = pygame.transform.scale(img_mouse, (800, 600))
img_leftarm = pygame.transform.scale(img_leftarm, (img_leftarm.get_width() * 4 // 7, img_leftarm.get_height() * 4 // 7))
img_rightarm = pygame.transform.scale(img_rightarm, (img_rightarm.get_width() * 4 // 7, img_rightarm.get_height() * 4 // 7))

bg_rect = img_mouse.get_rect(center = (400, 300))

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    time_now = datetime.datetime.now().time()
    sec_angle = -(time_now.second * 6)
    min_angle = -(time_now.minute * 6)

    rotated_leftarm = pygame.transform.rotate(img_leftarm, sec_angle)
    rotated_rightarm = pygame.transform.rotate(img_rightarm, min_angle)

    leftarm_rect = rotated_leftarm.get_rect(center = bg_rect.center)
    rightarm_rect = rotated_rightarm.get_rect(center = bg_rect.center)


    screen.blit(img_mouse, bg_rect)
    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    pygame.display.flip()