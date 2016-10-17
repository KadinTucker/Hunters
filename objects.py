import math
import pygame
import equipment

pygame.mixer.init()

class scenery():
    """
    An object of scenery, can be solid or non-solid.
    Takes in an image filename, and dimensions.
    """
    def __init__(self, image, dimensions, solid, coords):
        self.dimensions = dimensions
        self.image = pygame.image.load(image)
        self.coords = coords
        self.solid = solid

class entity(object):
    """
    A class of an entity to be the player, a projectile, or an enemy.

    Takes in a list of stats, displays. coordinates.
    """
    def __init__(self, stats, displays, coords):
        self.coords = coords
        self.target = coords
        self.entity_target = None
        self.frozen = False
        self.movements = (0, 0)
        self.speed = stats[0]
        self.size = stats[1]
        self.image = pygame.image.load(displays[0])
        self.deathsound = pygame.mixer.Sound(displays[1])
        
    def path(self):
        """
        Find the movements (x, y) needed to get toward the target location.
        If frozen, this does not happen.
        """
        if not self.frozen and self.speed != 0:
            xdist = self.coords[0] - self.target[0]
            ydist = self.coords[1] - self.target[1]
            distance = math.hypot(abs(xdist), abs(ydist))
            if distance < 5:
                self.movements = (0, 0)
            else:
                xmove = ((self.speed * xdist)/distance) * -1
                ymove = ((self.speed * ydist)/distance) * -1
                self.movements = (xmove, ymove)
        else:
            self.movements = (0, 0)
            
    def collision(self, room):
        testptdown = (self.coords[0], self.coords[1] + self.size)
        testptup = (self.coords[0], self.coords[1] - self.size)
        testptleft = (self.coords[0] - self.size, self.coords[1])
        testptright = (self.coords[0] + self.size, self.coords[1])
        for obj in room.sceneries:
                if obj.solid:
                    if testptdown[0] - obj.coords[0] >= 0 and testptdown[0] - obj.coords[0] <= obj.dimensions[0]:
                        if testptdown[1] - obj.coords[1] >= 0 and testptdown[1] - obj.coords[1] <= obj.dimensions[1]:
                            self.coords =  (self.coords[0], obj.coords[1] - self.size)
                    if testptup[0] - obj.coords[0] >= 0 and testptup[0] - obj.coords[0] <= obj.dimensions[0]:
                        if testptup[1] - obj.coords[1] >= 0 and testptup[1] - obj.coords[1] <= obj.dimensions[1]:
                            self.coords =  (self.coords[0], obj.coords[1] + obj.dimensions[1] + self.size)
                    if testptleft[1] - obj.coords[1] >= 0 and testptleft[1] - obj.coords[1] <= obj.dimensions[1]:
                        if testptleft[0] - obj.coords[0] >= 0 and testptleft[0] - obj.coords[0] <= obj.dimensions[0]:
                            self.coords =  (obj.coords[0] + obj.dimensions[0] + self.size, self.coords[1])
                    if testptright[1] - obj.coords[1] >= 0 and testptright[1] - obj.coords[1] <= obj.dimensions[1]:
                        if testptright[0] - obj.coords[0] >= 0 and testptright[0] - obj.coords[0] <= obj.dimensions[0]:
                            self.coords =  (obj.coords[0] - self.size, self.coords[1])
        
    def move(self):
        if self.entity_target != None:
            self.target = self.entity_target.coords
        else:
            self.frozen = False
        self.path()
        self.coords = (self.coords[0] + self.movements[0], self.coords[1] + self.movements[1])
        if self.movements == (0, 0):
            self.target = self.coords

    def target_entity(self, room):
        mousepos = pygame.mouse.get_pos()
        for i in room.enemies:
            if i.alive:
                cdistance = math.hypot(i.coords[0] - mousepos[0], i.coords[1] - mousepos[1])
                #print(cdistance)
                if cdistance <= i.size:
                    return i
        return None

    

class player(entity):
    """
    The player.
    """
    def __init__(self, stats, displays, coords):
        super(player, self).__init__(stats, displays, coords)
        self.hpmax = stats[2]
        self.hp = self.hpmax
        self.atktick = 0
        self.tick = 0
        self.regentick = 0
        self.equipment = []
        self.temphp = self.hpmax
        self.kills = 0
        
    def attack(self):
        if self.entity_target != None:
            distance = math.hypot(self.entity_target.coords[0] - self.coords[0], self.entity_target.coords[1] - self.coords[1])
            if distance <= self.equipment[0].range:
                self.frozen = True
                self.tick += self.equipment[0].atkspd
                if self.tick >= 200:
                    self.entity_target.hp -= self.equipment[0].get_damage()
                    self.equipment[0].sound.play()
                    self.tick -= 200
                    self.entity_target.target = self.coords
            else:
                self.frozen = False
        else:
            self.tick = 0

    def target_location(self, room):
##        mouse = pygame.mouse.get_pos()
##        for obj in room.sceneries:
##            if mouse[0] - obj.coords[0] <= obj.dimensions[0] and mouse[0] - obj.coords[0] >= 0:
##                if mouse[1] - obj.coords[1] <= obj.dimensions[1] and mouse[1] - obj.coords[1] >= 0:
##                    return
        self.target = pygame.mouse.get_pos()
        self.entity_target = None

    def switch_weapon(self):
        self.equipment.append(self.equipment[0])
        self.equipment.remove(self.equipment[0])
        self.tick = 0

    def test_death(self):
        if self.hp <= 0:
            return True

    def regenerate(self):
        self.regentick += 1
        if self.regentick >= 300:
            self.hp += 1
            if self.hp > self.hpmax:
                self.hp = self.hpmax
            self.regentick = 0

class enemy(entity):
    """
    An enemy to be fought by the player.
    Takes in a list of stats, a list of displays, and some coords.
    atktick is the ticking of attacking rate.
    Temphp is used to determine whether the enemy has taken damage.
    """
    def __init__(self, stats, displays, coords, exp):
        super(enemy, self).__init__(stats, displays, coords)
        self.sight = stats[2]
        self.hpmax = stats[3]
        self.hp = self.hpmax
        self.tick = 0
        self.resetTick = 0
        self.equipment = equipment.weapon(stats[4])
        self.temphp = self.hpmax
        self.origin = coords
        self.alive = True
        self.exp = exp
        
    def AI(self, PLAYER):
        distance = math.hypot(PLAYER.coords[0] - self.coords[0], PLAYER.coords[1] - self.coords[1])
        if distance <= self.sight:
            self.entity_target = PLAYER
        else:
            self.resetTick += 1
            self.entity_target = None
##            if self.resetTick >= 500:
##                self.entity_target = None
##                self.target = self.origin
##                self.resetTick = 0
##        if self.temphp < self.hp:
##            print('CONSOLE: Entity hit detected.')
##            self.target = PLAYER.coords
##            self.temphp = self.hp

    def attack(self, TPS):
        if self.entity_target != None:
            distance = math.hypot(self.entity_target.coords[0] - self.coords[0], self.entity_target.coords[1] - self.coords[1])
            if distance <= self.equipment.range:
                self.frozen = True
                self.tick += self.equipment.atkspd
                if self.tick >= TPS:
                    self.entity_target.hp -= self.equipment.damage
                    self.equipment.sound.play()
                    self.tick -= TPS
            else:
                self.frozen = False
        else:
            self.tick = 0

    def checkDeath(self, PLAYER):
        if self.hp <= 0:
            self.deathsound.play()
            self.alive = False
            PLAYER.entity_target = None
            PLAYER.kills += 1
            PLAYER.equipment[0].exp += self.exp
            PLAYER.equipment[0].levelup()

    def show_hp(self, display):
        length = (35 * self.hp)/self.hpmax
        gbar2 = pygame.transform.smoothscale(pygame.image.load('gbar.png'), (length, 10))
        display.blit(pygame.image.load('rbar.png'), (self.coords[0] - 17, self.coords[1] - 36))
        display.blit(gbar2, (self.coords[0] - 17, self.coords[1] - 36))
            
    
bandit1 = [[2, 32, 200, 30, equipment.banditSword], ['bandit1.png', 'humandeath.ogg'], 4]
bandit2 = [[2, 32, 200, 30, equipment.banditBow], ['bandit2.png', 'humandeath.ogg'], 4]



