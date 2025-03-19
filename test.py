import pygame
from math import pi
import random

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

hurd_limit = 20
hurd = [pygame.Rect(0,0,5,5), pygame.Rect(600,300,5,5), pygame.Rect(100, 100, 5, 5)]

portal = pygame.Rect(400, 250, 60, 60)

while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set screen color
    screen.fill([255,255,255])

    pygame.draw.rect(screen, [100,100,100], portal)

    # Draw the player
    player_rect = pygame.draw.rect(screen, [0,0,0], (player_pos.x, player_pos.y, player_size, player_size))

    #if len(hurd) <= hurd_limit:
        

    index = player_rect.collidelist(hurd)
    if index >= 0:
        beast = hurd[index]
        player_size += beast.width//2
        hurd.pop(index)

    for h in hurd:
        pygame.draw.rect(screen, [0,0,0], h)
        direction = -1
        if player_rect.width >= portal.width:
            direction = 1
        x = direction
        y = direction
        if player_pos.x < h.x:
            x = -x
        if player_pos.y < h.y:
            y = -y
        h.move_ip(x,y)
            
    
    if portal.contains(player_rect) and portal.width - player_rect.width < 5 :
        running = False
        win = True

    # update player position based on keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 1
    if keys[pygame.K_s]:
        player_pos.y += 1
    if keys[pygame.K_a]:
        player_pos.x -= 1
    if keys[pygame.K_d]:
        player_pos.x += 1
        
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

if win:
    fontSurface = font.render("You win", True, [0,255,0])
else:
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
