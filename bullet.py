from entity import entity
import numpy as np

class bullet(entity):
    def __init__(self, position, acceleration, orientation,
                 sprite, rotateSprite):
        
       	self.timer = 100
       	self.speed = 5
       	self.velocity = self.speed * np.asarray([np.cos(orientation), np.sin(orientation)])
        super(bullet, self).__init__(position, acceleration, orientation,
                                     self.velocity, self.speed, sprite, rotateSprite)

