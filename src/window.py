import pygame
WIDTH = 1000
HEIGHT = 600
def init_screen(): 
    """
    Initialize screen and clock
    """
    pygame.init()
    #screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # var for screen size, set as fullscreen
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    
    pygame.display.set_caption ("Fruit Slicer") 
    clock = pygame.time.Clock() # init a clock object
    return screen, clock

