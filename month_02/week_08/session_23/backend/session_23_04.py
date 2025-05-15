import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH ,HEIGHT))
pygame.display.set_caption("My Pygame window")

WHITE = (255,255, 255)
BLACK =(0,0,0)
RED =(255, 0,0)
GREEN=(0,255,0)
BLUE =(0,0,255)




clock = pygame.time.Clock()
running =True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (400, 300),50)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()