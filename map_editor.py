import pygame
from pygame.locals import *
import sys
import objects
import math

pygame.init()

display = pygame.display.set_mode((1000, 800))

objs = [objects.bandit1, objects.bandit2]

enemies = []

def save():
    world = open('savedworld.txt', 'w')
    world.write(str(enemies))

while True:
    display.fill((75, 35, 35))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if event.button == 1:
                enemies.append((objs[0][0], objs[0][1], mouse, objs[0][2]))
            elif event.button == 3:
                for i in enemies:
                    if math.hypot(mouse[0] - (i[2][0] + 32), mouse[1] - (i[2][1] + 32)) <= 48:
                        enemies.remove(i)
        elif event.type == KEYDOWN:
            if event.key == K_TAB:
                objs.append(objs[0])
                objs.remove(objs[0])
            elif event.key == K_s:
                save()
    for i in enemies:
        display.blit(pygame.image.load(i[1][0]), i[2])
    pygame.display.update()
