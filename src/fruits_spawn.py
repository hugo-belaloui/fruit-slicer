import pygame
import random
import string

FRUITS_NAMES = ["apple", "mango", "kiwi", "bomb", "ice"]
SCALE = 0.3
GRAVITY = 0.5
SPAWN_DELAY = 1000 #ms

def load_fruits():
    fruits = []

    for name in FRUITS_NAMES:
        img = pygame.image.load(f"assets/{name}.png")
        w, h = img.get_width(), img.get_height()
        img = pygame.transform.scale(img, (int(w * SCALE), int(h * SCALE)))
        fruits.append(img)

    return fruits

fruits_images = load_fruits()

class Fruit:
    def __init__(self, image):
        self.image = image
        self.x = random.randint(0, 800) 
        self.y = 400
        if self.x < 800 // 2:
            self.vx = random.uniform(3, 6) #uniform for floating numbers
        else:
            self.vx = random.uniform(-6, -3)
        self.vy = random.uniform(-22, -18)
        self.letter = random.choice(string.ascii_uppercase) # choose an uppercase letter randomly
        self.letter_font = pygame.font.Font(None, 50) # font for the letters
        self.letter_text = self.letter_font.render(self.letter, True, (255,255,255) )
    def update(self) :
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.letter_text, (self.x - 10, self.y - 10))

fruits = []
# print(last_spawn)
def spawn(last_spawn):
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn > SPAWN_DELAY:
        fruit = Fruit(random.choice(fruits_images))
        fruits.append(fruit)
        last_spawn = current_time
        return current_time
    return last_spawn

def update_draw(screen):
    for fruit in fruits[:]:
        fruit.update()
        fruit.draw(screen)


# spawn_x = random.randint(0 , 800)
# spawn_y = 400

# fruit = random.choice(fruits)

# def draw_fruit(screen):
#         screen.blit(fruit, (spawn_x, spawn_y))
