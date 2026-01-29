import pygame
WIDTH = 400
HEIGHT = 800
def init_screen(): 
    """
    Initialize screen and clock
    """
    pygame.init()
    #screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # var for screen size, set as fullscreen
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    
    pygame.display.set_caption ("Fruit Slicer") 
    clock = pygame.time.Clock() # init a clock object
    return screen, clock

