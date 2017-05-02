import pygame
import numpy as np
import math
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = [600, 400]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the spaceship
pos = [100,100]
 
# Speed and direction of spaceship
a = 0
theta = 0

v = np.asarray([0,0])
b = pygame.sprite.Sprite() 
savedImage = pygame.image.load("sprite.png").convert()
b.image = pygame.image.load("sprite.png").convert()

pygame.key.set_repeat(10,10)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    a += 0.1
            if event.key == pygame.K_DOWN:
                    a -= 0.1
            if event.key == pygame.K_LEFT:
                theta -= 0.1 % (2*math.pi)    
            if event.key == pygame.K_RIGHT:
                theta += 0.1 % (2*math.pi)
                

    screen.fill(BLACK)

    b.rect = pos

    rotationVector = np.asarray([np.cos(theta), np.sin(theta)])
    imageRot = np.arctan2(rotationVector[0], rotationVector[1])
    
    b.image = pygame.transform.rotate(savedImage, math.degrees(imageRot))
    screen.blit(b.image, b.rect)

    v = a*rotationVector
    
    speed = np.linalg.norm(v)
    
    pos += v
    pos %= size

    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    print(speed)
# Close the window and quit.
pygame.quit()

#hejda