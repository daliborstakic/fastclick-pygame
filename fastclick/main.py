""" Importing pygame """
from random import randint
import pygame
""" Importing Circle class """
from fastclick.circle import Circle

# Initializing pygame
pygame.init()

# Screen parameters
WIDTH = 500

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def is_clicked(pos, circle):
    """ If the mouse clicked on the circle """
    x, y = pos

    if circle.x > x > circle.x + circle.radius and circle.y > y > circle.y + circle.radius:
        return True

    return False

def random_circle():
    """ Returns a circle on a random location """

    # Circle parameters
    radius = randint(10, 30)

    x = randint(radius, WIDTH - radius)
    y = randint(radius, WIDTH - radius)

    return Circle(x, y, radius)

def draw(surface):
    """ Renders the screen """
    surface.fill(WHITE)

    pygame.display.update()

def main(surface):
    """ Main function """
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(surface)

    pygame.quit()

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Fast Clicker")

if __name__ == '__main__':
    main(win)
