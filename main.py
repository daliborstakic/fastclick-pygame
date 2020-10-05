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

# Creating the highscore file if it doesn't exist
with open('highscores.txt', 'a+', newline='\n') as score_file:
    pass

# Font
text_font = pygame.font.SysFont('Arial', 30)
end_font = pygame.font.SysFont('Arial', 20)

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

def draw(surface, circle, score, seconds, highscore):
    """ Renders the screen """
    surface.fill(WHITE)

    # Draws the circle
    circle.draw(surface)

    # Score
    score_text = text_font.render(f"Score: {score}", 1, BLACK)
    surface.blit(score_text, (10, 10))

    # High score
    high_text = end_font.render(f"High score: {highscore}", 1, BLACK)
    surface.blit(high_text, ((WIDTH // 2 - high_text.get_width() // 2), 5 + score_text.get_height() - high_text.get_height()))

    # Time
    time_text = text_font.render(f"Time: {seconds}", 1, BLACK)
    surface.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))

    pygame.display.update()

def display_end_result(surface, seconds, score):
    """ Displays the result when the time reaches 30 seconds """

    # Number of clicks per minute
    speed = round(score / seconds, 2)

    # Rendering the screen
    surface.fill(WHITE)

    end_text = end_font.render(f"Your speed was {speed} clicks per second.", 1, BLACK)
    surface.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))

    pygame.display.update()

    # End the function after a second
    pygame.time.delay(1000)

def get_high_score():
    with open('highscores.txt', 'r') as score_file:   
        scores = [line for line in score_file.readlines()]

    if not scores:
        return 0

    return max(scores)

def write_score(score, seconds):
    with open('highscores.txt', 'a') as score_file:
        score_file.write(f"{round(score / seconds, 2)}\n")

def main(surface):
    """ Main function """
    run = True

    # Game variables
    circle = random_circle()
    score = 0
    highscore = get_high_score().strip()

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

        draw(surface, circle, score, seconds, highscore)

        if seconds >= 30:
            display_end_result(surface, seconds, score)
            write_score(score, seconds)
            run = False

    pygame.quit()

# Screen init
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Fast Clicker")

if __name__ == '__main__':
    main(win)
