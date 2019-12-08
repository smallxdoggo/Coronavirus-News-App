import pygame
import columns_view

def run() -> None:
    pygame.init()

    surface = pygame.display.set_mode((600, 600))

    running = True

    color_amount = 0
    clock = pygame.time.Clock()
    circle_center_x = 350
    circle_center_y = 300

    jewel = columns_view.Jewel(surface)
    jewel.color('red')

    
    gameboard = columns_view.Gameboard(surface, 13, 6)
    
    while running:
        clock.tick(30)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
        #color_amount = (color_amount + 1) % 256

        circle_center_x -= 1
        circle_center_y += 1
      
        surface.fill(pygame.Color(color_amount, color_amount, color_amount))

        #jewel.draw()
        gameboard.draw_board()
        
        
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    run()
