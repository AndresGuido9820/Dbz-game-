import pygame, sys
from config import SCREEN, get_font
from button import Button
from game_interface import game_interface

# Cargar imágenes de personajes
character_images = [
    pygame.image.load("assets/iddle.png"),
    pygame.image.load("assets/iddle2.png"),
   
    pygame.image.load("assets/nappaStance.png"),
    pygame.transform.scale(pygame.image.load("assets/vegetaStanding.png"), (5,5)),
    pygame.image.load("assets/raditzStanding.png"),
    pygame.image.load("assets/goku.png"),
    
 
]

# Cargar imágenes de mapas
map_images = [
    pygame.transform.scale(pygame.image.load("assets/map1.jpg"), (200,100)),
    pygame.transform.scale(pygame.image.load("assets/map2.jpg"),(200,100)),
    pygame.transform.scale(pygame.image.load("assets/map3.jpg"),(200,100)),
    pygame.transform.scale(pygame.image.load("assets/map4.jpg"),(200,100)),
]

def play():
    character_index = 0  # Índice del personaje seleccionado
    map_index = 0  # Índice del mapa seleccionado
    marge_horizontal= 30 
    whithd_image= 200


    while True:
        SCREEN.fill("black")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        

        # Texto para seleccionar personaje
        SELECTION_TEXT = get_font(45).render("SELECT YOUR CHARACTER", True, "White")
        SELECTION_RECT = SELECTION_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(SELECTION_TEXT, SELECTION_RECT)

        # Mostrar el personaje seleccionado
        character_image = character_images[character_index]
        character_rect = character_image.get_rect(center=(640, 250))
        SCREEN.blit(character_image, character_rect)

        # Mostrar el mapa seleccionado
        map_image = map_images[map_index]
        map_rect = map_image.get_rect(center=(650, 400))
        SCREEN.blit(map_image, map_rect)

        # Botones de navegación para personajes
        left_arrow_image = pygame.transform.scale(pygame.image.load("assets/Left_arrow.jpg"), (50, 50))
        LEFT_ARROW = Button(image=left_arrow_image, pos=(540, 250), text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        
        right_arrow_image = pygame.transform.scale(pygame.image.load("assets/Right_Arrow.jpg"), (50, 50))
        RIGHT_ARROW = Button(image=right_arrow_image, pos=(740, 250), text_input="", font=get_font(30), base_color="White", hovering_color="Green")

        # Botones de navegación para mapas
        left_map_arrow_image = pygame.transform.scale(pygame.image.load("assets/Left_arrow.jpg"), (50, 50))
        LEFT_MAP_ARROW = Button(image=left_map_arrow_image, pos=(650-(int(whithd_image/2))-marge_horizontal, 400), text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        
        right_map_arrow_image = pygame.transform.scale(pygame.image.load("assets/Right_Arrow.jpg"), (50, 50))
        RIGHT_MAP_ARROW = Button(image=right_map_arrow_image, pos=(650+100+marge_horizontal, 400), text_input="", font=get_font(30), base_color="White", hovering_color="Green")

        # Botón de confirmar
        CONFIRM_BUTTON = Button(image=None, pos=(640, 500), text_input="CONFIRM", font=get_font(40), base_color="White", hovering_color="Green")

        # Botón de salir
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 600), text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        # Cambiar el color cuando el mouse pasa sobre los botones
        LEFT_ARROW.changeColor(PLAY_MOUSE_POS)
        RIGHT_ARROW.changeColor(PLAY_MOUSE_POS)
        LEFT_MAP_ARROW.changeColor(PLAY_MOUSE_POS)
        RIGHT_MAP_ARROW.changeColor(PLAY_MOUSE_POS)
        CONFIRM_BUTTON.changeColor(PLAY_MOUSE_POS)
        QUIT_BUTTON.changeColor(PLAY_MOUSE_POS)

        # Actualizar los botones
        LEFT_ARROW.update(SCREEN)
        RIGHT_ARROW.update(SCREEN)
        LEFT_MAP_ARROW.update(SCREEN)
        RIGHT_MAP_ARROW.update(SCREEN)
        CONFIRM_BUTTON.update(SCREEN)
        QUIT_BUTTON.update(SCREEN)

        # Eventos de clic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEFT_ARROW.checkForInput(PLAY_MOUSE_POS):
                    character_index = (character_index - 1) % len(character_images)
                if RIGHT_ARROW.checkForInput(PLAY_MOUSE_POS):
                    character_index = (character_index + 1) % len(character_images)
                if LEFT_MAP_ARROW.checkForInput(PLAY_MOUSE_POS):
                    map_index = (map_index - 1) % len(map_images)
                if RIGHT_MAP_ARROW.checkForInput(PLAY_MOUSE_POS):
                    map_index = (map_index + 1) % len(map_images)
                if CONFIRM_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    game_interface(character_images, character_index, map_images, map_index)
                if QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    return 

        pygame.display.update()
