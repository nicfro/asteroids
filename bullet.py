class bullet(entity):
    def __init__(self, weaponName, position, acceleration, orientation,
                 velocity, speed, sprite, rotateSprite):
        
        super(bullet, self).__init__(position, acceleration, orientation,
                                     velocity, speed, sprite, rotateSprite)

