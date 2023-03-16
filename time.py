import pygame
import datetime

pygame.init()

# Set up the display window
screen = pygame.display.set_mode((400, 400))

# Set up the ball
ball_color = (255, 0, 0)
ball_radius = 20
ball_pos = [200, 200]
ball_speed = 100  # pixels per second

# Set up the clock
clock = pygame.time.Clock()

# Start the main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Calculate the time elapsed since the last frame
    delta_time = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

    # Update the ball position based on the current time
    current_time = datetime.datetime.now().time()
    ball_pos[0] = int(200 + ball_speed * (current_time.second + current_time.microsecond / 1000000.0))

    # Draw the ball
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.display.update()
