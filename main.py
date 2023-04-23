# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
import sys
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BG, GREEN, BLACK, DRAW, BG2
from checkers.game import Game
from minimax.algorithm import minimax, minimax2
import time

# number of frames shown per unit
FPS = 60

# initial the pygame, call __init__.py
pygame.init()

# set up the game windows and puting background image
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIDTHMenu = 800
HEIGHTMenu = 800
WINDOW = pygame.display.set_mode((WIDTHMenu, HEIGHTMenu))
pygame.display.set_caption('Checkers')
WINDOW.blit(BG, (0, 0))

# Set up the fonts for rule page
FONT = pygame.font.SysFont('comicsans', 18)

# Set up the buttons menu
BUTTON_COLOR = RED
BUTTON_TEXT_1 = 'Easy Game'
BUTTON_TEXT_2 = 'Advanced Game'
BUTTON_TEXT_3 = 'Rules'
BUTTON_FONT = pygame.font.SysFont('comicsans', 40)
button_rect_1 = pygame.Rect(250, 300, 300, 70)
button_rect_2 = pygame.Rect(250, 400, 300, 70)
button_rect_3 = pygame.Rect(250, 500, 300, 70)


button_text_1 = BUTTON_FONT.render(BUTTON_TEXT_1, True, WHITE)
WINDOW.fill(BUTTON_COLOR, rect=button_rect_1)
WINDOW.blit(button_text_1, (300, 300, 300, 70))

button_text_2 = BUTTON_FONT.render(BUTTON_TEXT_2, True, WHITE)
WINDOW.fill(BUTTON_COLOR, rect=button_rect_2)
WINDOW.blit(button_text_2, (250, 400, 300, 70))

button_text_3 = BUTTON_FONT.render(BUTTON_TEXT_3, True, WHITE)
WINDOW.fill(BUTTON_COLOR, rect=button_rect_3)
WINDOW.blit(button_text_3, (350, 500, 300, 70))


# Update the screen
pygame.display.update()


def get_row_col_from_mouse(pos):
    '''this returns the position of our mouse'''
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    '''rendering a paragraph in pygame'''
    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button_rect_1.collidepoint(pos):
                    '''this is the beginner level with the depth of 3 in minimax '''
                    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
                    pygame.display.set_caption('Game')
                    run = True
                    clock = pygame.time.Clock()
                    game = Game(WIN)
                    while run:
                        # for every second at most 60 frames should pass
                        clock.tick(FPS)

                        if game.turn == BLACK:
                            value, new_board = minimax2(
                                game.get_board(), 3, -1, 1, BLACK, game)
                            game.ai_moves(new_board)
                        if game.winner() != None:
                            if game.winner() == BLACK:

                                # if winner is black
                                pygame.display.set_caption('WINNER')
                                text = "unfortunately,  winner is Devil. You cannot be free with them. TRY AGAIN!"
                                WIN.fill(pygame.Color('white'))
                                blit_text(WIN, text, (20, 20), FONT)
                                pygame.display.update()
                                time.sleep(5)
                                run = False
                            if game.winner() == WHITE:

                                # if winner is white
                                pygame.display.set_caption('WINNER')
                                text = "Congrats, winner is Angel. You can live free from now."
                                WIN.fill(pygame.Color('white'))
                                blit_text(WIN, text, (20, 20), FONT)
                                pygame.display.update()
                                time.sleep(5)
                                run = False
                            if DRAW == True:

                                # if result becomes equall
                                pygame.display.set_caption('WINNER')
                                text = "The game result is equall. Try again and Try to win!"
                                WIN.fill(pygame.Color('white'))
                                blit_text(WIN, text, (20, 20), FONT)
                                pygame.display.update()
                                time.sleep(5)
                                run = False

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                row, col = get_row_col_from_mouse(pos)
                                game.select(row, col)

                        game.update()

                    pygame.quit()
                if button_rect_2.collidepoint(pos):
                    '''this is the advance level with the depth of 6 in minimax '''
                    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
                    pygame.display.set_caption('Game')
                    run = True
                    clock = pygame.time.Clock()
                    game = Game(WIN)
                    while run:

                        clock.tick(FPS)

                        if game.turn == BLACK:
                            value, new_board = minimax(
                                game.get_board(), 4, -1, 1, BLACK, game)
                            game.ai_moves(new_board)
                        if game.winner() != None:
                            if game.winner() == BLACK:

                                pygame.display.set_caption('WINNER')
                                text = "unfortunately, winner is Devil. You cannot be free with them. TRY AGAIN!"
                                WIN.fill(pygame.Color('white'))
                                blit_text(WIN, text, (20, 20), FONT)
                                pygame.display.update()
                                time.sleep(5)
                                run = False
                            if game.winner() == WHITE:

                                pygame.display.set_caption('WINNER')
                                text = "Congrats, winner is Angel. You can live free from now."
                                WIN.fill(pygame.Color('white'))
                                blit_text(WIN, text, (20, 20), FONT)
                                pygame.display.update()
                                time.sleep(5)
                                run = False
                            if DRAW == True:

                                pygame.display.set_caption('WINNER')
                                text = "The game result is equall. Try again and Try to win!"
                                WIN.fill(pygame.Color('white'))
                                blit_text(WIN, text, (20, 20), FONT)
                                pygame.display.update()
                                time.sleep(5)
                                run = False

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                row, col = get_row_col_from_mouse(pos)
                                game.select(row, col)

                        game.update()

                    pygame.quit()
                elif button_rect_3.collidepoint(pos):
                    # the rules window
                    NEW_WINDOW = pygame.display.set_mode(
                        (WIDTHMenu, HEIGHTMenu))

                    pygame.display.set_caption('Rules')
                    text = "This checker game has two color of pieces, one is black symbol of Devil which AI plays that"\
                        "and another is white, symbol of Angel which a human plays."\
                        "You should try to win the AI. "\
                        "You as a white piece go first.Each player receives twelve pieces."\
                        "The board had squares are laid out in eight columns and eight rows."\
                        "All the players just can have diagonal move forward from one square to an adjacent square or "\
                        "they can jump and capture the opponent piece. If player of AI has the chance, they can have two or three jump in one move."\
                        "when player selects a piece, the guidance pieces show the possible movement of his piece."\
                        "If there was a jump opportunity the guidance piece will show that."\
                        "The AI tries to move the best movement consider to human movement.and try to beat player pieces"\
                        "When each of players reach to the last row of their adjacent squares,"\
                        "they can convert their pieces to kings and their kings can move both forward and backward."\
                        "The looser is a player who has at most one piece in board."\
                        "If both of players has just one piece in the board the result is equall and the game does not have winner."\


                    NEW_WINDOW.blit(BG2, (0, 0))
                    blit_text(NEW_WINDOW, text, (20, 20), FONT)

                    pygame.display.update()


main()
