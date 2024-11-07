import pygame

# Configuración de pantalla
SCREEN = pygame.display.set_mode((1280, 720))

# Cargar recursos
BG = pygame.transform.scale(pygame.image.load("assets/dbz2.png"),(1280,720))

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)
