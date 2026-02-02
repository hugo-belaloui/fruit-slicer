import pygame
import random
import window
import string


ASSETS = ["apple", "mango", "kiwi", "bomb", "ice"]
FRUIT_NAME = ["apple", "mango", "kiwi"]
BOMB = ["bomb"]
FREEZE = ["ice"]
SCALE = 0.3
GRAVITY = 0.1
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
    def __init__(self, image, name):
        self.image = image
        self.name = name
        self.x = random.randint(0, window.WIDTH) 
        self.y = window.HEIGHT 
        if self.x < window.WIDTH // 2:
            self.vx = random.uniform(3, 6) #uniform for floating numbers
        else:
            self.vx = random.uniform(-6, -3)
        self.vy = random.uniform(-10, -5)
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
        self.freeze_end_time = 0 #variable that time of end freeze
        self.strikes = 0 # amount of strikes

    def check_input(self, user_input):
        
        for fruit in self.fruits:
            # we compare letter with user input
            if user_input.upper() == fruit.letter.upper():
                self.fruits.remove(fruit) # we remove the fruit, should be animated later on
                return fruit.name 
        return None
    
    def activate_freeze(self, duration):
        self.freeze_end_time = pygame.time.get_ticks() + duration

    #method to reset the amount of lives when it quits without quitting the program
    def reset(self):
        self.fruits = []
        self.strikes = 0
        self.current_wave_fruits = 0
        self.last_spawn = pygame.time.get_ticks()

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

        if current_time < self.freeze_end_time : #if frozen don't add fruits
            self.last_spawn = current_time 
            return
        
        if self.current_wave_fruits == 0:                             # number of fruit in the current wave
            if current_time - self.last_wave_time < WAVE_DELAY:       # waits until the delay of the wave becomes 0
                return

        if current_time - self.last_spawn > SPAWN_DELAY:              # look if the delay has passed
            fruit_name = self.probability()
            fruit_image = fruits_images[ASSETS.index(fruit_name)]
            fruit = Fruit(fruit_image, fruit_name)               # choose a random fruit 
            self.fruits.append(fruit)                                 # add the chosen fruit to the list
            self.last_spawn = current_time                            # update the the time of last spawn 
            self.current_wave_fruits += 1                             # add +1 to the number of fruits in the wave

            if self.current_wave_fruits >= self.fruits_per_wave:
                self.current_wave_fruits = 0
                self.last_wave_time = current_time                    #update the time of the last wave
                self.fruits_per_wave = random.randint(3, 5)           # add a fruit between 3 and 5

    def update_draw(self, screen):
        current_time = pygame.time.get_ticks()
        is_frozen = current_time < self.freeze_end_time #check if time is frozen
        for fruit in self.fruits[:]:
            if not is_frozen: # if time isn't frozen we move the assets
                fruit.update()
            fruit.draw(screen)
            if fruit.y > window.HEIGHT or fruit.x > window.WIDTH: #if fruit leaves the screen 
                self.fruits.remove(fruit) # remove the fruit from the list of fruits in the wave
                if fruit.name in FRUIT_NAME:
                    self.strikes += 1
