import random
import pygame
from pygame.locals import *
import sys
try:
    import objects
    import world
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
    def __init__(self, location, identity, image):
        self.location = location
        self.identity = identity
        self.image = image
        self.pressed = False
        
    def buttonPressed(self):
        """
        Checks whether or not a button has been clicked.

        Returns a slightly modified list of buttons, modifying whether or not the button has been pressed.
        """
        mouse = pygame.mouse.get_pos()
        print('CONSOLE: Clicked at point '+str(mouse))
        if mouse[0] - self.location[0] <= 200 and mouse[0] - self.location[0] >= 0:
            if mouse[1] - self.location[1] <= 50 and mouse[1] - self.location[1] >= 0:
                self.pressed = True
                print('CONSOLE: Button of ID %s has been pressed.' % self.identity)
    def displayButtons(self, display):
        """
        Displays the button on the screen as self.image. All button images should be 200px X 50px
        to have proper dimensions.

        Takes in the main game display screen.
        """
        display.blit(self.image, self.location)

def checkButtons(buttons):
    """
    Checks whether the ID of all buttons being pressed checks out with any pre-determined functions
    of specific buttons. If the function goes through and nothing happens, the button becomes un-pressed.

    Takes in the list of all buttons.

    Ex: A 'quit' button will terminate the game when pressed (game state 0).

    Returns the new game state.
    """
    for i in buttons:
        if i.pressed == True:
            if i.identity == 'quit':
                print('CONSOLE: Quit Button pressed.')
                return 0
                print('ERROR: Quit not gone through.')
            if i.identity == 'play':
                print('CONSOLE: Play button pressed.')
                #setMusic('Janon', 0)
                return 2
        else:
            i.pressed == False
    return 1

def initButtons():
    """
    Initializes the buttons for the main menu.

    Returns a list of all buttons in the main menu.
    """
    buttons = []
    #buttons.append(button((RES[0], 210), 'load', pygame.image.load('loadgameButton.png')))
    buttons.append(button((RES[0] / 2 - 125, 20), None, pygame.image.load('title.png')))
    buttons.append(button((RES[0] / 2 - 100, 150), 'play', pygame.image.load('newgameButton.png')))
    buttons.append(button((RES[0] / 2 - 100, 270), 'quit', pygame.image.load('quitButton.png')))
    return buttons

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
    if PLAYER.hp > 0:
        PLAYER.show_hp(display)
    if PLAYER.entity_target != None:
        #pygame.draw.ellipse(display, (255, 0, 0), ((int(PLAYER.entity_target.coords[0] - 20), int(PLAYER.entity_target.coords[1])), int((PLAYER.entity_target.coords[0] + 20), int(PLAYER.entity_target.coords[1])), int(PLAYER.entity_target.coords[0]), int(PLAYER.entity_target.coords[1] - 20)), (int(PLAYER.entity_target.coords[0]), int(PLAYER.entity_target.coords[1] + 20)))
        display.blit(pygame.image.load('target_reticule.png'), (PLAYER.entity_target.coords[0] - 23, PLAYER.entity_target.coords[1] - 23))
    
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
            if i.entity_target != None:
                i.attack(TPS)
            i.checkDeath(PLAYER)
            if i.hp > 0:
                i.show_hp(display)
##    for i in room.sceneries:
##        display.blit(i.image, i.coords)

def show_tick(display):
        length = int((100 * PLAYER.tick)/200)
        bar2 = pygame.transform.smoothscale(pygame.image.load('ybar.png'), (length, 20))
        display.blit(pygame.image.load('bbar.png'), (100, RES[1] - 60))
        display.blit(bar2, (100, RES[1] - 60))

def display_gui(display, gui, font):
    display.blit(gui[0], (0, RES[1] - 200))
    display.blit(PLAYER.equipment[0].image, (23, RES[1] - 70))
    display.blit(gui[1], (0, 0))
    display.blit(font.render(str(PLAYER.kills), True, (150, 100, 0)), (150, 8))
    show_tick(display)

def initialize():
    """
    Initializes the pygame library, and creates a display window.

    Returns a list of buttons in the main menu, and the starting game state.
    """
    print('CONSOLE: Initializing loop...')
    global PLAYER, resolution, font
    PLAYER = objects.player([3, 20, 50], ['player.png', 'humandeath.ogg'], (700, 700))
    resolution = (RES)
    room = world.area(world.world['hunterland1'])
    room.buildSurface(resolution)
    gui = [pygame.image.load('GUI_1.png'), pygame.image.load('GUI_2.png')]
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    font = pygame.font.Font(None, 60)
##    sounds = initSounds()
    display = pygame.display.set_mode(resolution)
    pygame.display.toggle_fullscreen()
    buttons = initButtons()
    gamestate = 1 #Gamestate 1 is the main menu.
    setMusic('Music', 0)
    print('CONSOLE: Init complete. Starting loop.')
    return buttons, gamestate, display, room, gui

def runProgram(buttons, gamestate, display, room, gui):
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
                            i.buttonPressed()
                if event.type == QUIT:
                    terminate()
            gamestate = checkButtons(buttons)
            for i in buttons:
                i.displayButtons(display)
                
        elif gamestate == 2:
##            display.fill((50, 150, 50))
            if PLAYER.test_death():
                gamestate = 3
            display.blit(room.scene, (0, 0))
            displayPlayer(display)
            display_gui(display, gui, font)
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

        CLOCK.tick(TPS)
        pygame.display.update()

def main():
    """
    Initialize data, then run the program.
    """
    buttons, gamestate, display, room, gui = initialize()
    runProgram(buttons, gamestate, display, room, gui)

if __name__ == '__main__':
    main()

