
class Solver:
    def __init__(self, input_file):
        self.input_file = input_file

    def run(self):
        self.grid = list()

        with open(self.input_file, 'r') as f:
            rows = f.readlines()

        for row in rows:
            self.grid.append(list(map(int, row[:-1].split(','))))

    def print(self):
        num_rows = len(self.grid)
        num_cols = len(self.grid[1])


        for i in range(9):
            if i in [0, 3, 6]:
                print('-----------------------')

            for j in range(9):
                print(self.grid[i][j], end=' ')
                if j in [2, 5, 8]:
                    print('|', end=' ')
            
            print()
        print('-----------------------')

    def __str__(self):
        num_rows = len(self.grid)
        num_cols = len(self.grid[0])

        result = []

        for i in range(num_rows):
            if i in [0, 3, 6]:
                result.append('-----------------------')

            row = []
            for j in range(num_cols):
                row.append(str(self.grid[i][j]))
                if j in [2, 5, 8]:
                    row.append('|')
        
            result.append(' '.join(row))
    
        result.append('-----------------------')

        return '\n'.join(result)

    def get_presence(self, grid):
        row = [{num: False for num in range(1, 10)} for _ in range(9)]
        column = [{num: False for num in range(1, 10)} for _ in range(9)]
        quadrant = [{num: False for num in range(1,10)} for _ in range(9)]

        for row_id in range(9):
            for col_id in range(9):
                
                # Check value in grid at current position
                current_value = grid[row_id][col_id]
                if current_value > 0:
                    row[row_id][current_value] = True
                    column[col_id][current_value] = True
                    quadrant[row_id // 3 * 3 + col_id // 3][current_value] = True
        return row, column, quadrant

    def get_possible_values(self, grid):
        """
        Return: a dictionary for empty locations and their possible values

        """
        rows, cols, quadrants = self.get_presence(grid)
        possible_values = {}

        for row_id in range(9):
            for col_id in range(9):
                curren_value = grid[row_id][col_id]

                # If value in current grid position is empty (==0)
                if curren_value == 0:
                    possible_values[(row_id, col_id)] = []

                    # Fill possible_values dictionary with possible values for the current position, that don't conflict 
                    # with values already in the row, column, or quandrant
                    for num in range(1, 10):
                        if (not rows[row_id][num]) and (not cols[col_id][num]) and (not quadrants[row_id // 3 * 3 + col_id // 3][num]):
                            possible_values[(row_id, col_id)].append(num)
        return possible_values

    def simple_update(self, grid):
        """
            Fill empty cells that have only one possible value.
        """
        update_again = False
        possible_values = self.get_possible_values(grid)

        for row_id, col_id in possible_values:
            if len(possible_values[(row_id, col_id)]) == 1:
                update_again = True
                grid[row_id][col_id] = possible_values[(row_id, col_id)][0]
        
        # Recursively update with new possible values.
        if update_again:
            grid = self.simple_update(grid)

        return grid

    def recur_solve(self, grid):
        grid = self.simple_update(grid)
        possible_values = self.get_possible_values(grid)
        # All cells in grid are filed
        if len(possible_values) == 0:
            return grid

        # Find empty cell with fewest possible values.
        fewest_num_values = 10
        for row_id, col_id in possible_values:
            # Invalid move
            if len(possible_values[(row_id, col_id)]) == 0:
                return False

            if (len(possible_values[(row_id, col_id)]) < fewest_num_values):
                fewest_num_values = len(possible_values[(row_id, col_id)])
                target_location = (row_id, col_id)

        for value in possible_values[target_location]:
            duplicate_cells = deepcopy(grid)
            duplicate_cells[target_location[0]][target_location[1]] = value
            potential_sol = recur_solve(duplicate_cells)

            # Return when a valid solution is found.
            if potential_sol:
                return potential_sol

        # Return if no valid solution found
        return False

sudoku_solver = Solver('sudoku_input_2.txt')
sudoku_solver.run()
print(sudoku_solver)
sudoku_solver.recur_solve(sudoku_solver.grid)
print(sudoku_solver)
