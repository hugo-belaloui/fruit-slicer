import pygame
import random
import window
import string


ASSETS = ["apple", "mango", "kiwi", "bomb", "ice"]
FRUIT_NAME = ["apple", "mango", "kiwi"]
BOMB = ["bomb"]
FREEZE = ["ice"]
SCALE = 0.3
GRAVITY = 0.4
SPAWN_DELAY = random.randint(300, 800)  #ms
WAVE_DELAY = 2000 #ms
PERCENTAGE = random.randint(0, 100)


def load_fruits():
    fruits = []

    for name in ASSETS:
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

    def probability(self):
        probability = random.randint(0, 100)
        if probability in range(0, 88):
            return random.choice(FRUIT_NAME)
        elif probability in range(88, 96):
            return random.choice(BOMB)
        else:
            return random.choice(FREEZE)

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.current_wave_fruits == 0:                             # number of fruit in the current wave
            if current_time - self.last_wave_time < WAVE_DELAY:       # waits until the delay of the wave becomes 0
                return

        if current_time - self.last_spawn > SPAWN_DELAY:              # look if the delay has passed
            fruit_name = self.probability()
            fruit_image = fruits_images[ASSETS.index(fruit_name)]
            fruit = Fruit(fruit_image)               # choose a random fruit 
            self.fruits.append(fruit)                                 # add the chosen fruit to the list
            self.last_spawn = current_time                            # update the the time of last spawn 
            self.current_wave_fruits += 1                             # add +1 to the number of fruits in the wave

            if self.current_wave_fruits >= self.fruits_per_wave:
                self.current_wave_fruits = 0
                self.last_wave_time = current_time                    #update the time of the last wave
                self.fruits_per_wave = random.randint(3, 5)           # add a fruit between 3 and 5

    def update_draw(self, screen):
        for fruit in self.fruits[:]:
            fruit.update()
            fruit.draw(screen)
