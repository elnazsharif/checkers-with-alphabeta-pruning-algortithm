import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
RED = (218, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (35, 159, 64)
YELLOW = (253, 236, 166)
GRAY = (128, 128, 128)
DRAW = False


CROWN = pygame.transform.scale(pygame.image.load('devil.png'), (60, 60))
CROWN1 = pygame.transform.scale(
    pygame.image.load('angel.jpg'), (60, 60))
BG = pygame.image.load("mainbg.jpg")
BG2 = pygame.image.load("BG2.jpg")
