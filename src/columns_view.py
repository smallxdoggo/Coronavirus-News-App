import pygame

class Jewel:
    def __init__(self, surface):
        super().__init__()
        self._radius = 5

        self._surface = surface
        self._color = pygame.Color(225, 225, 225)
        
    def color(self, color):
        try:
            if color == ' ':
                self._color = pygame.Color(0, 0, 0) # black/background color
            elif color[0] == 'S':
                self._color = pygame.Color(200, 95, 95) # blue
            elif color[0] == 'T':
                self._color = pygame.Color(66, 135, 245) # red
            elif color[0] == 'V':
                self._color = pygame.Color(41, 186, 53) # green
            elif color[0] == 'W':
                self._color = pygame.Color(255, 162, 23) # orange
            elif color[0] == 'X':
                self._color = pygame.Color(135, 23, 255) # purple
            elif color[0] == 'Y':
                self._color = pygame.Color(255, 25, 240) # pink
            elif color[0] == 'Z':
                self._color = pygame.Color(150, 255, 252) # light teal
        except IndexError:
            pass    
    def draw(self):
        pygame.draw.circle(self._surface, self._color, (300, 300), 100)
        

        

class Gameboard:
    def __init__(self, surface, rows, columns, gameboard):
        super().__init__()
        self._rows = rows
        self._columns = columns
        self._surface = surface
        self._color = pygame.Color(255, 255, 255)
        self._length = 20
        self._points = []
        
<<<<<<< HEAD
<<<<<<< HEAD
        self._jewels = []
        self._gameboard = gameboard
    


    def fill_with_jewels(self, gameboard):
        self._gameboard = gameboard

        width = self._surface.get_width()/self._columns
        height = self._surface.get_height()/self._rows
        rect = (0, 0, (self._surface.get_width()/self._columns), (self._surface.get_height()/self._rows))
        

        for r in range(self._rows):
            self._jewels.append([])
            for c in range(self._columns+1):
                rect = (c*width+6, (r)*height+6, width-11, height-11)
                self._jewels[r].append(Jewel(self._surface, rect))
                self._jewels[r][c].color(self._gameboard[r+2][c-1])
                self._jewels[r][c].draw()
=======
        
>>>>>>> parent of c897a5d... Filled whole board with jewels
=======
        
>>>>>>> parent of c897a5d... Filled whole board with jewels

        

    def draw_board(self):
        for column in range(self._columns):
            pygame.draw.line(self._surface, self._color, ((column+1)*(self._surface.get_width()/self._columns), 0), ((column+1)*(self._surface.get_width()/self._columns), self._surface.get_height() ) )

        for row in range(self._rows):
            pygame.draw.line(self._surface, self._color, (0, (row+1)*(self._surface.get_height()/self._rows)), (self._surface.get_width(), (row+1)*(self._surface.get_height()/self._rows)) )










            
