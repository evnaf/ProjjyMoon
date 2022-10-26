import pygame as py 
from settings import *
from support import *
from timer import Timer

class Player(py.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        self.import_assets()
        self.status = 'down_idle'
        self.frame_idx = 0
        
        # General Setup
        self.image = self.animations[self.status][self.frame_idx]
        self.rect = self.image.get_rect(center = pos)
        
        # Move the player
        self.direction = py.math.Vector2()
        self.pos = py.math.Vector2(self.rect.center)
        self.speed = 125
        
        #timers
        self.timers = {
                'tool use': Timer(350,self.use_tool),
                'tool switch': Timer(200)
        }
        
        # Tool use player
        self.tools = ['hoe', 'axe', 'water']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]
        
        # Elements used
        self.elements = ['oxygen', 'hydrogen', 'nitrogen', 'carbon']
        
        # Minerals
        self.minerals = ['scrap', 'metal', 'steel', 'crystal', 'astral']
        
    def import_assets(self):
        self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[]}
        
        for animation in self.animations.keys():
            full_path = 'Assets/character/' + animation
            self.animations[animation] = import_folder(full_path)
    
    def animatePlayer(self, dt):
        self.frame_idx += 4 * dt
        if self.frame_idx >= len(self.animations[self.status]):
            self.frame_idx = 0
        
        self.image = self.animations[self.status][int(self.frame_idx)]
    
    def use_tool(self):
        print(self.selected_tool)
       
    def input(self):
        keys = py.key.get_pressed()
        
        if not self.timers['tool use'].active:
            # Vertical Inputs
            if keys[py.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[py.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
             
            # Horizontal Inputs
            if keys[py.K_a]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[py.K_d]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0
            
            # Tool use Inputs
            if keys[py.K_SPACE]:
                self.timers['tool use'].activate()
                self.direction = pg.math.Vector2()
                self.frame_idx = 0
            
            if keys[py.K_1] and not self.timers['tool switch'].active:
                self.timers['tool switch'].activate()
                last_tool = self.tool_index
                self.tool_index = 0
                self.tool_index = self.tool_index if self.tool_index < len(self.tools) else last_tool
                self.selected_tool = self.tools[self.tool_index]
            elif keys[py.K_2] and not self.timers['tool switch'].active:
                self.timers['tool switch'].activate()
                last_tool = self.tool_index
                self.tool_index = 1
                self.tool_index = self.tool_index if self.tool_index < len(self.tools) else last_tool
                self.selected_tool = self.tools[self.tool_index]
            elif keys[py.K_3] and not self.timers['tool switch'].active:
                self.timers['tool switch'].activate()
                last_tool = self.tool_index
                self.tool_index = 2
                self.tool_index = self.tool_index if self.tool_index < len(self.tools) else last_tool
                self.selected_tool = self.tools[self.tool_index]
            elif keys[py.K_4] and not self.timers['tool switch'].active:
                self.timers['tool switch'].activate()
                last_tool = self.tool_index
                self.tool_index = 3
                self.tool_index = self.tool_index if self.tool_index < len(self.tools) else last_tool
                self.selected_tool = self.tools[self.tool_index]
                
                
    
    def get_status(self):
        # Movement Idle Check
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
            
        # Tool use status
        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool
    
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
        
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
    
    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        
        self.movePlayer(dt)
        self.animatePlayer(dt)

    