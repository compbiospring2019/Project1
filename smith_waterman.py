import utils
import dp_table


class SmithWaterman(dp_table.DPTable):
    max_position = (0, 0)

    def get_score(self):
        # Save the max score (for printing purposes)
        self.score = self.get_cell(self.max_position).value

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
        current_position = self.max_position
        current_cell = self.get_cell(current_position)
        alignment_1 = list()
        alignment_2 = list()

        while current_cell.value > 0:
            if not current_cell.previous:
                print('Something has gone terribly wrong.')

            if current_position[0] == current_cell.previous[0]:
                # Previous cell was to the left
                alignment_1.insert(0, '-')
                alignment_2.insert(0, self.seq_2[current_position[1] - 1])
            elif current_position[1] == current_cell.previous[1]:
                # Previous cell was above
                alignment_1.insert(0, self.seq_1[current_position[0] - 1])
                alignment_2.insert(0, '-')
            else:
                # Previous cell was diagonal
                alignment_1.insert(0, self.seq_1[current_position[0] - 1])
                alignment_2.insert(0, self.seq_2[current_position[1] - 1])

            current_position = current_cell.previous
            current_cell = self.get_cell(current_position)

        self.alignment_1 = ''.join(alignment_1)
        self.alignment_2 = ''.join(alignment_2)

    def get_cell(self, position_tuple):
        return self.table[position_tuple[0]][position_tuple[1]]
