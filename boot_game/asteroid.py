import pygame

import random

from circleshape import*

from constants import*

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    
    def update(self, dt):
        
        self.position += self.velocity * dt

    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_num = random.uniform(20, 50)

        Vect_1 = pygame.math.Vector2.rotate(self.velocity, random_num)
        Vect_2 = pygame.math.Vector2.rotate(self.velocity, -random_num)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = Vect_1 * 1.2
        asteroid_2.velocity = Vect_2 * 1.2