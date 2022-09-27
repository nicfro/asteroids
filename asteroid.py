from entity import entity
import numpy as np

class asteroid(entity):
    def __init__(self, position, acceleration, orientation,
                 sprite, rotateSprite):
        
       	self.speed = 1
       	self.velocity = self.speed * np.asarray([np.cos(orientation), np.sin(orientation)])
        super(asteroid, self).__init__(position, acceleration, orientation,
                                     self.velocity, self.speed, sprite, rotateSprite)