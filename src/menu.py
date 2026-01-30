import pygame
import inputs
import window

pygame.font.init() # init only the required module from pygame for mouse handling

class Button:
    def __init__(self, x, y, width, height, text="Hello World"):
        self.rect = pygame.Rect(x, y, width, height) # create rectangle maybe add radius later
        
        #dict containing our colors depeding on the state
        self.fill_colors = {
            'normal': '#ffffff', 
            'hover': '#666666', 
            'pressed': '#333333'
        }
        self.current_color = self.fill_colors["normal"] # init the button state color
        self.text_color = (23, 33, 32)
        
        # police and text 
        self.font = pygame.font.Font(None, 40) 
        self.text_surface = self.font.render(text, True, self.text_color)
        
        # center our text in the rectangle
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw_button(self, screen):
        # draw our rectangle
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=12)
        if self.rect.collidepoint(inputs.mouse_position()):
            self.current_color = self.fill_colors['hover']
            if pygame.mouse.get_just_pressed()[0]: # mouse get pressed [0] is for left click
                self.current_color = self.fill_colors['pressed']
        else :
            self.current_color = self.fill_colors['normal']
        # draw our text 
        screen.blit(self.text_surface, self.text_rect)

# constants for alignment 
SCREEN_WIDTH = window.WIDTH
SCREEN_HEIGHT = window.HEIGHT
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 80
GAP = 20

center_x = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
start_y = (SCREEN_HEIGHT - (BUTTON_HEIGHT * 2 + GAP)) // 2

play_button = Button(center_x, start_y, BUTTON_WIDTH, BUTTON_HEIGHT, "Jouer")
quit_button = Button(center_x, start_y + BUTTON_HEIGHT + GAP, BUTTON_WIDTH, BUTTON_HEIGHT, "Quitter")



def draw(screen):
    screen.fill((222, 222, 222))
    play_button.draw_button(screen)
    quit_button.draw_button(screen)




