""" Importing pygame """
import pygame

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

def draw(surface):
    pass

def main(surface):
    pass

if __name__ == '__main__':
    main()
