class DPTable(object):
    def __init__(self, s1, s2):
        self.seq_1 = s1
        self.seq_2 = s2
        self.table = []

    def calculate_alignment(self):
        self.build_table()
        self.base_cases()
        self.fill_matrix()

    # Funct to build the matrix
    def build_table(self):
        self.table = [[Cell() for i in range(len(self.seq_1) + 1)] for j in range(len(self.seq_2) + 1)]

    # Funct to assign initial values to base cases
    def base_cases(self):
        for row in range(len(self.table[0])):
            self.table[0][row].value = 0

        for col in range(len(self.table)):
            self.table[row][0].value = 0

    # Funct to traverse the matrix, and assign values to each cell
    def fill_matrix(self):
        for row in range(1, len(self.table)):
            for col in range(1, len(self.table[0])):
                val, prev = self.calc_value(row, col)
                self.table[row][col].value = val
                self.table[row][col].previous = prev

    # Funct to calculate the value of each cell
    def calc_value(self, row, col):
        # Overwrite this one
        # Calculate value of cell here, based on the values & alignment of the cells around it
        # Note: char # in string is 1 less than row/col num
        value = 0
        prev_cell = (0, 0)
        return value, prev_cell

    # Funct to return the path through the graph
    def backtrack(self):
        # Overwrite this one, too
        # Should return the path through the graph (via the sequence)
        pass


class Cell(object):
    value = 0
    previous = (0, 0)

    def __str__(self):
        return str(self.value)
