import numpy as np
import pygame
from entity import entity
import math

class ship(entity):
    def __init__(self, hitpoints, position, acceleration, orientation,
                 velocity, speed, sprite, rotateSprite):
    #def __init__(self, position, hitpoints, acceleration, orientation,
    # 			 velocity, speed, sprite, rotateSprite):
        self.hitpoints = hitpoints

        super(ship, self).__init__(position, acceleration, orientation,
                                   velocity, speed, sprite, rotateSprite)

        #self.entity = entity(position, acceleration, orientation,
        #                       velocity, speed, sprite, rotateSprite)

        '''
        self.position = position
        self.acceleration = acceleration
        self.orientation = orientation
        self.rotationVector = np.asarray([np.cos(orientation), 
        								 np.sin(orientation)])
        self.velocity = velocity
        self.speed = speed
        self.sprite = sprite
        self.rotateSprite = rotateSprite
        self.rotateSprite.rect = self.position
        '''

    '''
    def rotateShip(self):
    	self.rotationVector = np.asarray([np.cos(self.orientation), 
    									 np.sin(self.orientation)])

    	imageRot = np.arctan2(self.rotationVector[0], self.rotationVector[1])
    	self.rotateSprite.image = pygame.transform.rotate(self.sprite, 
    													  math.degrees(imageRot))

    def accelerateShip(self):
    	self.velocity += self.acceleration*self.rotationVector
    	self.speed = np.linalg.norm(self.velocity)

    def updatePosition(self, size):
    	self.position += self.velocity
    	self.position %= size

    def updateShip(self, size):
    	self.rotateSprite.rect = self.position
    	self.accelerateShip()
    	self.rotateShip()
    	self.updatePosition(size)
    '''

