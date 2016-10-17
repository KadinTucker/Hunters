from objects import *
from pygame import Surface

def buildEnemies(enemies):
    entities = []
    for i in enemies:
        entities.append(enemy(i[0], i[1], i[2], i[3]))
    return entities

class area():
    """
    An area is a plot of area on screen, with entities, sceneries, NPCs, and others.
    It also has 4 warps areas that go to different areas of the world.
    The warps are [Left, Up, Right, Down]
    """
    def __init__(self, items):
        self.enemies = buildEnemies(items[0])
        self.sceneries = items[1]
        self.bgcolor = items[4]
        self.quests = items[2]
        self.warps = items[3]
        self.scene = None

    def buildSurface(self, resolution):
        self.scene = Surface(resolution)
        self.scene.fill(self.bgcolor)
        for i in self.sceneries:
            self.scene.blit(i.image, i.coords)
        

world = {}

world['hunterland1'] = ([(bandit1[0], bandit1[1], (300, 230), bandit1[2]),
                         (bandit2[0], bandit2[1], (800, 560), bandit2[2])],
                        [],
                        [],
                        ['hunterland4', 'hunterland2', None, None], (80, 40, 10))
world['hunterland2'] = ([(bandit1[0], bandit1[1], (540, 330), bandit1[2]),
                         (bandit1[0], bandit1[1], (740, 230), bandit1[2])],
                        [],
                        [],
                        ['hunterland3', None, None, 'hunterland1'], (80, 40, 10))
world['hunterland3'] = ([(bandit2[0], bandit2[1], (200, 430), bandit2[2])],
                        [],
                        [],
                        [None, 'hunterland5', 'hunterland2', 'hunterland4'], (80, 40, 10))
world['hunterland4'] = ([(bandit1[0], bandit1[1], (400, 670), bandit1[2])],
                        [],
                        [],
                        [None, 'hunterland3', 'hunterland1', None], (80, 40, 10))
world['hunterland5'] = ([([2, 32, 200, 30, [1, 10, 30, 'sword.png', 'slash.ogg']], ['bandit1.png', 'humandeath.ogg'], (604, 602), 4), ([2, 32, 200, 30, [1, 10, 30, 'sword.png', 'slash.ogg']], ['bandit1.png', 'humandeath.ogg'], (594, 177), 4), ([2, 32, 200, 30, [1, 10, 30, 'sword.png', 'slash.ogg']], ['bandit1.png', 'humandeath.ogg'], (260, 251), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (828, 312), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (810, 556), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (202, 392), 4), ([2, 32, 200, 30, [1, 10, 30, 'sword.png', 'slash.ogg']], ['bandit1.png', 'humandeath.ogg'], (337, 553), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (78, 510), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (96, 611), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (286, 711), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (624, 754), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (233, 120), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (407, 88), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (601, 112), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (737, 122), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (740, 236), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (883, 193), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (33, 107), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (143, 78), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (281, 69), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (373, 63), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (756, 105), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (557, 89), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (676, 84), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (690, 210), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (809, 387), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (907, 487), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (908, 726), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (818, 748), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (563, 719), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (474, 731), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (307, 670), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (267, 658), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (126, 357), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (132, 408), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (146, 436), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (179, 529), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (205, 616), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (216, 713), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (224, 737), 4), ([2, 32, 200, 30, [0.9, 7, 150, 'bow.png', 'bow.ogg']], ['bandit2.png', 'humandeath.ogg'], (40, 717), 4)],
                        [],
                        [],
                        [None, 'hunterland3', 'hunterland1', 'hunterland4'], (80, 40, 10))
