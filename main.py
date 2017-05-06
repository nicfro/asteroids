import pygame
import numpy as np
import math
from ship import ship
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = [600, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Nicomina")
 
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

spriteImage = "shipLong4.png"
# Starting position of the spaceship
pos = np.asarray([100.0,100.0])
hp = 100
acc = 0
orientation = 0
vel = np.asarray([0.0,0.0])
speed = 0
sprite = pygame.image.load(spriteImage).convert()
rotSprite =  pygame.sprite.Sprite()
rotSprite.image = pygame.image.load(spriteImage).convert()

ship = ship(hp, pos, acc, orientation, vel, speed, sprite, 
            rotSprite)

pygame.key.set_repeat(1,10)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.acceleration = 0.1      
            if event.key == pygame.K_LEFT:
                ship.orientation -= 0.1 % (2*math.pi)
            if event.key == pygame.K_RIGHT:
                ship.orientation += 0.1 % (2*math.pi)
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
            ship.acceleration = 0

    
    ship.update(size)
    screen.fill(BLACK)

    screen.blit(ship.rotateSprite.image, ship.rotateSprite.rect)
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(100)

# Close the window and quit.
pygame.quit()

