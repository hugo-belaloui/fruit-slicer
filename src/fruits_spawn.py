import pygame
import random
import window
import string


FRUITS_NAMES = ["apple", "apple", "apple",
    "mango", "mango", "mango",
    "kiwi", "kiwi",
    "bomb",
    "ice"]
SCALE = 0.3
GRAVITY = 0.4
SPAWN_DELAY = random.randint(300 , 800)  #ms
WAVE_DELAY = 2000 #ms

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
        self.x = random.randint(0, window.WIDTH) 
        self.y = window.HEIGHT 
        if self.x < window.WIDTH // 2:
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

class FruitSpawner:
    def __init__(self):
        self.fruits = []
        self.last_spawn = 0
        self.last_wave_time = 0
        self.current_wave_fruits = 0
        self.fruits_per_wave = random.randint(3, 5)

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.current_wave_fruits == 0:
            if current_time - self.last_wave_time < WAVE_DELAY:
                return

        if current_time - self.last_spawn > SPAWN_DELAY:
            fruit = Fruit(random.choice(fruits_images))
            self.fruits.append(fruit)
            self.last_spawn = current_time
            self.current_wave_fruits += 1

            if self.current_wave_fruits >= self.fruits_per_wave:
                self.current_wave_fruits = 0
                self.last_wave_time = current_time
                self.fruits_per_wave = random.randint(3, 5)

    def update_draw(self, screen):
        for fruit in self.fruits[:]:
            fruit.update()
            fruit.draw(screen)

