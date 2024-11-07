import pygame, sys
from config import SCREEN, BG
from menu import main_menu

def main():
    pygame.init()
    pygame.display.set_caption("DBZ")
    main_menu()

if __name__ == "__main__":
    main()
