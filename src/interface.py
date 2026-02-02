import pygame

pygame.init()

#window size
window_width, window_height = 1000, 600
screen = pygame.display.set_mode((window_width, window_height))

#Load the images
bg_image = pygame.image.load("image/fondnumber1.jpg")

buttonplay_img = pygame.image.load("image/buttonfondplay.png").convert_alpha() 

buttonexit_img = pygame.image.load("image/buttonfondexit.png").convert_alpha() 

buttonparam_img = pygame.image.load("image/parametre.png").convert_alpha()

button_back_img = pygame.image.load("image/retour.png").convert_alpha()

#Images music
son_on_img = pygame.image.load("image/son.png").convert_alpha()
son_off_img = pygame.image.load("image/coupeson.png").convert_alpha()

#background for the settings
bg_params = pygame.image.load("image/fondparameter.png") 
bg_params_scaled = pygame.transform.scale(bg_params, (window_width, window_height))


#Colors
white = (255, 255, 255)

#Background music (background1)
pygame.mixer.music.load("song./Sketchbook 2024-10-26.ogg")
pygame.mixer.music.play(-1)

#Button Area (Position and Size)
button_rect = pygame.Rect(356, 300, 310, 180)
#resize the PNG image so that it is exactly the size of the button
button_img = pygame.transform.scale(buttonplay_img, (button_rect.width, button_rect.height))


#Button Area (Position and Size)
exit_rect = pygame.Rect(356, 393, 310, 180)
#resize the PNG image so that it is exactly the size of the button
exit_img = pygame.transform.scale(buttonexit_img, (exit_rect.width, exit_rect.height))


#BUTON PARAMETER(background 2)
parameter_rect = pygame.Rect(830, 20, 200, 100) #at the top right
parameter_img = pygame.transform.scale(buttonparam_img, (parameter_rect.width, parameter_rect.height))



#BACK BUTTON (SETTINGS)
back_rect = pygame.Rect(20, 20, 200, 100) #en haut à gauche
back_img = pygame.transform.scale(button_back_img, (back_rect.width, back_rect.height))

#BUTON music (SETTINGS)
mute_rect = pygame.Rect(420, 250, 180, 100) # Au milieu de l'écran paramètres son
son_on_scaled = pygame.transform.scale(son_on_img, (mute_rect.width, mute_rect.height))
son_off_scaled = pygame.transform.scale(son_off_img, (mute_rect.width, mute_rect.height))


#Font for the text
font = pygame.font.Font("LuckyRookie Regular 400.ttf", 60) 

play_pressed = False#indicates whether play was clicked or not

params_open = False#will be used to determine whether to display the settings or not

is_muted = False #NEW: to know if the sound is muted


#Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #If we are on the first menu
            if not play_pressed:
                if button_rect.collidepoint(event.pos):
                    play_pressed = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("song./Sketchbook 2025-12-11_VERSE.ogg")
                    pygame.mixer.music.play(-1)

                if exit_rect.collidepoint(event.pos):
                    running = False



            #    CLICKS MENU SETTINGS (BACKGROUND 3)

            elif params_open:#If we are in the settings
                if back_rect.collidepoint(event.pos):
                    params_open = False # We close the settings to return to Background 2

                # NEW: Click the MUTE button
                if mute_rect.collidepoint(event.pos):
                    is_muted = not is_muted #We reverse the state (ON becomes OFF and vice-versa)
                    
                    if is_muted:
                        pygame.mixer.music.set_volume(0) # Turn down the volume
                    else:
                        pygame.mixer.music.set_volume(1) # Turn the volume up all the way

                if exit_rect.collidepoint(event.pos):
                    running = False


            #CLICK GAME (BACKGROUND 2)
            
            else:
                if parameter_rect.collidepoint(event.pos):
                    params_open = True


    if not play_pressed:#Display the main menu until play is clicked
#Display the background
        bg_scaled = pygame.transform.scale(bg_image, (window_width, window_height))
        screen.blit(bg_scaled, (0, 0))
        
        #PNG image of the text play button
        screen.blit(button_img, (button_rect.x, button_rect.y))
        text = font.render("PLAY", True, white) # color of the text
        text_rect = text.get_rect(center=button_rect.center) # centrer le texte
        screen.blit(text, text_rect) # afficher le texte sur le bouton

        #PNG image of the text play button
        screen.blit(exit_img, (exit_rect.x, exit_rect.y))
        text_exit = font.render("EXIT", True, white)
        screen.blit(text_exit, text_exit.get_rect(center=exit_rect.center))
        


    elif params_open:
        #Display of settings background
        screen.blit(bg_params_scaled, (0, 0))
        #display back button
        screen.blit(back_img, (back_rect.x, back_rect.y))

        if is_muted:#display the correct image based on the sound state
            screen.blit(son_off_scaled, (mute_rect.x, mute_rect.y))
        else:
            screen.blit(son_on_scaled, (mute_rect.x, mute_rect.y))

        screen.blit(exit_img, (exit_rect.x, exit_rect.y))
        text_exit = font.render("EXIT", True, white)
        screen.blit(text_exit, text_exit.get_rect(center=exit_rect.center))

    else:
        #ackground for the game
        bg_game = pygame.image.load("image/fond2.jpg")
        bg_game_scaled = pygame.transform.scale(bg_game, (window_width, window_height))
        screen.blit(bg_game_scaled, (0, 0))

        #display parameter button
        screen.blit(parameter_img, (parameter_rect.x, parameter_rect.y))
        
        



    pygame.display.update()
pygame.quit()