# project4.py

import mechanics


gamestate = mechanics.GameState(4, 3)
colors = ['A', 'B', 'C']
faller = mechanics.Faller()

def inputs():
    rows = input('Rows: ')
    columns = input('Columns: ')

    begin = input('Empty or w/ contents: ').upper()
    
        
        




def display():
    gameboard = gamestate.get_gameboard()
    output = ''

    for r in range(2, gamestate.get_rows()):
        output += '|'
        for c in range(gamestate.get_columns()):
            if gameboard[r][c][0] == '[' or gameboard[r][c][0] == '*':
                output += gameboard[r][c]
            else:
                output += f' {gameboard[r][c]} '
        output += '|'
        output += '\n'  

    output += ' '     
    for c in range(gamestate.get_columns()):
        output += f'---'
    output += ' '
    print(output)     

if __name__ == "__main__":
    gamestate.set_gameboard([['S', ' ', 'X'], ['V', 'W', ' '], [' ', ' ', 'Z'], [' ', ' ', ' ']])
    print(gamestate.get_gameboard())
    gamestate.pass_time()
    print(gamestate.get_gameboard())
    gamestate.pass_time()
    print(gamestate.get_gameboard())
    faller.new_faller(2, colors)
    faller.rotate()
    print(faller.get_colors())
    gamestate.set_faller(faller)
    gamestate.update_faller()
    print(gamestate.get_gameboard())
    faller.move_left()
    faller.move_left()
    gamestate.update_faller()
    gamestate.pass_time()
    print(gamestate.get_gameboard())
    gamestate.pass_time()
    print(gamestate.get_gameboard())
    display()

    

