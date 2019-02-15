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
        
        for row in range(len(self.table[0])):
            self.table[0][row].value = row * -1
            self.table[0][row].previous = self.table[0][row - 1]
            self.table[0][row].char1 = '-'
            self.table[0][row].char2 = self.seq_1[0]
            

        for col in range(len(self.table)):
            cols = self.table[col][0]
            cols.value = col * -1
            cols.previous = self.table[col - 1][0]
            cols.char1 = self.seq_2[0]
            cols.char2 = '-'

    # Funct to traverse the matrix, and assign values to each cell
    def fill_matrix(self):
        for col in range(1, len(self.table[0])):
            for row in range(1, len(self.table)):
                val, prev = self.calc_value(row, col)
                self.table[row][col].value = val
                self.table[row][col].previous = prev
    
    # Funct to calculate the value of each cell
    def calc_value(self, row, col):
        # Overwrite this one
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
            value = utils.blosum62[current.char1, '*']
        elif (left.value > diagonal.value) and (left.value > above.value):
            prev_cell = left
            current.char1 = '-'
            current.char2 = self.seq_2[row - 1]
            value =  utils.blosum62['*', current.char2]
        else: 
            prev_cell = diagonal
            current.char1 = self.seq_1[col - 1]
            current.char2 = self.seq_2[row - 1]
            
            value = utils.blosum62[current.char1, current.char2]
        
        return value, prev_cell

    # Funct to return the path through the graph
    def backtrack(self):
        # Overwrite this one, too
        # Should return the path through the graph (via the sequence)
        self.table[0][0].previous = None
        n = len(self.seq_1)
        m = len(self.seq_2)
        current = self.table[m][n]
        
        while current.previous is not None:
            
            self.score += current.value
            self.aligned1 += current.char1

            print(current.char1)
            self.aligned2 += current.char2
            print(current.char2)
            
            
            #print(current.previous)
            current = current.previous

        self.aligned1 = self.aligned1[::-1]
        self.aligned2 = self.aligned2[::-1]


class Cell(object):
    value = 0
    previous = (0, 0)
    char1 = ''
    char2 = ''

    def __str__(self):
        return str(self.value)
