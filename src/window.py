import pygame
# WIDTH = 1000
# HEIGHT = 600
pygame.display.init()
info_screen = pygame.display.Info()

# Option A : Pour jouer en PLEIN ÉCRAN (Fullscreen)
# On utilise la largeur et hauteur maximales de l'écran
WIDTH = info_screen.current_w
HEIGHT = info_screen.current_h
def init_screen(): 
    """
    Initialize screen and clock
    """
    pygame.init()
    #screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # var for screen size, set as fullscreen
    screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
    
    pygame.display.set_caption ("Fruit Slicer") 
    clock = pygame.time.Clock() # init a clock object
    return screen, clock

