# JERON ARTEST
# 14616419

# mechanics.py

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
        '''Creates a new faller at a specific column'''
        self._row = 3
        self._column = column
        self._prev_column = column
        self._colors = deque(faller)
        self._colors.reverse()
        self._is_frozen = False
        self._freezing = False

    def rotate(self):
        '''Rotates faller using deque'''
        self._colors.rotate(-1)
        #print(self._colors)


    def set_freezing(self, freezing, row):
        '''sets the faller as freezing at a row'''
        self._freezing = freezing 
        self._freezing_row = row
        #print('FREEZING')
 
    def is_freezing(self):
        '''gets _freezing'''
        return self._freezing   

    def is_frozen(self):
        '''gets _is_frozen'''
        return self._is_frozen

    def get_freezing_row(self):
        '''gets the freezing row'''
        return self._freezing_row

    def get_colors(self):
        '''gets the list of colors'''
        return list(self._colors)

    def get_column(self):
        '''gets the column the faller is in'''
        return self._column
    
    def get_prev_column(self):

        return self._prev_column

    def get_row(self):
        return self._row
    
    def set_row(self, row):
        self._row = row

    def set_max_columns(self, max_columns):
        '''for use in move_right() to avoid index errors'''
        self._max_columns = max_columns
    
    def left_is_blocked(self, blocked):
        '''sets left_is_blocked as True or False '''
        self._left_is_blocked = blocked


    def right_is_blocked(self, blocked):
        '''sets right_is_blocked as True or False '''
        self._right_is_blocked = blocked

   

    def move_left(self):
        '''subtracts the column'''
        if self._column > 0 and not self._is_frozen and not self._left_is_blocked:
            self._prev_column = self._column
            self._column -= 1
            #print(self._column)
            #print(self._left=_is_blocked)
    
    def move_right(self):
        '''adds the column'''
        if self._column < self._max_columns+1 and not self._is_frozen and not self._right_is_blocked:
            self._prev_column = self._column
            self._column += 1
            #print(self._column)
            #print(self._right_is_blocked)

    def pass_time(self):
        '''move the faller down'''
        self._row += 1
        self._prev_column = self._column

    def freeze(self):
        '''sets the faller as frozen'''
        self._colors = deque([])
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
        '''gets the gameboard array'''
        return self._gameboard
    
    def get_rows(self):
        '''length of the gameboard rows'''
        return len(self._gameboard)

    def get_columns(self):
        '''length of the gameboard columns'''
        return len(self._gameboard[0])

    def pass_time(self):
        '''move everything down one if it can'''
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
        '''updates the current faller appearance on the gameboard'''
        self._faller = faller
        column = self._faller.get_column()
        prev_column = self._faller.get_prev_column()
        colors = self._faller.get_colors()
        row = self._faller.get_row()
        is_freezing = self._faller.is_freezing()
        freezing_row = self._faller.get_freezing_row()
        #print(row)
        #print(colors)

        
        if row - 1 < len(self._gameboard):
            if column <= 1:
                #print('left is blocked')
                self._faller.left_is_blocked(True)
            elif not self._gameboard[row-1][column-2] == ' ':
                #print('left is blocked')
                self._faller.left_is_blocked(True)
            else:
                #print('left is NOT blocked')
                self._faller.left_is_blocked(False)

            
            if column >= self._columns:
                #print('right is blocked')
                self._faller.right_is_blocked(True)
            elif not self._gameboard[row-1][column] == ' ':
                #print('right is blocked')
                self._faller.right_is_blocked(True)
            else:
                #print('right is NOT blocked')
                self._faller.right_is_blocked(False)

        else:
            pass


         
        #print(f'freezing is {is_freezing}')

        if len(colors) > 0:
            if freezing_row < row and is_freezing:
                for r in range(row-3, row):  
                    prev_column = column
                    self._gameboard[r-1][column-1] = f'{colors[row - r - 1]}'
                self.check_game_over()
                self._faller.freeze()
                
                #print('FROZE')
            elif row >= len(self._gameboard) or not self._gameboard[row][column-1] == ' ' :
                for r in range(row-3, row):  
                    prev_column = column
                    self._gameboard[r][column-1] = f'|{colors[row - r - 1]}|'
                self._faller.set_freezing(True, row)
                freezing_row = row   
            
            else:
                for r in range(row-3, row):  
                    prev_column = column
                    self._gameboard[r][column-1] = f'[{colors[row - r - 1]}]'
                    self._faller.set_freezing(False, row)
                    

        #print(f'freezing is {self._faller.is_freezing()}')
        
        
        
    def move_faller(self, faller):
        '''updates previous column to empty'''
        self._faller = faller
        column = self._faller.get_column()
        prev_column = self._faller.get_prev_column()
        row = self._faller.get_row()
        #print(row)

        if not prev_column == column:
            for r in range(row-3, row):
                self._gameboard[r][prev_column-1] = ' ' 
        
        #print(self._gameboard[row-1][column-1])
        

         
            

    def empty_gameboard(self):
        '''initializes an empty gameboard'''
        gameboard = [[' ' for c in range(self._columns)] for r in range(self._rows)]
        for gb in gameboard:
            self._gameboard.append(gb)

    def set_gameboard(self, gameboard):
        '''sets gameboard with contents'''
        for gb in gameboard:
            self._gameboard.append(gb)
        
    def check_matches(self) -> bool:
        '''check for matches'''
        for r in range(len(self._gameboard)-1, 0, -1):
            for c in range(len(self._gameboard[0])-2):
                if not self._gameboard[r][c] == ' ' and self._gameboard[r][c] == self._gameboard[r][c+1] == self._gameboard[r][c+2]:
                    #print('COLUMNS EQUAL')
                    matches = 0
                    while c+matches+1 < len(self._gameboard[r]) and self._gameboard[r][c+matches] == self._gameboard[r][c+matches+1]:
                        matches += 1

                    for x in range(matches+1):
                        self._gameboard[r][c+x] = f'*{self._gameboard[r][c+x]}*' 
                    return True
                         
        for r in range(len(self._gameboard)-2):
            for c in range(len(self._gameboard[0])):
                if not self._gameboard[r][c] == ' ' and self._gameboard[r][c] == self._gameboard[r+1][c] == self._gameboard[r+2][c]:
                    #print('ROWS EQUAL')
                    
                    

                    for x in range(3):
                        self._gameboard[r+x][c] = f'*{self._gameboard[r+x][c]}*' 
                    return True

        for r in range(len(self._gameboard)-2):
            for c in range(len(self._gameboard[0])-2):
                if not self._gameboard[r][c] == ' ' and self._gameboard[r][c] == self._gameboard[r+1][c+1] == self._gameboard[r+2][c+2]:
                    #print('DOWN DIAGONAL EQUAL')
                    for x in range(3):
                        self._gameboard[r+x][c+x] = f'*{self._gameboard[r+x][c+x]}*' 
                    return True

        for r in range(2, len(self._gameboard)):
            for c in range(len(self._gameboard[0])-2):
                if not self._gameboard[r][c] == ' ' and self._gameboard[r][c] == self._gameboard[r-1][c+1] == self._gameboard[r-2][c+2]:
                    #print('UP DIAGONAL EQUAL')
                    for x in range(3):
                        self._gameboard[r-x][c+x] = f'*{self._gameboard[r-x][c+x]}*' 
                    return True

        return False
    
    def check_game_over(self) -> bool:
        '''checks if game over'''
        #print('checking game over')
        if not self._faller == None:
            row = self._faller.get_row()
            is_frozen = self._faller.is_frozen()
            #print(row)
            #print(is_frozen)
            if row <= 5 and is_frozen:
                return True
            else:
                return False

    def update_gameboard(self):
        '''removes matches and drops all the gameboard'''
        #print('Updating Gameboard')

        for r in range(len(self._gameboard)):
            for c in range(len(self._gameboard[0])) :
                if self._gameboard[r][c][0] == '*':
                    self._gameboard[r][c] = ' '
        
        for r in range(len(self._gameboard)-1):
            for c in range(len(self._gameboard[0])) :
                
                if not self._gameboard[r][c][0] == ' ' and self._gameboard[r+1][c][0] == ' ':
                    self.pass_time()
                    self.update_gameboard()


    