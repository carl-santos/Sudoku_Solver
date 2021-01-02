rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]


boxes = cross(rows, cols)

diagonal_units = (
    [[val+key for val, key in zip(rows, cols)]] + 
    [[val+key for val, key in zip(rows, cols[::-1])]]
)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

len(grid)

list_grid = list(grid)

     
new_grid = []

for i in list_grid:
    if i == '.':
        i = '123456789'
    new_grid.append(i)

len(new_grid)


mapping = {}

for key, value in zip(boxes, new_grid):
    mapping[key] =value
    
print(mapping)

solved_values = []

for value_box in mapping.keys():
    if len(mapping[value_box]) ==  1:
        solved_values.append(value_box)
        
for value_box in solved_values:
    digit = mapping[value_box]
    for peer in peers[value_box]:
        mapping[peer] = mapping[peer].replace(digit, '')
     
   

for unit in unitlist:
    numbers = '123456789'
    for digit in numbers:
        dplaces = [value_box for value_box in unit if digit in mapping[value_box]]
        if len(dplaces) == 1:
            mapping[dplaces[0]] = digit
            
def search(values):
    """Apply depth first search to solve Sudoku puzzles in order to solve puzzles
    that cannot be solved by repeated reduction alone.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary with all boxes assigned or False

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    and extending it to call the naked twins strategy.
    """
    # TODO: Copy your code from the classroom to complete this function
    
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


mapping_s = search(mapping)        
        





















