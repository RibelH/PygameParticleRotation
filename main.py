import pygame
import sys
import math
import random
pygame.init()

size = width, height = 1300, 720
screen = pygame.display.set_mode(size)
WHITE = [255,255,255]
GREY = [128,128,128]
DARK_GREY = [80,80,80]
pos = [600, 200]
Center = [600, 400]
inner_pos = [750, 200]

#img = pygame.image.load("frontgate.jpeg")
#screen.blit(img,(100,100))
def rotate(pos, angle, center):


    new_x = (pos[0] - center[0]) * math.cos(angle) - (pos[1]- center[1]) * math.sin(angle)
    new_y = (pos[0]- center[0]) * math.sin(angle) + (pos[1]- center[1]) * math.cos(angle)

    return [new_x+center[0], new_y + center[1]]


def RedrawWindow():
    screen.fill((0,0,0))





mainClock = pygame.time.Clock()
run = True
particles = []
while run:
    mainClock.tick(60)
    particles.append([[pos[0], pos[1]], 10, random.randint(-1,1), "planet"])
    particles.append([[inner_pos[0], inner_pos[1]], 5, random.randint(-1,1), "moon"])
    for event in pygame.event.get():

        # Quit event
        if event.type == pygame.QUIT:
            run = False
    RedrawWindow()
    for particle in particles:

        particle[1] -= 1
        particle[0][1] -= particle[2]/2
        particle[0][0] -= particle[2]/2
        if particle[3] == "planet":
            pygame.draw.circle(screen, WHITE, [particle[0][0], particle[0][1]], particle[1])
        else:
            pygame.draw.circle(screen, DARK_GREY, [particle[0][0], particle[0][1]], particle[1])
        if particle[1] <= 0:
            particles.remove(particle)

    #ROTATE POINT ON GRID
    #x' = (cos(a) * x) + (-sin(a) * y)
    #y' = (sin(a) * x) + (cos(a) * y)


    #pygame.draw.polygon(screen, WHITE, [(154, 209), (254, 239), (354, 209), (254, 179) ], width=0)
    #pygame.draw.polygon(screen, GREY, [(154, 209), (154, 289), (254, 319), (254, 239) ], width=0)
    #pygame.draw.polygon(screen, DARK_GREY, [(354, 209), (354, 289), (254, 319), (254, 239)], width=0)

    new_pos = rotate(pos, 0.025, Center)


    inner_pos = (inner_pos[0] - (pos[0]-new_pos[0]), inner_pos[1] - (pos[1]-new_pos[1]))
    pos = new_pos
    inner_pos = rotate(inner_pos,  -0.1, pos)
    pygame.draw.circle(screen, DARK_GREY, inner_pos , 5)
    pygame.draw.circle(screen, WHITE, pos, 10)




    pygame.display.update()

pygame.quit()