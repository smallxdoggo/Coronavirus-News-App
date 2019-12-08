import pygame

class Jewel:
    def __init__(self, surface, rect):
        super().__init__()
        self._radius = 5

        self._surface = surface
        self._color = pygame.Color(225, 225, 225)
        self._rect = rect
        
    def color(self, color):
        if color == 'red':
            self._color = pygame.Color(225, 100, 95)
        
    def draw(self):
        pygame.draw.rect(self._surface, self._color, self._rect)

        

        

class Gameboard:
    def __init__(self, surface, rows, columns):
        super().__init__()
        self._rows = rows
        self._columns = columns
        self._surface = surface
        self._color = pygame.Color(255, 255, 255)
        self._length = 20
        
        self._jewels = []
        
    


    def fill_with_jewels(self):
        width = self._surface.get_width()/self._columns
        height = self._surface.get_height()/self._rows
        rect = (0, 0, (self._surface.get_width()/self._columns), (self._surface.get_height()/self._rows))
        

        for r in range(self._rows+1):
            self._jewels.append([])
            for c in range(self._columns+1):
                rect = (c*width+2, r*height+2, width-3, height-3)
                self._jewels[r].append(Jewel(self._surface, rect))
                self._jewels[r][c].color('red')
                self._jewels[r][c].draw()

        

    def draw_board(self):
        for column in range(self._columns):
            pygame.draw.line(self._surface, self._color, ((column+1)*(self._surface.get_width()/self._columns), 0), ((column+1)*(self._surface.get_width()/self._columns), self._surface.get_height() ) )

        for row in range(self._rows):
            pygame.draw.line(self._surface, self._color, (0, (row+1)*(self._surface.get_height()/self._rows)), (self._surface.get_width(), (row+1)*(self._surface.get_height()/self._rows)))










            
