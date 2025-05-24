import pygame 
import sys


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving Rectangle")



WHITE = (255, 255, 255)
RED =(255, 0,0)


rect_x = 300
rect_y= 200
rect_widht= 50
rect_height= 50
rect_speed =5

clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False


    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT] and rect_x < 640 - rect_widht:
        rect_x += rect_speed
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN] and rect_y < 400:
        rect_y += rect_speed


    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_widht , rect_height))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit