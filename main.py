""" Importing pygame """
import pygame
""" Importing randint method """
from random import randint
""" Importing Circle class """
from fastclick.circle import Circle
""" Distance calculation """
from math import hypot

# Initializing pygame
pygame.init()

# Screen parameters
WIDTH = 500

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
text_font = pygame.font.SysFont('Arial', 30)

def is_clicked(pos, circle):
    """ If the mouse clicked on the circle """
    x, y = pos

    # Distance to the center
    distance = hypot(x - circle.x, y - circle.y)

    if distance <= circle.radius:
        return True

    return False

def random_circle():
    """ Returns a circle on a random location """

    # Circle parameters
    radius = randint(10, 20)

    x = randint(radius, WIDTH - radius)
    y = randint(radius, WIDTH - radius)

    return Circle(x, y, radius)

def draw(surface, circle, score, seconds):
    """ Renders the screen """
    surface.fill(WHITE)

    # Draws the circle
    circle.draw(surface)

    # Score
    score_text = text_font.render(f"Score: {score}", 1, BLACK)
    surface.blit(score_text, (10, 10))

    # Time
    time_text = text_font.render(f"Time: {seconds}", 1, BLACK)
    surface.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))

    pygame.display.update()

def main(surface):
    """ Main function """
    run = True

    # Game variables
    circle = random_circle()
    score = 0

    # Start ticks
    start_ticks = pygame.time.get_ticks()

    while run:
        # Counting seconds
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                if is_clicked(pos, circle):
                    circle = random_circle()
                    score += 1

        draw(surface, circle, score, seconds)

    pygame.quit()

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Fast Clicker")

if __name__ == '__main__':
    main(win)
