import pygame
import window

screen, clock = window.init_screen() #call function from diffrent module to initialize screen
game_on = True 

while game_on: # while game_on is true as set previously the game is running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # handle window closing
            game_on = False

    screen.fill((30, 144, 255)) # fill the screen with a color as RGB
    pygame.display.flip() # update the screen
    clock.tick(60) # avoid overloading the CPU by capping the game at 60 FPS

pygame.quit()