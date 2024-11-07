import pygame, sys
from config import SCREEN, get_font
from button import Button
from question import QuizManager
import random
from utils import wrap_text
from dialogs import player_correct_dialogues, player_incorrect_dialogues, villain_correct_dialogues, villain_incorrect_dialogues

# Cargar imágenes de los personajes
villain_image = pygame.image.load("assets/villain.png")

# Variables de nivel y progreso
questions_per_level = 6
required_correct_answers = 7

def game_interface(listaCharacters, character_index, listaMaps, indexMap ):
    # Inicializar el administrador de preguntas
    quiz_manager = QuizManager()
    correct_answers = 0
    feedback_text = ""  # Texto de retroalimentación
    feedback_color = (255, 255, 255)  # Color de la retroalimentación (por defecto blanco)

    # Frases de diálogo inicial
    character_dialogue = ""
    villain_dialogue = ""

    # Tamaño del rectángulo para los cuadros de diálogo
    dialog_rect_width = 350
    dialog_rect_height = 80
    max_text_width = dialog_rect_width - 20  # Descontamos un margen de 10 píxeles a cada lado
    map_image = pygame.transform.scale(listaMaps[indexMap], (1280, 720))

    while True:
        SCREEN.blit(map_image, (0, 0))
        pause_button = Button(image=None, pos=(1000, 50), text_input="Salir ", font=get_font(16), base_color="White", hovering_color="Green")
        pause_button.update(SCREEN)

        # Mostrar el menú de pausa al hacer clic en el botón
        font = get_font(16)
        text = 'Nivel '
        render = font.render(text, True, (0, 0, 0))
        SCREEN.blit(render, (50, 50))
        text2 = str(quiz_manager.get_level())
        render2 = font.render(text2, True, (0, 0, 0))
        SCREEN.blit(render2, (150, 50))

        # Mostrar personaje y villano
        character_image = pygame.transform.scale(listaCharacters[character_index], (50, 50))
        villain_rect = villain_image.get_rect(center=(900, 300))
        character_rect = character_image.get_rect(center=(380, 300))

        SCREEN.blit(character_image, character_rect)
        SCREEN.blit(villain_image, villain_rect)

        # Cuadro de diálogo tipo cómic para cada personaje
        char_dialog_rect = pygame.Rect(character_rect.x - 50, character_rect.y - 100, dialog_rect_width, dialog_rect_height)
        pygame.draw.rect(SCREEN, (0, 0, 0), char_dialog_rect, border_radius=15)
        pygame.draw.rect(SCREEN, (255, 255, 255), char_dialog_rect, 2)

        if character_dialogue:
            char_font = get_font(16)
            lines = wrap_text(character_dialogue, char_font, max_text_width)
            y_offset = character_rect.y - 90
            for line in lines:
                text_surface = char_font.render(line, True, "White")
                SCREEN.blit(text_surface, (character_rect.x - 40, y_offset))
                y_offset += char_font.get_height()

        villain_dialog_rect = pygame.Rect(villain_rect.x - 50, villain_rect.y - 100, dialog_rect_width, dialog_rect_height)
        pygame.draw.rect(SCREEN, (0, 0, 0), villain_dialog_rect, border_radius=15)
        pygame.draw.rect(SCREEN, (255, 255, 255), villain_dialog_rect, 2)

        if villain_dialogue:
            villain_font = get_font(16)
            lines = wrap_text(villain_dialogue, villain_font, max_text_width)
            y_offset = villain_rect.y - 90
            for line in lines:
                text_surface = villain_font.render(line, True, "White")
                SCREEN.blit(text_surface, (villain_rect.x - 40, y_offset))
                y_offset += villain_font.get_height()

        # Agregar "VS" entre los personajes
        vs_text = get_font(60).render("VS", True, "White")
        vs_rect = vs_text.get_rect(center=(640, 300))
        SCREEN.blit(vs_text, vs_rect)

        # Cuadro de diálogo para preguntas
        dialog_surface = pygame.Surface((1200, 300), pygame.SRCALPHA)
        dialog_surface.fill((169, 169, 169, 150))  # Color gris con transparencia (150 es el nivel alfa)

        # Dibujar el borde del cuadro de diálogo
        pygame.draw.rect(SCREEN, (255, 255, 255), (100, 520, 1200, 300), 2)  # Bordes blancos

        # Blitear el fondo con transparencia sobre la pantalla
        SCREEN.blit(dialog_surface, (100, 520))

        # Obtener la pregunta actual
        question = quiz_manager.get_question()
        question_text = get_font(16).render(question["question"], True, "black")
        SCREEN.blit(question_text, (120, 530))

        # Opciones
        num_columns = 2
        num_rows = (len(question["options"]) + num_columns - 1) // num_columns

        option_buttons = []
        option1 = question["options"][0]
        option2 = question["options"][1]
        option3 = question["options"][2]
        option4 = question["options"][3]

        x_pos = 300
        y_pos = 600
        option_button = Button(image=None, pos=(x_pos, y_pos), text_input=option1, font=get_font(12), base_color="black", hovering_color="Green")
        option_buttons.append(option_button)
        option_button.update(SCREEN)

        option_button = Button(image=None, pos=(x_pos, y_pos + 80), text_input=option2, font=get_font(12), base_color="black", hovering_color="Green")
        option_buttons.append(option_button)
        option_button.update(SCREEN)

        option_button = Button(image=None, pos=(x_pos + 500, y_pos), text_input=option3, font=get_font(12), base_color="black", hovering_color="Green")
        option_buttons.append(option_button)
        option_button.update(SCREEN)

        option_button = Button(image=None, pos=(x_pos + 500, y_pos + 80), text_input=option4, font=get_font(12), base_color="black", hovering_color="Green")
        option_buttons.append(option_button)
        option_button.update(SCREEN)

        # Cuadro de retroalimentación
        if feedback_text:
            feedback_rect = pygame.Rect(100, 450, 1080, 50)
            pygame.draw.rect(SCREEN, (0, 0, 0), feedback_rect)
            pygame.draw.rect(SCREEN, (255, 255, 255), feedback_rect, 2)
            feedback_label = get_font(30).render(feedback_text, True, feedback_color)
            SCREEN.blit(feedback_label, (120, 460))

        # Si el juego terminó, mostrar el botón "Finalizar"
        if quiz_manager.game_over():
            game_over_text = get_font(12).render("¡Has perdido! Inicie de nuevo.", True, "Black")
            game_over_rect = game_over_text.get_rect(center=(640, 350))
            SCREEN.blit(game_over_text, game_over_rect)

            # Crear el botón de "Finalizar"
            finish_button = Button(image=None, pos=(640, 400), text_input="Finalizar", font=get_font(30), base_color="black", hovering_color="Red")
            finish_button.update(SCREEN)

            # Si se hace clic en el botón de finalizar, se cierra el juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if finish_button.checkForInput(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
     
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.checkForInput(pygame.mouse.get_pos()): 
                    return  # Volver al inicio

                for button in option_buttons:
                    if button.checkForInput(pygame.mouse.get_pos()):
                        # Verificar si la respuesta es correcta
                        if quiz_manager.check_answer(button.text_input):
                            correct_answers += 1
                            feedback_text = "¡Respuesta Correcta!"
                            feedback_color = (0, 255, 0)
                            character_dialogue = random.choice(player_correct_dialogues)
                            villain_dialogue = random.choice(villain_correct_dialogues)
                        else:
                            feedback_text = "¡Respuesta Incorrecta!"
                            feedback_color = (255, 0, 0)
                            character_dialogue = random.choice(player_incorrect_dialogues)
                            villain_dialogue = random.choice(villain_incorrect_dialogues)

                        # Avanzar al siguiente nivel si se alcanza el número de respuestas correctas
                        if quiz_manager.advance_level==False:
                            character_dialogue = "¡Has alcanzado el máximo nivel! ¡Felicidades!"
                            villain_dialogue = "¡Maldito, me has derrotado!"
                            

                        break

        pygame.display.update()
