# dialogue.py
import random
from config import get_font
import pygame

class DialogueManager:
    def __init__(self):
        self.character_dialogue = ""
        self.villain_dialogue = ""
        self.player_correct_dialogues = [
            "¡Eso está bien hecho! ¡Sigue así!",
            "¡Impresionante! ¡Continúa así!",
            "¡Lo lograste! ¡Bien hecho!",
            "¡Vaya, qué rápido! ¡Siguiente pregunta!"
        ]
        self.player_incorrect_dialogues = [
            "¡Oh no! ¡Intenta otra vez!",
            "¡Eso estuvo cerca! Pero no es correcto.",
            "¡Casi! Pero aún falta un poco.",
            "¡Ay, no! ¡Debes pensar mejor!"
        ]
        self.villain_correct_dialogues = [
            "¡Oh no, es un desastre para ti!",
            "¡Te lo dije! Estaba claro que no lo lograrías.",
            "¡Jajaja! ¡Te vencí!",
            "¡Qué mal, pero me alegra que sigas jugando!"
        ]
        self.villain_incorrect_dialogues = [
            "¡¿Cómo?! ¡Esto no puede ser!",
            "¡Esto no puede ser! ¿Cómo lo hiciste?",
            "¡Te estoy subestimando!",
            "¡No puede ser! Esto no estaba en mis planes..."
        ]

    def update_dialogue(self, is_correct):
        if is_correct:
            self.character_dialogue = random.choice(self.player_correct_dialogues)
            self.villain_dialogue = random.choice(self.villain_incorrect_dialogues)
        else:
            self.character_dialogue = random.choice(self.player_incorrect_dialogues)
            self.villain_dialogue = random.choice(self.villain_correct_dialogues)

    def display_dialogue(self, character_rect, villain_rect):
        # Cuadro de diálogo para el personaje principal
        char_dialog_rect = pygame.Rect(character_rect.x - 50, character_rect.y - 100, 350, 80)
        pygame.draw.rect(SCREEN, (0, 0, 0), char_dialog_rect, border_radius=15)
        pygame.draw.rect(SCREEN, (255, 255, 255), char_dialog_rect, 2)

        if self.character_dialogue:
            self.render_text(self.character_dialogue, char_dialog_rect, character_rect)

        # Cuadro de diálogo para el villano
        villain_dialog_rect = pygame.Rect(villain_rect.x - 50, villain_rect.y - 100, 350, 80)
        pygame.draw.rect(SCREEN, (0, 0, 0), villain_dialog_rect, border_radius=15)
        pygame.draw.rect(SCREEN, (255, 255, 255), villain_dialog_rect, 2)

        if self.villain_dialogue:
            self.render_text(self.villain_dialogue, villain_dialog_rect, villain_rect)

    def render_text(self, dialogue, dialog_rect, rect):
        lines = wrap_text(dialogue, get_font(16), dialog_rect.width - 20)
        y_offset = rect.y - 90
        for line in lines:
            text_surface = get_font(16).render(line, True, "White")
            SCREEN.blit(text_surface, (rect.x - 40, y_offset))
            y_offset += get_font(16).get_height()
