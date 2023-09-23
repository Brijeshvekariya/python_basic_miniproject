import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 7
score = 0
highscore = 0
font = pygame.font.Font(None, 36)
# Colors
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Load a background image
background_image = pygame.image.load("assets\\BG.png")  # Replace "assets\\BG.png" with your image file path

# Scale the background image to match the screen size
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Define the reset button's position and dimensions
reset_button_rect = pygame.Rect(335, 394, 100, 40)
reset_button = False

# pygame.display.get_caption(f"Score : {score}")

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Initialize paddle positions
left_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Initialize ball position
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

# Ball direction
ball_dx = BALL_SPEED * random.choice((1, -1))
ball_dy = BALL_SPEED * random.choice((1, -1))

clock = pygame.time.Clock()
running = True
game_over = False  # Track if the game is over

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check for mouse-click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button (1) clicked
                if reset_button and reset_button_rect.collidepoint(event.pos):
                    # Reset the game
                    score = 0
                    ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
                    reset_button = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    if not game_over:
        # Move the ball only if the game is not over
        ball.x += ball_dx
        ball.y += ball_dy

        # Ball collisions with walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy *= -1

        # Ball collisions with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_dx *= -1
            score += 1
            if highscore < score:
                highscore = score

        # Ball out of bounds
        if ball.left <= 0 or ball.right >= WIDTH:
            score -= 1
            game_over = True  # Set game over when the ball goes out of bounds
            reset_button = True  # Show the reset button

    # Draw the background image first
    screen.blit(background_image, (0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw the reset button if it's visible
    if reset_button:
        pygame.draw.rect(screen, (0, 128, 255), reset_button_rect)  # Button color
        reset_button_text = font.render("Reset", True, WHITE)  # Button text
        screen.blit(reset_button_text, (350, 400))  # Position the text

    # Display current score
    score_surface = font.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

    highscore_surface = font.render(f"High Score: {highscore}", True, WHITE)
    screen.blit(highscore_surface, (10, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
