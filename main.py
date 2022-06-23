import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED,WHITE #importing variables from constraints
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60 #involved with rendering rather than drawing that's why not in constants folder

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption('Checkers') #display name

def get_row_col_from_mouse(pos): #takes position of our mouse 
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():  
    run = True   #for calling main loop from outside
    clock = pygame.time.Clock()  #for constant frame rate
    game = Game(WIN) 
    while run:
        clock.tick(FPS) #defined above 60FPS

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get(): #check for certain events in the game
            if event.type == pygame.QUIT: #red button end
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: #related to turns
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()