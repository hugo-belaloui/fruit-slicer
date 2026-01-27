import pygame
import random
import time


FRUITS_NAMES = ["apple", "mango", "kiwi", "bomb", "ice"]
SCALE = 0.5

def load_fruits():
    fruits = []

    for name in FRUITS_NAMES:
        img = pygame.image.load(f"fruit-slicer/assets/{name}.png")
        w, h = img.get_width(), img.get_height()
        img = pygame.transform.scale(img, (int(w * SCALE), int(h * SCALE)))
        fruits.append(img)

    return fruits


fruits = load_fruits()

fruit = random.choice(fruits)

def draw_fruit(screen):
        screen.blit(fruit, (00, 150))