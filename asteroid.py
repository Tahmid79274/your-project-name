import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            movement1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            movement2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteriod1 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteriod2 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteriod1.velocity = movement1 * 1.2
            new_asteriod2.velocity = movement2 * 1.2
            
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    
    def update(self,dt):
        self.position+=(self.velocity * dt)
