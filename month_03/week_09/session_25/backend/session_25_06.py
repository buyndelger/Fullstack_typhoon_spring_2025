import pygame 
import sys
import random


pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("mouse interration")

WHITE =(255, 255, 255)
BLACK =(0,0,0)

circles =[]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                color = (
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255),
                )
                circles.append({
                    "pos": event.pos,
                    "radius": random.randint(10,50),
                    "color" : color
                })

            if event.button == 3:
                circles =[]

    screen.fill(WHITE)
    for circle in circles:
        pygame.draw.circle(screen, circle["color"], circle["pos"], circle["radius"])


    font = pygame.font.Font(None, 24)
    text = font.render("Left click: Add circle | Right click: Clear all" , True, BLACK)
    screen.blit(text, (10,10))
    pygame.display.flip()

pygame.quit()
sys.exit()
