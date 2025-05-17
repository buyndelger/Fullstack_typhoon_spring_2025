import pygame
import sys 

pygame.init()

screen = pygame.display.set_mode((800 ,600,))
pygame.display.set_caption("Minii anhnii pygame")


GREEN=(144, 238, 144)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREEN)
    pygame.display.flip()



pygame.quit()
sys.exit()