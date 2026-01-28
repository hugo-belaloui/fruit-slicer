


import pygame

pygame.init()

# Taille de la fenêtre
window_width, window_height = 1000, 600
screen = pygame.display.set_mode((window_width, window_height))

# Charger les images
bg_image = pygame.image.load("image/fondnumber1.jpg")

button1_img = pygame.image.load("image/buttonfondplay.png").convert_alpha() 

button2_img = pygame.image.load("image/buttonfondexit.png").convert_alpha() 


# Couleurs
white = (255, 255, 255)


# Zone du bouton (Position et Taille)
button_rect = pygame.Rect(356, 300, 310, 180)
#redimensionne l'image PNG pour qu'elle fasse exactement la taille du bouton
button_img = pygame.transform.scale(button1_img, (button_rect.width, button_rect.height))



# Zone du bouton (Position et Taille)
exit_rect = pygame.Rect(356, 393, 310, 180)
#redimensionne l'image PNG pour qu'elle fasse exactement la taille du bouton
exit_img = pygame.transform.scale(button2_img, (exit_rect.width, exit_rect.height))



# Police pour le texte
font = pygame.font.Font("LuckyRookie Regular 400.ttf", 60) 

play_pressed = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("play !")  
                play_pressed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rect.collidepoint(event.pos):
                print("exit !")  
                running = False#ferme la fenêtre quand on clique sur exit

    if not play_pressed:
        # Affichage du fond
        bg_scaled = pygame.transform.scale(bg_image, (window_width, window_height))
        screen.blit(bg_scaled, (0, 0))
        
#image png du bouton texte play
        screen.blit(button_img, (button_rect.x, button_rect.y))
        text = font.render("PLAY", True, white) # couleur du texte
        text_rect = text.get_rect(center=button_rect.center) # centrer le texte
        screen.blit(text, text_rect) # afficher le texte sur le bouton

#image png du bouton texte play
        screen.blit(exit_img, (exit_rect.x, exit_rect.y))
        text = font.render("EXIT", False, white) 
        text_rect = text.get_rect(center=exit_rect.center) 
        screen.blit(text, text_rect) 
        
    else:
        # Fond 2 uniquement après le clic play
        bg_game = pygame.image.load("image/fond2.jpg")
        bg_game_scaled = pygame.transform.scale(bg_game, (window_width, window_height))
        screen.blit(bg_game_scaled, (0, 0))

    pygame.display.update()

pygame.quit()