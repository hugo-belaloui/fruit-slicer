import pygame
import sys

pygame.init()

#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # var for screen size, set as fullscreen
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption ("Fruit Slicer") 
clock = pygame.time.Clock()

game_on = True 

while game_on: # while game_on is true as set previously the game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # handle window closing
            game_on = False

    screen.fill((30, 144, 255)) # fill the screen with a color as RGB
    pygame.display.flip() # update the screen
    clock.tick(60)

pygame.quit()
sys.exit()