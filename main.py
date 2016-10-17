import random
import pygame
from pygame.locals import *
import sys
try:
    import objects
    import world
    import equipment
except:
    print('CONSOLE: Missing required modules. Terminating...')

IMAGES = {'uarrowImg' : pygame.image.load('warparrow.png'), 'larrowImg' : pygame.transform.rotate(pygame.image.load('warparrow.png'), 90), 'darrowImg' : pygame.transform.rotate(pygame.image.load('warparrow.png'), 180), 'rarrowImg' : pygame.transform.rotate(pygame.image.load('warparrow.png'), 270)}

MUSIC = {'Music' : 'Huntermarch.mp3'}

TPS = 200
CLOCK = pygame.time.Clock()

RES = (1000, 800)

def terminate():
    """
    Stop all functions of the program.
    """
    pygame.quit()
    sys.exit()

def checkWarp(room):
    if PLAYER.coords[0] > RES[0] / 2 - 45 and PLAYER.coords[0] < RES[0] / 2 + 45:
        if PLAYER.coords[1] < 30 and room.warps[1] != None:
            room = world.area(world.world[room.warps[1]])
            room.buildSurface(resolution)
            PLAYER.coords = (RES[0] / 2, RES[1] - 90)
            PLAYER.target = (RES[0] / 2, RES[1] - 90)
        elif PLAYER.coords[1] > RES[1] - 30 and room.warps[3] != None:
            room = world.area(world.world[room.warps[3]])
            room.buildSurface(resolution)
            PLAYER.coords = (RES[0] / 2, 90)
            PLAYER.target = (RES[0] / 2, 90)
    elif PLAYER.coords[1] > RES[1] / 2 - 45 and PLAYER.coords[1] < RES[1] / 2 + 45:
        if PLAYER.coords[0] < 30 and room.warps[0] != None:
            room = world.area(world.world[room.warps[0]])
            room.buildSurface(resolution)
            PLAYER.coords = (RES[0] - 90, RES[1] / 2)
            PLAYER.target = (RES[0] - 90, RES[1] / 2)
        elif PLAYER.coords[0] > RES[0] - 30 and room.warps[2] != None:
            room = world.area(world.world[room.warps[2]])
            room.buildSurface(resolution)
            PLAYER.coords = (90, RES[1] / 2)
            PLAYER.target = (90, RES[1] / 2)
    return room

class button():
    """
    A button class to have a width and coordinates. Also has a pressed state.

    Takes in location, which is the location of the button.
    Takes in button ID, which determines where the button takes you when pressing it.
    Takes in image, the image in which it displays on the screen.
    """
    def __init__(self, location, identity, image, size):
        self.location = location
        self.identity = identity
        self.image = image
        self.pressed = False
        self.active = False
        self.size = size
        
    def buttonPressed(self):
        """
        Checks whether or not a button has been clicked.

        Returns a slightly modified list of buttons, modifying whether or not the button has been pressed.
        """
        mouse = pygame.mouse.get_pos()
        print('CONSOLE: Clicked at point '+str(mouse))
        if mouse[0] - self.location[0] <= self.size[0] and mouse[0] - self.location[0] >= 0:
            if mouse[1] - self.location[1] <= self.size[1] and mouse[1] - self.location[1] >= 0:
                self.pressed = True
                print('CONSOLE: Button of ID %s has been pressed.' % self.identity)
    def displayButtons(self, display):
        """
        Displays the button on the screen as self.image. All button images should be 200px X 50px
        to have proper dimensions.

        Takes in the main game display screen.
        """
        if self.active:
            display.blit(self.image, self.location)

def checkButtons(gamestate):
    """
    Checks whether the ID of all buttons being pressed checks out with any pre-determined functions
    of specific buttons. If the function goes through and nothing happens, the button becomes un-pressed.

    Takes in the list of all buttons.

    Ex: A 'quit' button will terminate the game when pressed (game state 0).

    Returns the new game state.
    """
    for b in buttons:
        i = buttons[b]
        if i.active:
            if i.pressed:
                print('CONSOLE: Active button has been pressed.')
                if i.identity == 'quit':
                    print('CONSOLE: Quit Button pressed.')
                    return 0
                    print('ERROR: Quit not gone through.')
                if i.identity == 'play':
                    print('CONSOLE: Play button pressed.')
                    #setMusic('Janon', 0)
                    buttons['menuQuit'].active = False
                    buttons['menuPlay'].active = False
                    buttons['menuTitle'].active = False

                    buttons['wpchCrossbow'].active = True
                    buttons['wpchBow'].active = True
                    buttons['wpchKnife'].active = True
                    buttons['wpchSword'].active = True
                    buttons['wpchSpear'].active = True
                    buttons['wpchAxe'].active = True
                    return 4

                
                #weapon choices

                
                elif i.identity == 'bow':
                    PLAYER.equipment.append(equipment.weapon(equipment.bow))
                    print('CONSOLE: Player now has %s equipment items.' % len(PLAYER.equipment))
                    buttons['wpchCrossbow'].active = False
                    buttons['wpchBow'].active = False
                    buttons['wpchKnife'].active = False
                    if len(PLAYER.equipment) == 2:
                        return 2
                    else:
                        return 4
                elif i.identity == 'crossbow':
                    PLAYER.equipment.append(equipment.weapon(equipment.crossbow))
                    print('CONSOLE: Player now has %s equipment items.' % len(PLAYER.equipment))
                    buttons['wpchCrossbow'].active = False
                    buttons['wpchBow'].active = False
                    buttons['wpchKnife'].active = False
                    if len(PLAYER.equipment) == 2:
                        return 2
                    else:
                        return 4
                elif i.identity == 'knives':
                    PLAYER.equipment.append(equipment.weapon(equipment.knives))
                    print('CONSOLE: Player now has %s equipment items.' % len(PLAYER.equipment))
                    buttons['wpchCrossbow'].active = False
                    buttons['wpchBow'].active = False
                    buttons['wpchKnife'].active = False
                    if len(PLAYER.equipment) == 2:
                        return 2
                    else:
                        return 4
                elif i.identity == 'spear':
                    PLAYER.equipment.append(equipment.weapon(equipment.spear))
                    print('CONSOLE: Player now has %s equipment items.' % len(PLAYER.equipment))
                    buttons['wpchSword'].active = False
                    buttons['wpchSpear'].active = False
                    buttons['wpchAxe'].active = False
                    if len(PLAYER.equipment) == 2:
                        return 2
                    else:
                        return 4
                elif i.identity == 'sword':
                    PLAYER.equipment.append(equipment.weapon(equipment.sword))
                    print('CONSOLE: Player now has %s equipment items.' % len(PLAYER.equipment))
                    buttons['wpchSword'].active = False
                    buttons['wpchSpear'].active = False
                    buttons['wpchAxe'].active = False
                    if len(PLAYER.equipment) == 2:
                        return 2
                    else:
                        return 4
                elif i.identity == 'axe':
                    PLAYER.equipment.append(equipment.weapon(equipment.axe))
                    print('CONSOLE: Player now has %s equipment items.' % len(PLAYER.equipment))
                    buttons['wpchSword'].active = False
                    buttons['wpchSpear'].active = False
                    buttons['wpchAxe'].active = False
                    if len(PLAYER.equipment) == 2:
                        return 2
                    else:
                        return 4
            else:
                i.pressed == False
    return gamestate

def initButtons():
    """
    Initializes the buttons for the main menu.

    Returns a list of all buttons in the main menu.
    """
    #buttons.append(button((RES[0], 210), 'load', pygame.image.load('loadgameButton.png')))
    buttons['menuTitle'] = button((RES[0] / 2 - 125, 20), None, pygame.image.load('title.png'), (200, 50))
    buttons['menuPlay'] = button((RES[0] / 2 - 100, 150), 'play', pygame.image.load('newgameButton.png'), (200, 50))
    buttons['menuQuit'] = button((RES[0] / 2 - 100, 270), 'quit', pygame.image.load('quitButton.png'), (200, 50))

    buttons['wpchBow'] = button((RES[0] / 2 - 200, 100), 'bow', pygame.image.load('bow.png'), (90, 90))
    buttons['wpchCrossbow'] = button((RES[0] / 2 - 200, 200), 'crossbow', pygame.image.load('crossbow.png'), (90, 90))
    buttons['wpchKnife'] = button((RES[0] / 2 - 200, 300), 'knives', pygame.image.load('knife.png'), (90, 90))
    buttons['wpchSword'] = button((RES[0] / 2 + 200, 100), 'sword', pygame.image.load('sword.png'), (90, 90))
    buttons['wpchAxe'] = button((RES[0] / 2 + 200, 200), 'axe', pygame.image.load('axe.png'), (90, 90))
    buttons['wpchSpear'] = button((RES[0] / 2 + 200, 300), 'spear', pygame.image.load('spear.png'), (90, 90))

##def initSounds():
##    """
##    Adds a list of sounds to be used in the game.
##    """
##    sounds = {}
##    for sound_name in SOUND_NAMES:
##        sounds[sound_name] = pygame.mixer.Sound(SOUND_FILES[sound_name])
##    return sounds

def setMusic(song, delay):
    """
    Stops the currently playing song, then sets a new song to be played.
    Takes in the name of the song to be played, a string.
    """
    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSIC[song])
    pygame.mixer.music.play(-1, delay)

def displayPlayer(display):
    display.blit(PLAYER.image, (PLAYER.coords[0] - PLAYER.size, PLAYER.coords[1] - PLAYER.size))
    if PLAYER.entity_target != None:
        #pygame.draw.ellipse(display, (255, 0, 0), ((int(PLAYER.entity_target.coords[0] - 20), int(PLAYER.entity_target.coords[1])), int((PLAYER.entity_target.coords[0] + 20), int(PLAYER.entity_target.coords[1])), int(PLAYER.entity_target.coords[0]), int(PLAYER.entity_target.coords[1] - 20)), (int(PLAYER.entity_target.coords[0]), int(PLAYER.entity_target.coords[1] + 20)))
        display.blit(pygame.image.load('target_reticule.png'), (PLAYER.entity_target.coords[0] - 43, PLAYER.entity_target.coords[1] - 43))
    
def displayArrows(room, display):
    if room.warps[1] != None:
        display.blit(IMAGES['uarrowImg'], (RES[0] / 2 - 45, 0))
    if room.warps[3] != None:
        display.blit(IMAGES['darrowImg'], (RES[0] / 2 - 45, RES[1] - 30))
    if room.warps[0] != None:
        display.blit(IMAGES['larrowImg'], (0, RES[1] / 2 - 45))
    if room.warps[2] != None:
        display.blit(IMAGES['rarrowImg'], (RES[0] - 30, RES[1] / 2 - 45))
        
def roomLoop(room, display):
    for i in room.enemies:
        if i.alive:
            display.blit(i.image, (i.coords[0] - i.size, i.coords[1] - i.size))
            i.AI(PLAYER)
            i.move()
            i.attack(TPS)
            i.checkDeath(PLAYER)
            if i.hp > 0:
                i.show_hp(display)
##    for i in room.sceneries:
##        display.blit(i.image, i.coords)

def show_tick(display):
        length = int((100 * PLAYER.tick)/200)
        bar2 = pygame.transform.smoothscale(pygame.image.load('ybar.png'), (length, 20))
        display.blit(pygame.image.load('bbar.png'), (220, RES[1] - 90))
        display.blit(bar2, (220, RES[1] - 90))

def show_hp(display):
        length = int((200 * PLAYER.hp)/PLAYER.hpmax)
        bar2 = pygame.transform.smoothscale(pygame.image.load('gbar.png'), (length, 40))
        display.blit(pygame.transform.smoothscale(pygame.image.load('rbar.png'), (200, 40)), (RES[0] - 260, 60))
        display.blit(bar2, (RES[0] - 260, 60))

def display_gui(display, gui, font):
    display.blit(gui[0], (0, RES[1] - 300))
    display.blit(PLAYER.equipment[0].image, (48, RES[1] - 142))
    display.blit(gui[1], (0, 0))
    display.blit(gui[2], (220, RES[1] - 150))
    display.blit(font[0].render(str(PLAYER.kills), True, (150, 100, 0)), (120, 8))
    display.blit(font[1].render(str(PLAYER.equipment[0].level), True, (130, 100, 0)), (280, RES[1] - 125))
    display.blit(font[1].render(str(PLAYER.equipment[0].exp), True, (130, 100, 0)), (280, RES[1] - 145))
    show_tick(display)
    if PLAYER.hp > 0:
        show_hp(display)

def initialize():
    """
    Initializes the pygame library, and creates a display window.

    Returns a list of buttons in the main menu, and the starting game state.
    """
    print('CONSOLE: Initializing loop...')
    global PLAYER, resolution, font, buttons
    buttons = {}
    PLAYER = objects.player([3, 20, 50], ['player.png', 'humandeath.ogg'], (500, 500))
    resolution = (RES)
    room = world.area(world.world['hunterland1'])
    room.buildSurface(resolution)
    gui = [pygame.image.load('GUI_1.png'), pygame.image.load('GUI_2.png'), pygame.image.load('GUI_3.png')]
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    font = [pygame.font.Font(None, 60), pygame.font.Font(None, 18)]
##    sounds = initSounds()
    display = pygame.display.set_mode(resolution)
    pygame.display.toggle_fullscreen()
    initButtons()
    buttons['menuQuit'].active = True
    buttons['menuPlay'].active = True
    buttons['menuTitle'].active = True
    gamestate = 1 #Gamestate 1 is the main menu
    setMusic('Music', 0)
    print('CONSOLE: Init complete. Starting loop.')
    return gamestate, display, room, gui

def runProgram(gamestate, display, room, gui):
    """
    Run the program main loop

    Takes in a list of buttons in the main menu, and the starting game state.
    """
    #setMusic('Intrepid', 0)
    while True:
        if gamestate == 1:
            display.fill((85, 35, 5))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i in buttons:    
                            buttons[i].buttonPressed()
                if event.type == QUIT:
                    terminate()
            gamestate = checkButtons(gamestate)
            for i in buttons:
                buttons[i].displayButtons(display)
                
        elif gamestate == 2:
##            display.fill((50, 150, 50))
            if PLAYER.test_death():
                gamestate = 3
            display.blit(room.scene, (0, 0))
            displayPlayer(display)
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 3:
                        PLAYER.target_location(room)
                        PLAYER.entity_target = PLAYER.target_entity(room)
                elif event.type == KEYDOWN:
                    if event.key == K_TAB:
                        PLAYER.switch_weapon()
            PLAYER.attack()
            PLAYER.move()
            PLAYER.collision(room)
            PLAYER.regenerate()
            roomLoop(room, display)
            room = checkWarp(room)
            display_gui(display, gui, font)
            displayArrows(room, display)

        elif gamestate == 0:
            print('CONSOLE: Quitting game.')
            terminate()

        elif gamestate == 3:
            display.fill((75, 35, 35))
            display.blit(pygame.image.load('gameover.png'), (RES[0] / 2 - 150, RES[1] / 2 - 150))
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()

        elif gamestate == 4:
            display.fill((85, 35, 5))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i in buttons:    
                            buttons[i].buttonPressed()
                if event.type == QUIT:
                    terminate()
            gamestate = checkButtons(gamestate)
            for i in buttons:
                buttons[i].displayButtons(display)

        CLOCK.tick(TPS)
        pygame.display.update()

def main():
    """
    Initialize data, then run the program.
    """
    gamestate, display, room, gui = initialize()
    runProgram(gamestate, display, room, gui)

if __name__ == '__main__':
    main()

