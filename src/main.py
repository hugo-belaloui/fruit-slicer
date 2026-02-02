import pygame
import window
import game_states
import menu
import inputs
import fruits_spawn
import score
import random

screen, clock = window.init_screen() #call function from diffrent module to initialize screen
game_on = True 

current_state = game_states.STATE_MENU
spawner = fruits_spawn.FruitSpawner()
lives = 3
lives_font = pygame.font.Font(None, 40)
score_font = pygame.font.Font(None, 40)
menu_image = pygame.image.load("assets/main_theme.png") #load images 
background_image = pygame.image.load("assets/background_theme.png")
menu_image = pygame.transform.scale(menu_image, (window.WIDTH, window.HEIGHT)) #resize images
background_image = pygame.transform.scale(background_image, (window.WIDTH, window.HEIGHT))
# load songs
gameplay_sound = pygame.mixer.Sound("assets/gameplay_audio.ogg")
menu_sound = pygame.mixer.Sound("assets/menu_audio.ogg")



while game_on: # while game_on is true as set previously the game is running

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # handle window closing
            game_on = False

        if event.type == pygame.KEYDOWN: # input handling
            print(pygame.key.name(event.key)) # for debugging purpose
            if current_state == game_states.STATE_MENU: # check current state
                if event.key == pygame.K_q:
                    current_state = game_states.STATE_GAME
                    spawner.reset()
            elif current_state == game_states.STATE_GAME:
                if event.key == pygame.K_ESCAPE:
                    current_state = game_states.STATE_MENU
                else:
                    hit_fruit = spawner.check_input(pygame.key.name(event.key))
                    if hit_fruit:
                        if "bomb" in hit_fruit:
                            current_state = game_states.STATE_MENU # if we hit the bomb we go back to the menu for now 
                            spawner.reset() #reset the lists of fruits
                        else: 
                            if "ice" in hit_fruit:
                                spawner.activate_freeze(random.randint(3000,5000)) #we add random duration time to the freeze
                            real_fruits_hit = [f for f in hit_fruit if f in fruits_spawn.FRUIT_NAME] #make a list of only the fruits excluding the ice and bombs
                            count = len(real_fruits_hit)
                            if count > 0: # if we hit a fruit score increases 
                                points = count #one point per fruit
                                if count >= 3: #rules for bonus ex three fruits plus two points
                                    bonus = count - 1
                                    points += bonus
                                scoring = score.load_scores()
                                scoring["scores"]["players"]["jhon doe"] += points 
                                score.add_scores(scoring)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if menu.play_button.rect.collidepoint(inputs.mouse_position()):
                    print(inputs.mouse_position())
                    current_state = game_states.STATE_GAME
                    spawner.reset()
                if menu.quit_button.rect.collidepoint(inputs.mouse_position()):
                    game_on = False
                    
    if current_state == game_states.STATE_MENU:
        gameplay_sound.stop()
        if menu_sound.get_num_channels() == 0: #check if the sound is already playing 
            menu_sound.play(-1) #play the audio as an infinite loop
        screen.blit(menu_image, (0, 0))
        menu.draw(screen)
    
    elif current_state == game_states.STATE_GAME:
        #screen.fill((30, 144, 255)) # fill the screen with a color as RGB
        menu_sound.stop()
        if gameplay_sound.get_num_channels() == 0:
            gameplay_sound.play(-1) #play the audio as an infinite loop
        screen.blit(background_image, (0,0))
        spawner.update()
        spawner.update_draw(screen)
        lives = 3 - spawner.strikes # substract the amount of lives by the amount of strikes
        lives_text = lives_font.render(f"Lives: {lives}", True, (255, 255, 255))
        current_score = score.load_scores()["scores"]["players"]["jhon doe"] # access the json to dispaly the score
        score_text = score_font.render(f"Score: {current_score}", True, (255, 255, 255))
        screen.blit(lives_text, (10, 10))
        screen.blit(score_text, (10, 50))
        if lives <= 0: # if no more lives quit to menu
            current_state = game_states.STATE_MENU
        # print([fruit.letter for fruit in spawner.fruits])



    pygame.display.flip() # update the screen
    clock.tick(120) # avoid overloading the CPU by capping the game at 60 FPS

pygame.quit()