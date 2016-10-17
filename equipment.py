import pygame

class weapon():
    def __init__(self, stats, level=1):
        self.atkspd = stats[0]
        self.damage = stats[1]
        self.range = stats[2]
        self.image = pygame.image.load(stats[3])
        self.sound = pygame.mixer.Sound(stats[4])
        self.exp = 0
        self.level = level

    def levelup(self):
        if self.exp >= (2**self.level) + (self.level * 10) + 6:
            self.exp -= (2**self.level) + (self.level * 10) + 6
            print('CONSOLE: Equipment item has leveled up.')
            self.level += 1

    def get_damage(self):
        return self.damage*self.level

crossbow = [0.8, 10, 500, 'crossbow.png', 'crossbow.ogg']
bow = [1, 10, 300, 'bow.png', 'bow.ogg']
knives = [2, 5, 300, 'knife.png', 'knives.ogg']
spear = [1, 7, 90, 'spear.png', 'spear.ogg']
sword = [2, 7, 30, 'sword.png', 'slash.ogg']
axe = [0.8, 14, 30, 'axe.png', 'axe.ogg']

banditSword = [1, 10, 30, 'sword.png', 'slash.ogg']
banditBow = [0.9, 7, 150, 'bow.png', 'bow.ogg']

