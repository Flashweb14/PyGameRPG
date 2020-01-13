import os
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))


def load_image(filename):
    image = pygame.image.load(filename).convert_alpha()
    return image


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
