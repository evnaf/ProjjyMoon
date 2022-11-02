import pygame as pg
from settings import *
from player import Player
from sprites import Generic

class World:
    def __init__(self):
        # Initialize Display Surface
        self.display_surface = pg.display.get_surface()
        # Init Sprite Groups
        self.all_sprites = CameraGroup()
        # Init Setup
        self.setup()
    
    def setup(self):
        
        self.player = Player((640,360), self.all_sprites)
        Generic(pos = (0,0),surf = pg.image.load('Assets\ground.png').convert_alpha(), groups = self.all_sprites, z = LAYERS['ground'])
      
    def run(self,dt):
        # Setting background color to black
        self.display_surface.fill('black')
        self.all_sprites.customize_draw(self.player)
        self.all_sprites.update(dt)
        
class CameraGroup(pg.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pg.display.get_surface()
		self.offset = pg.math.Vector2()

	def customize_draw(self, player):
		self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
		self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

		for layer in LAYERS.values():
			for sprite in self.sprites():
				if sprite.z == layer:
					offset_rect = sprite.rect.copy()
					offset_rect.center -= self.offset
					self.display_surface.blit(sprite.image, offset_rect)