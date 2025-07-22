#Cosmic Raiders Version 0.1
import pygame
# import random to generate enemy positions?

#Initialization
pygame.init() #Initialize pygame modules
screen = pygame.display.set_mode((800, 600)) #setup the game window
pygame.display.set_caption("Cosmic Raiders")
clock = pygame.time.Clock() #to check game speed

# Player
player_img = pygame.Surface((50, 30))
player_img.fill((0, 255, 0))
player_x = 375
player_y = 540
player_speed = 5

# Main Game Loop
running = True
while running:
    clock.tick(60) #to cap speed at 60fps 
    screen.fill((0, 0, 0))  # black background
    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 800 - 50:
        player_x += player_speed

    # Player Img
    screen.blit(player_img, (player_x, player_y))
    pygame.display.flip()  # aggiorna il display

pygame.quit()