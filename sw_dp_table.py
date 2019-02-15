import utils
import dp_table


class SW_DPTable(object):
    def __init__(self, s1, s2):
        self.seq_1 = s1
        self.seq_2 = s2
        self.table = []
        self.aligned1 = ''
        self.aligned2 = ''
        self.score = 0

    def calculate_alignment(self):
        self.build_table()
        self.sw_base_cases()
        self.sw_fill_matrix()
        #self.backtrack()
def sw_base_cases(self):
        for row in range(len(self.table[0])):
            self.table[0][row].value = 0
        for col in range(len(self.table)):
            self.table[col][0].value = 0
def sw_fill_matrix(self):
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
