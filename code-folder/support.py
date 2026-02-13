from settings import *
from os.path import join
from os import walk
from pytmx.util_pygame import load_pygame

def import_image(*path, alpha = True, format = ".png"):
    full_path = join(*path) + format
    surf = pygame.image.load(full_path).convert() if alpha else pygame.image.load(full_path).convert_alpha()
    return surf


def import_folder():
    pass