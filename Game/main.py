import pygame as pg
import sys as sy
from settings import *
from world import World 

class moonglow:
    def __init__(self): 
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption('Project Moonglow')
        self.world = World()
    
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sy.exit()
            
            dt = self.clock.tick() / 1000
            self.world.run(dt)
            pg.display.update()
    
if __name__ == '__main__':
    moonglow = moonglow()
    moonglow.run()
    