import numpy as np
import pygame
import math

class entity(object):
    def __init__(self, position, acceleration, orientation,
    			 velocity, speed, sprite, rotateSprite):
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

    def rotate(self):
    	self.rotationVector = np.asarray([np.cos(self.orientation), 
    									 np.sin(self.orientation)])

    	imageRot = np.arctan2(self.rotationVector[0], self.rotationVector[1])
    	self.rotateSprite.image = pygame.transform.rotate(self.sprite, 
    													  math.degrees(imageRot))

    def accelerate(self):
        #checking for speed limit
        tempVelocity = self.velocity + (self.acceleration*self.rotationVector)
        if np.linalg.norm(tempVelocity) < 10:
            #updating velocity and speed
        	self.velocity += self.acceleration*self.rotationVector
        	self.speed = np.linalg.norm(self.velocity)

    def updatePosition(self, size):
    	self.position += self.velocity
    	self.position %= size

    def update(self, size):
    	self.rotateSprite.rect = self.position
    	self.accelerate()
    	self.rotate()
    	self.updatePosition(size)