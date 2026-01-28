import pygame

# list of instances
STATE_MENU = "menu"
STATE_GAME = "game"
STATE_QUIT = "end_game"


# import pygame
# import sys

# # Initialisation de Pygame
# pygame.init()



# # --- Boucle Principale d'Exécution ---

# # Configuration de l'écran
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Test de Bouton")
# clock = pygame.time.Clock()

# # Création d'une instance de bouton
# my_button = Button(300, 250, 200, 80, "Cliquez ici")

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Remplir le fond
#     screen.fill((30, 30, 30))

#     # Mise à jour et dessin du bouton
#     my_button.process() # Vérifie le survol (hover)
#     my_button.draw(screen) # Dessine à l'écran

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
# sys.exit()