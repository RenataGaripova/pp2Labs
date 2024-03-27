import pygame

def next_song():
    global currently_playing
    global playlist

    if currently_playing < len(playlist) - 1:
        currently_playing += 1
    else:
        currently_playing = 0

    pygame.mixer.music.load(playlist[currently_playing])
    pygame.mixer.music.play()

def prev_song():
    global currently_playing
    global playlist

    if currently_playing > 0:
        currently_playing -= 1
    else:
        currently_playing = len(playlist) - 1

    pygame.mixer.music.load(playlist[currently_playing])
    pygame.mixer.music.play()

pygame.init()

screen = pygame.display.set_mode((700, 600))
color_screen = (250, 250, 250)

play_button = pygame.image.load('play.png').convert_alpha()
pause_button = pygame.image.load('pause.png').convert_alpha()
right_button = pygame.image.load('right_arrow.png').convert_alpha()
left_button = pygame.image.load('left_arrow.png').convert_alpha()

screen.fill(color_screen)
screen.blit(right_button, (500, 420))
screen.blit(left_button, (92, 420))
screen.blit(play_button, (296, 400))

done = False

playlist = ['song1.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3', 'song5.mp3', 'song6.mp3', 'song7.mp3']
currently_playing = 0

play = False

cycle = 0

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if play == True:
                    play = False
                    pygame.mixer.music.pause()
                    screen.blit(play_button, (296, 400))
                elif play == False:
                    play = True
                    screen.blit(pause_button, (296, 400))
                    if cycle == 0:
                        cycle = 1
                        pygame.mixer.music.load(playlist[currently_playing])
                        pygame.mixer.music.play()
                    else:
                        pygame.mixer.music.unpause() 

            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()


    pygame.display.flip()