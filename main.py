import pygame
import math
import random
import time

# Initialization
pygame.init()

# Screen
screen = pygame.display.set_mode((1000, 667))

# Background
bg = pygame.image.load("427.jpg")

# Title and Icon
pygame.display.set_caption("Bouncing Ball")
icon = pygame.image.load("ball icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("volleyball-ball.png")
playerX = 230
playerY = 480
playerX_change = 0
playerY_change = 0

# Coin
coinImg = pygame.image.load("coin 24.png")
coinX = random.randint(0, 936)
coinY = random.randint(50, 600)
coin_timer = time.time()

# Enemy
enemyImg = pygame.image.load("chick.png")
enemyX = random.randint(0, 936)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def coin(x, y):
    screen.blit(coinImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def is_collision(objX, objY, playerX, playerY):
    distance = math.sqrt(math.pow(objX - playerX, 2) + math.pow(objY - playerY, 2))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    if playerY <= 0:
        playerY = 0
    elif playerY >= 600:
        playerY = 600

    # Movement of Enemy
    enemyX += enemyX_change
    enemyY += enemyY_change

    if enemyX <= 0:
        enemyX_change = 0.3
    elif enemyX >= 936:
        enemyX_change = -0.3

    if enemyY <= 0:
        enemyY_change = 0.3
    elif enemyY >= 600:
        enemyY_change = -0.3

    # Collision with Enemy
    collision_with_enemy = is_collision(enemyX, enemyY, playerX, playerY)
    if collision_with_enemy:
        playerX = 480
        score_value += 1

    # Collision with Coin
    collision_with_coin = is_collision(coinX, coinY, playerX, playerY)
    if collision_with_coin:
        score_value += 5
        coinX = random.randint(0, 936)
        coinY = random.randint(50, 600)
        coin_timer = time.time()

    # Change coin position every 5 seconds if not hit
    if time.time() - coin_timer > 5:
        coinX = random.randint(0, 936)
        coinY = random.randint(50, 600)
        coin_timer = time.time()

    player(playerX, playerY)
    coin(coinX, coinY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)
    pygame.display.update()
