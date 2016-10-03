import pygame

class weapon():
    def __init__(self, stats):
        self.atkspd = stats[0]
        self.damage = stats[1]
        self.range = stats[2]
        self.image = pygame.image.load(stats[3])
        self.sound = pygame.mixer.Sound(stats[4])

crossbow = [0.55, 16, 500, 'crossbow.png', 'crossbow.ogg']
spear = [0.9, 25, 55, 'spear.png', 'spear.ogg']
sword = [1, 10, 30, 'crossbow.png', 'slash.ogg']
