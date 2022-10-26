import pygame as pg
from settings import *
from player import Player

class World:
    def __init__(self):
        # Initialize Display Surface
        self.display_surface = pg.display.get_surface()
        # Init Sprite Groups
        self.all_sprites = pg.sprite.Group()
        # Init Setup
        self.setup()
    
    def setup(self):
        self.player = Player((640,360), self.all_sprites)
    
    def run(self,dt):
        # Setting background color to black
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)