import pygame
pygame.display.init() # init only the required module from pygame for mouse handling
def mouse_position():
    mouse_position = pygame.mouse.get_pos()
    return mouse_position   

def keyboard_inputs():
    """
    Checks for keyboard events
    """
    key_pressed = []
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed.append(pygame.key.name(event.key))
    return key_pressed