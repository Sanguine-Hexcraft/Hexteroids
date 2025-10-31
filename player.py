import pygame
from constants import *
from circleshape import *

class Player(CircleShape):
    # initiate the parent class CircleShape from circleshape
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]# in the player class

    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_a]:
            # call the rotate method with keypress = a, moves the spaceship counter clockwise
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # call the rotate method with keypress = d, moves the spaceship clockwise
            self.rotate(dt)
        if keys[pygame.K_w]:
            # call the move method with keypress = w, moves teh spacehip forward
            self.move(dt)
        if keys[pygame.K_s]:
            # call the move method with keypress - d, move the spacehip backwards
            self.move(-dt)
        
