import objects
from pygame import Surface

def buildEnemies(enemies):
    entities = []
    for i in enemies:
        entities.append(objects.enemy(i[0], i[1], i[2]))
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

world['hunterland1'] = ([(objects.soldier[0], objects.soldier[1], (300, 230)), (objects.soldier[0], objects.soldier[1], (800, 560))], [], [], ['hunterland4', 'hunterland2', None, None], (80, 40, 10))
world['hunterland2'] = ([(objects.soldier[0], objects.soldier[1], (540, 330))], [], [], ['hunterland3', None, None, 'hunterland1'], (80, 40, 10))
world['hunterland3'] = ([(objects.soldier[0], objects.soldier[1], (200, 430))], [], [], [None, None, 'hunterland2', 'hunterland4'], (80, 40, 10))
world['hunterland4'] = ([(objects.soldier[0], objects.soldier[1], (100, 730))], [], [], [None, 'hunterland3', 'hunterland1', None], (80, 40, 10))
