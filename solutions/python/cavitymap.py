# Solution for the problem "Cavity Map"
# https://www.hackerrank.com/challenges/cavity-map/problem

# Order of the square
order = int(input())

# Initializing the depths matrix as empty
depths = []

for rowIndex in range(0, order):
    # Each row is inserted into the matrix by initially split to individual characters and each mapper to integer
    depths.append(list(map(int, list(input().strip()))))

for rowIndex in range(1, order - 1):
    # This is an optimization used. If the immediately previous cell in a row is already marked as cavity, we don't
    # need to check the current cell. It cannot be a cavity. So we can check a cell
    previousCellCavity = False
    for columnIndex in range(1, order - 1):
        if previousCellCavity:
            # If the previous cell is a cavity, the current cell cannot be a cavity. So we reset the flag
            previousCellCavity = False
            continue

        # The cell just above the current cell (previous row)
        previousRowCell = depths[rowIndex - 1][columnIndex]

        # If the cell just above this one is a cavity, just skip the current one as it cannot be a cavity
        if previousRowCell == 'X':
            continue

        # We need to get all the other three cell depths surrounding the current cell
        previousColumnCell = depths[rowIndex][columnIndex - 1]
        nextRowCell = depths[rowIndex + 1][columnIndex]
        nextColumnCell = depths[rowIndex][columnIndex + 1]

        # Depth of the current cell
        currentCellDepth = depths[rowIndex][columnIndex]

        # We are checking whether the depths of all surrounding cells to verify whether they are strictly less than
        # current cell
        if currentCellDepth > previousRowCell and currentCellDepth > previousColumnCell and currentCellDepth > nextRowCell and currentCellDepth > nextColumnCell:
            # We mark current cell as cavity so we can skip the next cell
            previousCellCavity = True
            # We put an 'X' mark in the grid
            depths[rowIndex][columnIndex] = 'X'

for rowIndex in range(0, order):
    # For each row, we map the int values back to string and join them using empty string
    print(''.join(map(str, depths[rowIndex])))