import sys
import pygame

from pygame import QUIT

# Colors
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
bgcolor = white

# Dimensions
width = 800
height = 600
widthCenter = int(width / 2)
heightCenter = int(height / 2)
posCenter = (widthCenter, heightCenter)
circleRadius = 100
offset = (100, 100)

polyPos = [(widthCenter, heightCenter - circleRadius),
           (widthCenter + circleRadius, heightCenter),
           (widthCenter, heightCenter + circleRadius),
           (widthCenter - circleRadius, heightCenter)]

# Set up
framerate = 5
screen = pygame.display.set_mode((width, height))
screen.fill(bgcolor)
clock = pygame.time.Clock()

# Drawing
pygame.draw.circle(screen, blue, posCenter, circleRadius, 3)
pygame.draw.polygon(screen, red, polyPos, 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    newWidthCenter = widthCenter + offset[0]
    newHeightCenter = heightCenter + offset[1]
    newPosCenter = (newWidthCenter, newHeightCenter)
    newPolyPos = [(newWidthCenter, newHeightCenter - circleRadius),
                  (newWidthCenter + circleRadius, newHeightCenter),
                  (newWidthCenter, newHeightCenter + circleRadius),
                  (newWidthCenter - circleRadius, newHeightCenter)]

    # Rendering
    pygame.draw.circle(screen, blue, newPosCenter, circleRadius, 3)
    pygame.draw.polygon(screen, red, newPolyPos, 3)

    pygame.display.flip()
    clock.tick(framerate)
