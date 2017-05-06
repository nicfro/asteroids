import numpy as np
import pygame
from entity import entity
import math

class ship(entity):
    def __init__(self, hitpoints, position, acceleration, orientation,
                 velocity, speed, sprite, rotateSprite):
        self.hitpoints = hitpoints

        super(ship, self).__init__(position, acceleration, orientation,
                                   velocity, speed, sprite, rotateSprite)

