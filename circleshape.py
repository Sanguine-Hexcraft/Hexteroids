import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collisions(self, other):
        # Distance is the first objects' position (x, y) 
        # calculated to the second objects' distance (x, y)
        distance = self.position.distance_to(other.position)
        # If distance is less than or equal to r1 + r2, 
        # the circles are colliding. If not, they aren't.
        if distance <= self.radius + other.radius:
            return True
        return False    
