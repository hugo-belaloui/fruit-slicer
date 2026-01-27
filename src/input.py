import pygame

def keyboard_inputs():
    """
    Checks for keyboard events
    """
    key_pressed = []
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed.append(pygame.key.name(event.key))
    return key_pressed