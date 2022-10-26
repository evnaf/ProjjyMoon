import pygame as py 
from settings import *

class Player(py.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        # General Setup
        self.image = py.Surface((32,60))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
        
        # Move the player
        self.direction = py.math.Vector2()
        self.pos = py.math.Vector2(self.rect.center)
        self.speed = 125
        
    def input(self):
        keys = py.key.get_pressed()
      
        if keys[py.K_w]:
            self.direction.y = -1
        elif keys[py.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[py.K_a]:
            self.direction.x = -1
        elif keys[py.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    def movePlayer(self,dt):
        # Normalize the direction
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        # Collision Horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # Collision Vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        
    
    def update(self, dt):
        self.input()
        self.movePlayer(dt)

    