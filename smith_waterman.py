import utils
import dp_table


class SmithWaterman(dp_table.DPTable):
    max_position = (0, 0)

    def calculate_alignment(self):
        self.build_table()
        self.base_cases()
        self.fill_matrix()
        self.backtrack()

    def base_cases(self):
        for row in range(len(self.table)):
            self.table[row][0].value = 0
        for col in range(len(self.table[0])):
            self.table[0][col].value = 0

    def calc_value(self, row, col):
        # Calc value and previous cell
        seq_1_char = self.seq_1[row - 1]
        seq_2_char = self.seq_2[col - 1]

        # Calc val of above, left, and diagonal
        # (based on cell vals, and blosum matrix)
        above_val = self.table[row - 1][col].value + utils.blosum62['*', seq_2_char]
        left_val = self.table[row][col - 1].value + utils.blosum62[seq_1_char, '*']
        diagonal_val = self.table[row - 1][col - 1].value + utils.blosum62[seq_1_char, seq_2_char]

        # Choose max
        max_value = max(above_val, left_val, diagonal_val)
        if max_value == diagonal_val:
            previous = (row - 1, col - 1)
        elif max_value == above_val:
            previous = (row - 1, col)
        else:
            previous = (row, col - 1)

        # if max is less than zero, set val to zero
        if max_value < 0:
            max_value = 0

        # Keep track of max val in the whole table
        if self.table[self.max_position[0]][self.max_position[1]].value < max_value:
            self.max_position = (row, col)

        # return val, prev
        return max_value, previous

    def backtrack(self):
        print('Max position: {}'.format(self.max_position))
        print('Max value: {}'.format(self.table[self.max_position[0]][self.max_position[1]].value))
        pass
