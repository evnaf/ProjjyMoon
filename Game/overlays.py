import pygame as pg
from settings import *

class Overlay:
    def __init__(self,player):
        # General Setup --------------------------------
        self.display_surface = pg.display.get_surface()
        self.player = player 
        # imports
        self.tools_surface = {}