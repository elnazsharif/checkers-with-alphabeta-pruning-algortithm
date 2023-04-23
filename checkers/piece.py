import pygame
from .constants import WHITE, GRAY, SQUARE_SIZE, CROWN, CROWN1, BLACK


class Piece:
    PADDING = 5
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        '''this function draw border of peices and put the crown images for kings '''
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

        if self.king:
            if self.color == WHITE:
                win.blit(CROWN1, (self.x - CROWN1.get_width() //
                                  2, self.y - CROWN1.get_height()//2))
            elif self.color == BLACK:
                win.blit(CROWN, (self.x - CROWN.get_width() //
                                 2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        '''we recalculate the x and y position inside our board when change our row and column'''
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
