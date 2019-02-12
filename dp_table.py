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
            if row == 0:
                self.table[0][row].value = 0 
            else: 
                self.table[0][row].value = self.table[0][row - 1] - 1
        
        for col in range(len(self.table)):
            if col == 0:
                self.table[col][0].value = 0
            else:
                self.table[col][0].value = self.table[col - 1][0].value - 1 

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
        current = self.table[row][col]
        above = self.table[row - 1][col]
        left = self.table[row][col - 1]
        diagonal = self.table[row - 1][col - 1]
        
        if (above.value > left.value) and (above.value > diagonal.value): 
            prev_cell = above
            value = above.value - 1
        elif (left.value > diagonal.value) and (left.value > above.values):
            prev_cell = left
            value = left.value - 1
        else: 
            prev_cell = diagonal
            letter1 = self.seq_1[row - 1]
            letter2 = self.seq_2[col - 1]
            if letter1 == letter2:
                value = diagonal + 1
            else:
                value = diagonal - 1
        
        return value, prev_cell

    # Funct to return the path through the graph
    def backtrack(self):
        # Overwrite this one, too
        # Should return the path through the graph (via the sequence)
        aligned1 = ""
        aligned2 = ""
        n = len(self.seq_1)
        m = len(self.seq_2)
        end = self.table[m][n]
        current = end
        while (n > 0 && m > 0):
            prev = current.prev 
            if (prev == self.table[m - 1][n - 1]):
                letter1 = self.seq_1[m - 1]
                letter2 = self.seq_2[n - 1]
                aligned1 += self.seq_1[m - 1]
                aligned2 += self.seq_2[n - 1]

                n = n - 1 
                m = m - 1

            elif (prev == self.table[m - 1][n]):
                aligned1 += self.seq_1[m - 1]
                aligned2 += '-'
                m = m - 1
            elif (prev == self.table[m][n - 1]):
                aligned1 += '-'
                aligned2 += self.seq_2[n - 1]
                n = n - 1
            current = prev
        while m > 0:
            aligned1 += self.seq_1[m - 1]
            aligned2 += '-'
            m = m - 1
        while n > 0:
            aligned1 += '-'
            aligned2 += self.seq_2[n - 1]
            n = n - 1
        aligned1 = aligned1[::-1]
        aligned2 = aligned2[::-1]

    return(aligned1, aligned2)






        


class Cell(object):
    value = 0
    previous = (0, 0)

    def __str__(self):
        return str(self.value)
