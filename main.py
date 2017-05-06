import pygame
import numpy as np
import math
from ship import ship
from bullet import bullet
import copy
 
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
bulletImage = "bullet.png"
# Starting position of the spaceship
pos = np.asarray([100.0,100.0])
hp = 100
acc = 0
orientation = 0
vel = np.asarray([0.0,0.0])
speed = 0
shipSprite = pygame.image.load(spriteImage).convert()
shipRotSprite =  pygame.sprite.Sprite()
shipRotSprite.image = pygame.image.load(spriteImage).convert()

ship = ship(hp, pos, acc, orientation, vel, speed, shipSprite, 
            shipRotSprite)

bulletSprite = pygame.image.load(bulletImage).convert()
bulletRotSprite = pygame.sprite.Sprite()
bulletRotSprite.image = pygame.image.load(bulletImage).convert()

bulletList = []
pygame.key.set_repeat(10,2)
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
            if event.key == pygame.K_SPACE:
                tempPos = copy.copy(ship.position)
                tempOri = copy.copy(ship.orientation)
                tempVel = 12 * np.asarray([np.cos(tempOri), np.sin(tempOri)])
                bulletList.append(bullet(tempPos, 0, tempOri, tempVel, 12, bulletSprite, 
                                  bulletRotSprite))
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
            ship.acceleration = 0

    
    ship.update(size)
    screen.fill(BLACK)

    if len(bulletList) > 0:
        for i in range(len(bulletList)):
            bulletList[i].update(size)
            screen.blit(bulletList[i].rotateSprite.image, bulletList[i].rotateSprite.rect)

    screen.blit(ship.rotateSprite.image, ship.rotateSprite.rect)
    pygame.display.flip()
    
    # --- Limit to 100 frames per second
    clock.tick(100)

# Close the window and quit.
pygame.quit()

