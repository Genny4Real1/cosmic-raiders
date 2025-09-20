#Cosmic Raiders Version 0.1
import pygame
import random

#Initialization
pygame.init() #Initialize pygame modules
screen = pygame.display.set_mode((1600, 900)) #setup the game window
pygame.display.set_caption("Cosmic Raiders")
clock = pygame.time.Clock() #to check game speed
dt = pygame.time.get_ticks()/ 1000

# Player
player_img = pygame.Surface((60, 40))
player_img.fill((0, 255, 0))
player = {'x':  800, 'y': 800, 'speed': 7.5}

# Enemies
enemy_img = pygame.Surface((30, 30))
enemy_img.fill((252, 0, 0))
enemies = []
for i in range(5):
    while True:
        x = random.randint(20,1480)
        if all(x != e['x'] for e in enemies):
            break
    enemies.append({'x': x, 'y': (random.randint(20, 90)), 'speed': 0.05})

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
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player['x'] > 0:
        player['x'] -= player['speed']
        print(f"x: {player['x']}, y: {player['y']}")
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player['x'] < 1600 - 60:
        player['x'] += player['speed']
        print(f"x: {player['x']}, y: {player['y']}")
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player['y'] < 900 - 40:
        player['y'] += player['speed']
        print(f"x: {player['x']}, y: {player['y']}")
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player['y'] > 0:
        player['y'] -= player['speed']
        print(f"x: {player['x']}, y: {player['y']}")
    if keys[pygame.K_ESCAPE]:
        running = False

    # Enemies behaviour


    for enemy in enemies:
        screen.blit(enemy_img, (enemy['x'], enemy['y']))
        enemy['y'] += enemy['speed']

        enemy['speed'] += 0.01 * dt





    # Player Img
    screen.blit(player_img, (player['x'], player['y']))
    pygame.display.flip()  # aggiorna il display

pygame.quit()
