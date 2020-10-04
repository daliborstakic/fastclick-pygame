from pygame.draw import circle
from random import choice

class Circle():
    def __init__(self, x, y, radius) -> None:
        """ Init method """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])

    def draw(self, surface):
        """ Draws the circle """
        circle(surface, self.color, (self.x, self.y), self.radius)
