from collections import deque

class Faller:
    def __init__(self):
        super().__init__()
        self._column = 1
        self._prev_column = 2
        self._max_columns = 3
        self._colors = deque([])
        self._row = 3
        self._is_frozen = True
        self._freezing = False
        self._left_is_blocked = False
        self._right_is_blocked = False
        self._freezing_row = 99
    
    def new_faller(self, column: int, faller: list):
        self._row = 3
        self._column = column
        self._prev_column = column
        self._colors = deque(faller)
        self._is_frozen = False
        self._freezing = False

    def rotate(self):
        self._colors.rotate(1)
        print(self._colors)


    def set_freezing(self, row):
        self._freezing = True 
        self._freezing_row = row
        print('FREEZING')

    def is_freezing(self):
        return self._freezing   

    def get_freezing_row(self):
        return self._freezing_row

    def get_colors(self):
        return list(self._colors)

    def get_column(self):
        return self._column
    
    def get_prev_column(self):
        return self._prev_column

    def get_row(self):
        return self._row
    
    def set_row(self, row):
        self._row = row

    def set_max_columns(self, max_columns):
        self._max_columns = max_columns
    
    def left_is_blocked(self, blocked):
        self._left_is_blocked = blocked


    def right_is_blocked(self, blocked):
        self._right_is_blocked = blocked

   

    def move_left(self):
        if self._column > 0 and not self._is_frozen and not self._left_is_blocked:
            self._prev_column = self._column
            self._column -= 1
            print(self._left_is_blocked)
    
    def move_right(self):
        if self._column < self._max_columns+1 and not self._is_frozen and not self._right_is_blocked:
            self._prev_column = self._column
            self._column += 1
            print(self._right_is_blocked)

    def pass_time(self):
        self._row += 1
        self._prev_column = self._column

    def freeze(self):
        self._colors = deque([])
        self._row = 3
        self._is_frozen = True
        self._freezing = False
        self._left_is_blocked = True
        self._right_is_blocked = True 


        

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

    def get_faller(self):
        return self._faller

    def update_faller(self, faller: Faller):
        self._faller = faller
        column = self._faller.get_column()
        prev_column = self._faller.get_prev_column()
        colors = self._faller.get_colors()
        row = self._faller.get_row()
        is_freezing = self._faller.is_freezing()
        freezing_row = self._faller.get_freezing_row()
        print(row)
        print(colors)

        
         
        print(f'freezing is {is_freezing}')

        if freezing_row < row and is_freezing:
            for r in range(row-3, row):  
                prev_column = column
                self._gameboard[r-1][column-1] = f'{colors[row - r - 1]}'
            self._faller.freeze()
            print('FROZE')
        elif row >= len(self._gameboard) or not self._gameboard[row][column] == ' ' :
            for r in range(row-3, row):  
                prev_column = column
                self._gameboard[r][column-1] = f'|{colors[row - r - 1]}|'
            self._faller.set_freezing(row)
            freezing_row = row   
           
        else:
            for r in range(row-3, row):  
                prev_column = column
                self._gameboard[r][column-1] = f'[{colors[row - r - 1]}]'

        print(f'freezing is {self._faller.is_freezing()}')
        
        print("test")
        
        
    def move_faller(self, faller):
        self._faller = faller
        column = self._faller.get_column()
        prev_column = self._faller.get_prev_column()
        colors = self._faller.get_colors()
        row = self._faller.get_row()
        is_freezing = self._faller.is_freezing()
        print(row)
        print(colors)
        

        if not self._gameboard[row][column-2] == ' ':
            print('left is blocked')
            self._faller.left_is_blocked(True)
        else:
            print('left is NOT blocked')
            self._faller.left_is_blocked(False)

        if not self._gameboard[row][column] == ' ':
            print('right is blocked')
            self._faller.right_is_blocked(True)
        else:
            print('right is NOT blocked')
            self._faller.right_is_blocked(False)

        if not prev_column == column:
            for r in range(row-3, row):
                self._gameboard[r][prev_column-1] = ' '  
        


    def empty_gameboard(self):
        gameboard = [[' ' for c in range(self._columns)] for r in range(self._rows)]
        for gb in gameboard:
            self._gameboard.append(gb)

    def set_gameboard(self, gameboard):
        for gb in gameboard:
            self._gameboard.append(gb)
        
   

        
    
    

    
