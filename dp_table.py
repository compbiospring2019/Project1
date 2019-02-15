import utils


class DPTable(object):
    def __init__(self, s1, s2):
        self.seq_1 = s1.upper()
        self.seq_2 = s2.upper()
        self.table = []
        self.aligned1 = ''
        self.aligned2 = ''
        self.score = 0

    def calculate_alignment(self):
        self.build_table()
        self.base_cases()
        self.fill_matrix()
        self.backtrack()

    # Funct to build the matrix
    def build_table(self):
        self.table = [[Cell() for i in range(len(self.seq_2) + 1)] for j in range(len(self.seq_1) + 1)]

    # Funct to assign initial values to base cases
    def base_cases(self):
        
        for row in range(1, len(self.table)):
            self.table[row][0].value = self.table[row - 1][0].value - 4
            self.table[row][0].previous = self.table[row - 1][0]
            self.table[row][0].char1 = self.seq_1[row - 1]
            self.table[row][0].char2 = '-'

        for col in range(1, len(self.table[0])):
            self.table[0][col].value = self.table[0][col - 1].value - 4
            self.table[0][col].previous = self.table[0][col - 1]
            self.table[0][col].char1 = '-'
            self.table[0][col].char2 = self.seq_2[col - 1]

    # Funct to traverse the matrix, and assign values to each cell
    def fill_matrix(self):
        for row in range(1, len(self.table)):
            for col in range(1, len(self.table[0])):
                val, prev = self.calc_value(row, col)
                self.table[row][col].value = val
                self.table[row][col].previous = prev

    # Funct to calculate the value of each cell
    def calc_value(self, row, col):
        # Calculate value of cell here, based on the values & alignment of the cells around it
        # Note: char # in string is 1 less than row/col num
        current = self.table[row][col]
        above = self.table[row - 1][col]
        left = self.table[row][col - 1]
        diagonal = self.table[row - 1][col - 1]
        
        if (above.value > left.value) and (above.value > diagonal.value): 
            prev_cell = above
            current.char1 = self.seq_1[col - 1]
            current.char2 = '-'
            value = above.value + utils.blosum62[current.char1, '*']
        elif (left.value > diagonal.value) and (left.value > above.value):
            prev_cell = left
            current.char1 = '-'
            current.char2 = self.seq_2[row - 1]
            value = left.value + utils.blosum62['*', current.char2]
        else: 
            prev_cell = diagonal
            current.char1 = self.seq_1[col - 1]
            current.char2 = self.seq_2[row - 1]
            value = diagonal.value + utils.blosum62[current.char1, current.char2]
        
        return value, prev_cell

    # Funct to return the path through the graph
    def backtrack(self):
        # Should return the path through the graph (via the sequence)
        self.table[0][0].previous = None
        n = len(self.seq_1)
        m = len(self.seq_2)
        current = self.table[m][n]
        
        while current.previous is not None:
            self.aligned1 += current.char1
            self.aligned2 += current.char2
            current = current.previous

        self.aligned1 = self.aligned1[::-1]
        self.aligned2 = self.aligned2[::-1]

    def get_score(self):
        n = len(self.seq_1)
        m = len(self.seq_2)
        self.score = self.table[n][m].value

class Cell(object):
    value = 0
    previous = (0, 0)
    char1 = ''
    char2 = ''

    def __str__(self):
        return str(self.value)
