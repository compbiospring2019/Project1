import utils
import dp_table


class SmithWaterman(dp_table.DPTable):
    max_position = (0, 0)

    def calculate_alignment(self):
        self.build_table()
        self.sw_base_cases()
        self.sw_fill_matrix()
        self.backtrack()

    def base_cases(self):
        for row in range(len(self.table[0])):
            self.table[0][row].value = 0
        for col in range(len(self.table)):
            self.table[col][0].value = 0

    def calc_value(self, row, col):
        # Calc value and previous cell

        # Calc val of above, left, and diagonal
        above_val = self.table[row - 1][col] + utils.blosum62[]
        # (based on cell vals, and blosum matrix)
        # Choose max
        # if max is less than zero, set val to zero
        # return val, prev

        pass

'''
    def fill_matrix(self):
        max_value = 0
        max_position = self.table[0][0]
        for row in range(1, len(self.table)):
            for col in range(1, len(self.table[0])):
                val, prev = self.calc_value(row, col)
                if val < 0:
                    val = 0
                if max_value <= val:
                    max_value = val
                    max_position = self.table[row][col]

                current = self.table[row][col]
                current.value = val
                current.previous = prev
'''