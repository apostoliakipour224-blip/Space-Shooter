import pygame
import random

# Initialize game
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
PURPLE = (138, 43, 226)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)

# Clock for frame rate
clock = pygame.time.Clock()

# Player (Spaceship)
player_x = WIDTH // 2 - 20
player_y = HEIGHT - 80
player_speed = 5

# Bullets & Enemies lists
bullets = []
enemies = []

# Score
score = 0
font = pygame.font.SysFont(None, 30)

# Spawn initial enemies
for _ in range(5):
    enemies.append({"x": random.randint(30, WIDTH - 30), "y": random.randint(-400, -50), "speed": random.randint(2, 4)})

# Main Game Loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot bullet from player center
                bullets.append({"x": player_x + 18, "y": player_y})

    # Continuous movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 40:
        player_x += player_speed

    # Update Bullets
    for bullet in bullets[:]:
        bullet["y"] -= 10
        if bullet["y"] < 0:
            bullets.remove(bullet)

    # Update Enemies
    for enemy in enemies[:]:
        enemy["y"] += enemy["speed"]
        if enemy["y"] > HEIGHT:
            enemy["y"] = random.randint(-400, -50)
            enemy["x"] = random.randint(30, WIDTH - 30)

        # Check collision with bullets
        for bullet in bullets[:]:
            if abs(enemy["x"] - bullet["x"]) < 25 and abs(enemy["y"] - bullet["y"]) < 25:
                score += 1
                enemies.remove(enemy)
                bullets.remove(bullet)
                # Respawn new enemy
                enemies.append({"x": random.randint(30, WIDTH - 30), "y": random.randint(-200, -50), "speed": random.randint(2, 4)})

    # Draw Player (Spaceship as a triangle)
    pygame.draw.polygon(screen, CYAN, [(player_x + 20, player_y), (player_x, player_y + 40), (player_x + 40, player_y + 40)])

    # Draw Bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet["x"], bullet["y"], 4, 10))

    # Draw Enemies
    for enemy in enemies:
        pygame.draw.polygon(screen, RED, [(enemy["x"], enemy["y"] + 20), (enemy["x"] - 15, enemy["y"]), (enemy["x"] + 15, enemy["y"])])

    # Draw Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()