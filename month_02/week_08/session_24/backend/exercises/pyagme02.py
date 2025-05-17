import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Дүрс зурах")

# Өнгөнүүд тодорхойлох
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (400, 300), 50)

    pygame.draw.rect(screen, BLUE, (200, 200, 100, 100))


    pygame.draw.line(screen, GREEN, (100, 100), (700, 500), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()