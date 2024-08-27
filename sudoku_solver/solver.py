
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



sudoku_solver = Solver('sudoku_input_2.txt')
sudoku_solver.run()
print(sudoku_solver)
