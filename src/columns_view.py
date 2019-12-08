import pygame

class Jewel:
    def __init__(self, surface):
        super().__init__()
        self._radius = 5

        self._surface = surface
        self._color = pygame.Color(225, 225, 225)
        
    def color(self, color):
        if color == 'red':
            self._color = pygame.Color(225, 100, 95)
        
    def draw(self):
        pygame.draw.circle(self._surface, self._color, (300, 300), 100)
        

        

class Gameboard:
    def __init__(self, surface, rows, columns):
        super().__init__()
        self._rows = rows
        self._columns = columns
        self._surface = surface
        self._color = pygame.Color(255, 255, 255)
        self._length = 20
        self._points = []
        
        

        

    def draw_board(self):
        for column in range(self._columns):
            pygame.draw.line(self._surface, self._color, ((column+1)*(self._surface.get_width()/self._columns), 0), ((column+1)*(self._surface.get_width()/self._columns), self._surface.get_height() ) )

        for row in range(self._rows):
            pygame.draw.line(self._surface, self._color, (0, (row+1)*(self._surface.get_height()/self._rows)), (self._surface.get_width(), (row+1)*(self._surface.get_height()/self._rows)) )










            
