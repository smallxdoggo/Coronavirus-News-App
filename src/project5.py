import pygame
import columns_view
import mechanics

def run() -> None:
    pygame.init()

    surface = pygame.display.set_mode((400, 700))

    running = True

    clock = pygame.time.Clock()

    rows = 13
    columns = 6

    #jewel = columns_view.Jewel(surface)
    #jewel.color('red')

    board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], ['S', 'T', 'V', 'S', 'S', 'S'], ['W', 'S', 'X', 'S', 'Y', 'S'], [' ', ' ', ' ', ' ', 'S', ' '], ['S', ' ', 'S', ' ', 'S', ' '], ['S', 'S', ' ', ' ', 'S', 'S'], ['S', ' ', ' ', 'S', 'S', ' '], [' ', ' ', ' ', ' ', ' ', ' '], ['S', 'S', 'S', ' ', ' ', ' '], ['S', ' ', 'S', ' ', 'S', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    gameboard = columns_view.Gameboard(surface, rows, columns, board)
    
    gamestate = mechanics.GameState(rows, columns)
    gamestate.set_gameboard(board)

    faller = mechanics.Faller()
    faller.set_max_columns(gamestate.get_columns())
    
    while running:
        clock.tick(1)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False

        
        gamestate.pass_time()
        board = gamestate.get_gameboard()

        surface.fill(pygame.Color(0, 0, 0))

        #jewel.draw()
        gameboard.draw_board()
        gameboard.fill_with_jewels(board)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    run()
