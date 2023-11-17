import math

BLANK_SPACE = ""
ALL_NUMS = set(range(1,10))

# Load sudoku into matrix
sudoku = []
with open('sudoku_easy.txt', 'r') as sudoku_file:
    for line in sudoku_file.readlines():
        row = []
        for char in line.strip('\n'):
            if char == " ":
                row.append(BLANK_SPACE)
            else:
                row.append(int(char))
        sudoku.append(row)

def getColumnValues(sudoku, col):
    colValues = set()
    for row in sudoku:
        val = row[col]
        if val != BLANK_SPACE:
            colValues.add(val)
    return colValues

def getRowValues(sudoku, row):
    rowValues = set()
    for val in sudoku[row]:
        if val != BLANK_SPACE:
            rowValues.add(val)
    return rowValues

def getSubMatrixValues(sudoku, row, col):
    subMatrixValues = set()

    # Find sub-matrix bounds
    sudoku_size = len(sudoku)
    sub_div = 3
    div_size = int(sudoku_size / sub_div)
    sub_matrix_start_row = (math.ceil((row+1)/div_size)-1) * div_size
    sub_matrix_start_col = (math.ceil((col+1)/div_size)-1) * div_size

    for r in range(sub_matrix_start_row,sub_matrix_start_row+div_size):
        for c in range(sub_matrix_start_col,sub_matrix_start_col+div_size):
            val = sudoku[r][c]
            if val != BLANK_SPACE:
                subMatrixValues.add(val)
    return subMatrixValues

# Iterate through the entire 2D sudoku and fill all valid possibilities at each blank space
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == BLANK_SPACE:
            row_values = getRowValues(sudoku, row)
            col_values = getColumnValues(sudoku, col)
            subMatrixValues = getSubMatrixValues(sudoku, row, col)
            possiblities = ALL_NUMS.difference(row_values, col_values, subMatrixValues)
            print(possiblities)
            if len(possiblities) == 1:
                sudoku[row][col] = possiblities.pop()