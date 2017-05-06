from entity import entity

class ship(entity):
    def __init__(self, hitpoints, position, acceleration, orientation,
                 velocity, speed, sprite, rotateSprite):
        self.hitpoints = hitpoints

        super(ship, self).__init__(position, acceleration, orientation,
                                   velocity, speed, sprite, rotateSprite)

