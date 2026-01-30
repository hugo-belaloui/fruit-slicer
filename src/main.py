import pygame
import window
import game_states
import menu
import inputs
import fruits_spawn

screen, clock = window.init_screen() #call function from diffrent module to initialize screen
game_on = True 

current_state = game_states.STATE_MENU
spawner = fruits_spawn.FruitSpawner()


while game_on: # while game_on is true as set previously the game is running

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # handle window closing
            game_on = False

        if event.type == pygame.KEYDOWN: # input handling
            print(pygame.key.name(event.key)) # for debugging purpose
            if current_state == game_states.STATE_MENU: # check current state
                if event.key == pygame.K_q:
                    current_state = game_states.STATE_GAME
            elif current_state == game_states.STATE_GAME:
                if event.key == pygame.K_ESCAPE:
                    current_state = game_states.STATE_MENU
                else:
                    spawner.check_input(pygame.key.name(event.key))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if menu.play_button.rect.collidepoint(inputs.mouse_position()):
                    print(inputs.mouse_position())
                    current_state = game_states.STATE_GAME
                if menu.quit_button.rect.collidepoint(inputs.mouse_position()):
                    game_on = False
                    
    if current_state == game_states.STATE_MENU:
        menu.draw(screen)
    elif current_state == game_states.STATE_GAME:
        screen.fill((30, 144, 255)) # fill the screen with a color as RGB
        spawner.update()
        spawner.update_draw(screen)
        print([fruit.letter for fruit in spawner.fruits])



    pygame.display.flip() # update the screen
    clock.tick(60) # avoid overloading the CPU by capping the game at 60 FPS

pygame.quit()