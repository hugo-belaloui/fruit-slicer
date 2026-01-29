import pygame

pygame.init()

#taille de la fenêtre
window_width, window_height = 1000, 600
screen = pygame.display.set_mode((window_width, window_height))

#Charger les images
bg_image = pygame.image.load("image/fondnumber1.jpg")

buttonplay_img = pygame.image.load("image/buttonfondplay.png").convert_alpha() 

buttonexit_img = pygame.image.load("image/buttonfondexit.png").convert_alpha() 

buttonparam_img = pygame.image.load("image/parametre.png").convert_alpha()

button_back_img = pygame.image.load("image/retour.png").convert_alpha()

#Images son
son_on_img = pygame.image.load("image/son.png").convert_alpha()
son_off_img = pygame.image.load("image/coupeson.png").convert_alpha()

#le fond pour les paramètres
bg_params = pygame.image.load("image/fondparameter.png") 
bg_params_scaled = pygame.transform.scale(bg_params, (window_width, window_height))


#Couleurs
white = (255, 255, 255)

#Musique de fond  (fond1)
pygame.mixer.music.load("Sketchbook 2024-10-26.ogg")
pygame.mixer.music.play(-1)

#Zone du bouton (Position et Taille)
button_rect = pygame.Rect(356, 300, 310, 180)
#redimensionne l'image PNG pour qu'elle fasse exactement la taille du bouton
button_img = pygame.transform.scale(buttonplay_img, (button_rect.width, button_rect.height))


#Zone du bouton (Position et Taille)
exit_rect = pygame.Rect(356, 393, 310, 180)
#redimensionne l'image PNG pour qu'elle fasse exactement la taille du bouton
exit_img = pygame.transform.scale(buttonexit_img, (exit_rect.width, exit_rect.height))


#BOUTON PARAMETRE (FOND 2)
parameter_rect = pygame.Rect(830, 20, 200, 100) #en haut à droite
parameter_img = pygame.transform.scale(buttonparam_img, (parameter_rect.width, parameter_rect.height))



#BOUTON RETOUR (PARAMETRES)
back_rect = pygame.Rect(20, 20, 200, 100) #en haut à gauche
back_img = pygame.transform.scale(button_back_img, (back_rect.width, back_rect.height))

#BOUTON SON (PARAMETRES)
mute_rect = pygame.Rect(420, 250, 180, 100) # Au milieu de l'écran paramètres son
son_on_scaled = pygame.transform.scale(son_on_img, (mute_rect.width, mute_rect.height))
son_off_scaled = pygame.transform.scale(son_off_img, (mute_rect.width, mute_rect.height))


#Police pour le texte
font = pygame.font.Font("LuckyRookie Regular 400.ttf", 60) 

play_pressed = False#indique si on a cliqué sur play ou pas

params_open = False#servira à savoir si on affiche les paramètres ou pas

is_muted = False # NOUVEAU : pour savoir si le son est coupé


#Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si on est sur le premier menu
            if not play_pressed:
                if button_rect.collidepoint(event.pos):
                    play_pressed = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Sketchbook 2025-12-11_VERSE.ogg")
                    pygame.mixer.music.play(-1)

                if exit_rect.collidepoint(event.pos):
                    running = False



            #    CLICS MENU PARAMÈTRES (FOND 3) 

            elif params_open:#Si on est dans les paramètres
                if back_rect.collidepoint(event.pos):
                    params_open = False # On ferme les paramètres pour revenir au Fond 2

                # NOUVEAU : Clic sur le bouton MUTE
                if mute_rect.collidepoint(event.pos):
                    is_muted = not is_muted # On inverse l'état (ON devient OFF et vice-versa)
                    
                    if is_muted:
                        pygame.mixer.music.set_volume(0) # Coupe le volume
                    else:
                        pygame.mixer.music.set_volume(1) # Remet le volume à fond

                if exit_rect.collidepoint(event.pos):
                    running = False


            #  CLICS JEU (FOND 2)  
            
            else:
                if parameter_rect.collidepoint(event.pos):
                    params_open = True


    if not play_pressed:#Affichage du menu principal tant que play n'est pas cliqué
        #Affichage du fond
        bg_scaled = pygame.transform.scale(bg_image, (window_width, window_height))
        screen.blit(bg_scaled, (0, 0))
        
        #image png du bouton texte play
        screen.blit(button_img, (button_rect.x, button_rect.y))
        text = font.render("PLAY", True, white) # couleur du texte
        text_rect = text.get_rect(center=button_rect.center) # centrer le texte
        screen.blit(text, text_rect) # afficher le texte sur le bouton

        #image png du bouton texte play
        screen.blit(exit_img, (exit_rect.x, exit_rect.y))
        text_exit = font.render("EXIT", True, white)
        screen.blit(text_exit, text_exit.get_rect(center=exit_rect.center))
        


    elif params_open:
        #Affichage du fond de paramètres
        screen.blit(bg_params_scaled, (0, 0))
        #affiche le boutton retour
        screen.blit(back_img, (back_rect.x, back_rect.y))

        if is_muted:# affiche l'icône son coupé ou non
            screen.blit(son_off_scaled, (mute_rect.x, mute_rect.y))
        else:
            screen.blit(son_on_scaled, (mute_rect.x, mute_rect.y))

        screen.blit(exit_img, (exit_rect.x, exit_rect.y))
        text_exit = font.render("EXIT", True, white)
        screen.blit(text_exit, text_exit.get_rect(center=exit_rect.center))

    else:
        #Fond 2 uniquement après le clic play
        bg_game = pygame.image.load("image/fond2.jpg")
        bg_game_scaled = pygame.transform.scale(bg_game, (window_width, window_height))
        screen.blit(bg_game_scaled, (0, 0))

        #affiche le boutton paramètre
        screen.blit(parameter_img, (parameter_rect.x, parameter_rect.y))
        
        



    pygame.display.update()
pygame.quit()