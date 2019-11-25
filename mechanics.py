from collections import deque

class Faller:
    def __init__(self):
        super().__init__()
        self._column = 1
        self._prev_column = 2
        self._max_columns = 3
        self._colors = deque([])
        self._row = 3
        
    
    def new_faller(self, column: int, faller: list):
        self._column = column - 1
        self._colors = deque(faller)

    def rotate(self):
        self._colors.rotate(1)
        
    def get_colors(self):
        return self._colors

    def get_column(self):
        return self._column
    
    def get_prev_column(self):
        return self._prev_column

    def get_row(self):
        return self._row

    def set_max_columns(self, max_columns):
        self._max_columns = max_columns
    
    def move_left(self):
        if self._column > 0:
            self._prev_column = self._column
            self._column -= 1
    
    def move_right(self):
        if self._column < self._max_columns:
            self._prev_column = self._column
            self._column += 1

    def pass_time(self):
        self._row += 1

    def freeze(self):
        self.__init__()   

        

class GameState:
    def __init__(self, rows, columns):
        super().__init__()
        self._gameboard = [[' ' for c in range(columns)] for r in range(2)]
        self._rows = rows
        self._columns = columns
        self._faller = None

    def get_gameboard(self):
        return self._gameboard
    
    def get_rows(self):
        return len(self._gameboard)

    def get_columns(self):
        return len(self._gameboard[0])

    def pass_time(self):
        for r in range(len(self._gameboard) - 1, 0, -1):
            for c in range(len(self._gameboard[0])):
                if self._gameboard[r][c] == ' ':
                    self._gameboard[r][c] = self._gameboard[r - 1][c]
                    self._gameboard[r - 1][c] = ' '
                if not self._faller == None:
                    self._faller.pass_time()

            


    def set_faller(self, faller: Faller):
        self._faller = faller


        
    def update_faller(self):
        column = self._faller.get_column()
        prev_column = self._faller.get_prev_column()
        colors = self._faller.get_colors()
        row = self._faller.get_row()

        for r in range(row-3, row):
            self._gameboard[r][prev_column - 1] = ' '
            self._gameboard[r][column - 1] = f'[{colors[r]}]'



    def empty_gameboard(self, rows, columns):
        gameboard = [[' ' for c in range(columns)] for r in range(rows)]
        for gb in gameboard:
            self._gameboard.append(gb)

    def set_gameboard(self, gameboard):
        for gb in gameboard:
            self._gameboard.append(gb)
        

        
    
    

    
