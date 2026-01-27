import pygame
import window



apple = pygame.image.load("fruit-slicer/assets/apple.png")
w = apple.get_width()
h = apple .get_height()
apple = pygame.transform.scale(apple ,(w * 0.5, h *0.5))

def draw_fruit(screen):
    screen.blit(apple,(50,40))

