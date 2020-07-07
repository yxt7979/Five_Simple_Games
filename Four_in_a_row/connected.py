import numpy as np
import pygame
import sys
import math

color_player_1 = (10, 220, 200)
color_player_2 = (100, 160, 80)

ROW_COUNT = 6
COLUMN_COUNT = 7

# init the board
def creat_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

# put the chess in
def drop_piece(board,row,col,piece):
    board[row][col] = piece

# is empty
def is_valid_location(board,col):
    return board[ROW_COUNT - 1][col] == 0

# find the place to set
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# overturn
def print_board(board):
    print(np.flip(board,0))

# four ways to win
def winning_move(board,piece):
    # Check horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # check (n,n)
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # check (-n,-n)
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

# draw
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,(52,112,192),(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,(0,0,0),(int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RASIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, color_player_1, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RASIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, color_player_2, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RASIUS)
        pygame.display.update()


board = creat_board()
print(board)
game_over = False
turn = 0    # 0->player1, 1->player2

pygame.init()

SQUARESIZE = 70
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width,height)

RASIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace",75)

while not game_over:

    # catch what user does
    for event in pygame.event.get():

        # Quit
        if event.type == pygame.QUIT:
            sys.exit()

        # move
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,(0,0,0),(0,0,width,SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen,color_player_1,(posx,int(SQUARESIZE/2)),RASIUS)
            else:
                pygame.draw.circle(screen, color_player_2, (posx, int(SQUARESIZE / 2)), RASIUS)
        pygame.display.update()

        # click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,(0,0,0),(0,0,width,SQUARESIZE))
            # Ask what player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = math.floor(posx/SQUARESIZE)

                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,1)

                    if(winning_move(board,1)):
                        label = myfont.render("Player 1 !!", 1,(255,255,255))
                        screen.blit(label,(0,0))
                        print("PLAYER 1 WIN!!!")
                        game_over = True

            # Ask Player 2 input
            else:
                posx = event.pos[0]
                col = math.floor(posx/SQUARESIZE)

                if is_valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,2)
                    if (winning_move(board, 2)):
                        label = myfont.render("Player 2 !!", 1, (255,255,255))
                        screen.blit(label, (0, 0))
                        print("PLAYER 1 WIN!!!")
                        game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)

