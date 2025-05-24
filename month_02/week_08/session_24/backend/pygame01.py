import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640 ,480,))
pygame.display.set_caption("my name")



running  = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False


    screen.fill((0,128,255))

    pygame.display.flip()


pygame.quit()
sys.exit()