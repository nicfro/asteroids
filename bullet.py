from entity import entity

class bullet(entity):
    def __init__(self, position, acceleration, orientation,
                 velocity, speed, sprite, rotateSprite):
        
       	self.timer = 200
        super(bullet, self).__init__(position, acceleration, orientation,
                                     velocity, speed, sprite, rotateSprite)

