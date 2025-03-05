import pygame
from math import pi

pygame.init() # initialize pygame
pygame.font.init()

font = pygame.font.SysFont('Ariel', 42)

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True
win = False

# create a variable to store player position so we can modify it based on keyboard input
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
player_health = 80
player_size = player_health // 2


while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set screen color
    screen.fill([255,255,255])

    # Draw the player
    pygame.draw.rect(screen, [0,0,0], (player_pos.x, player_pos.y, player_size, player_size))

    #pygame.draw.rect(screen, [0,0,0], 

    # update player position based on keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 10
    if keys[pygame.K_s]:
        player_pos.y += 10
    if keys[pygame.K_a]:
        player_pos.x -= 10
    if keys[pygame.K_d]:
        player_pos.x += 10
        
    player_health -= 0.1
    player_size = player_health // 2
    if player_health <= 0:
        running = False
        
    # handle player wrapping around the screen
    if player_pos.x <= -player_size:
        player_pos.x = screen.get_width() - 1
    if player_pos.x >= screen.get_width():
        player_pos.x = -player_size + 1
    if player_pos.y <= -player_size:
        player_pos.y = screen.get_height() - 1
    if player_pos.y >= screen.get_height():
        player_pos.y = -player_size + 1

    # Render what you've drawn to the screen
    pygame.display.flip()

    clock.tick(60) # limit to 60 FPS

fontSurface = font.render("You Died", True, [255,0,0])
screen.blit (fontSurface, [300, 200])
pygame.display.flip()

running = True
while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Exit game when we leave the game loop
pygame.quit()
