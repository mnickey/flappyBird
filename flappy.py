#! /usr/bin/python3
import pygame
import time
from random import randint, randrange

black = (0, 0, 0)
white = (255, 255, 255)
sunset = (253, 72, 47)
greenyellow = (184, 255, 0)
brightblue = (47, 228, 253)
orange = (255, 236, 0)
yellow = (255, 236, 0)
purple = (252, 67, 255)

color_choices = [greenyellow, brightblue, orange, yellow, purple]

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 43
imageWidth = 100

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

img = pygame.image.load('Helicopter.png')

def score(count):
    font = pygame.font.SysFont('freesansbold.ttf', 20)
    # font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(count), True, white)
    surface.blit(text, [0,0])

def blocks(x_block, y_block, block_width, block_height, gap, colorChoice):
    pygame.draw.rect(surface, colorChoice, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, colorChoice, [x_block, y_block+block_height+gap, block_width, surfaceHeight])

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    smallText = pygame.font.SysFont('freesansbold.tff', 20)
    largeText = pygame.font.SysFont('freesansbold.tff', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) )

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()
    main()

def gameOver():
    msgSurface('KaBoom!')

def helicopter(x, y, image):
    surface.blit(img, (x, y))

def main():
    x = 150
    y = 200
    y_move = 0
    x_block = surfaceWidth
    y_block = 0
    block_width = 75
    block_height = randint(0, surfaceHeight/2)
    gap = imageHeight * 3
    block_move = 4
    current_score = 0
    blockColor = color_choices[randrange(0, len(color_choices))]
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
        y += y_move
        surface.fill(black)
        helicopter(x, y, img)

        blocks(x_block, y_block, block_width, block_height, gap, blockColor)
        score(current_score)
        x_block -= block_move

        if x_block < (-1 * block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight / 2))
            blockColor = color_choices[randrange(0, len(color_choices))]
            current_score += 1

        if x + imageWidth > x_block:
            if y + imageHeight > block_height + gap:
                if x < block_width + x_block:
                    gameOver()

        if 3 <= current_score < 5:
            block_move = 5
            gap = imageHeight * 2.9
        if 5 <= current_score < 8:
            block_move = 6
            gap = imageHeight * 2.8
        if 8 <= current_score < 14:
            block_move = 7
            gap = imageHeight * 2.7

        pygame.display.update()
        clock.tick()

if __name__ == '__main__':
    main()
    pygame.quit()
    quit()