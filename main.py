import pygame
import numpy as np
import math
from ship import ship
from bullet import bullet
from asteroid import asteroid
import copy
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = [1600, 800]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Nicomina")
 
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

spriteImage = "shipLong4.png"
bulletImage = "bullet.png"
asteroidImage = "asteroid.png"
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

asteroidSprite = pygame.image.load(asteroidImage).convert()
asteroidRotSprite = pygame.sprite.Sprite()
asteroidRotSprite.image = pygame.image.load(asteroidImage).convert()
bulletList = []
asteroidList = []

tempPos = copy.copy(ship.position)
tempOri = copy.copy(ship.orientation)
asteroidList.append(asteroid(tempPos, 0, tempOri, asteroidSprite, 
                  asteroidRotSprite))


pygame.key.set_repeat(5,100)
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
                ship.orientation -= 0.5 % (2*math.pi)
            if event.key == pygame.K_RIGHT:
                ship.orientation += 0.5 % (2*math.pi)
            if event.key == pygame.K_SPACE:
                tempPos = copy.copy(ship.position)
                tempOri = copy.copy(ship.orientation)
                bulletList.append(bullet(tempPos, 0, tempOri, bulletSprite, 
                                  bulletRotSprite))
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
            ship.acceleration = 0


    ship.update(size)
    screen.fill(BLACK)

    bulletList[:] = [b for b in bulletList if (b.timer > 0)]
    if len(bulletList) > 0:
        for b in bulletList:
            if b.timer > 0:
                b.timer-=1
                b.update(size)
                screen.blit(b.rotateSprite.image, b.rotateSprite.rect)

    if len(asteroidList) > 0:
        for a in asteroidList:
            a.update(size)
            screen.blit(a.rotateSprite.image, a.rotateSprite.rect)
           
    print(len(bulletList))
    screen.blit(ship.rotateSprite.image, ship.rotateSprite.rect)
    pygame.display.flip()
    
    # --- Limit to 100 frames per second
    clock.tick(100)

# Close the window and quit.
pygame.quit()

