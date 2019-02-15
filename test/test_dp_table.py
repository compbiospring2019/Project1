import sys
sys.path.insert(0, '..')

import dp_table, utils

def test_base_cases():
    test_table = dp_table.DPTable("12345", "12345")
    test_table.build_table()
    test_table.base_cases()
    utils.print_table(test_table.table)

def test_calc_value():
    test_table = dp_table.DPTable("GCCCT", "GCGCA")
    test_table.build_table()
    test_table.base_cases()
    test_table.fill_matrix()
    utils.print_table(test_table.table)

def test_backtrack():
    test_table = dp_table.DPTable("GCCCT", "GCGCA")
    test_table.build_table()
    test_table.base_cases()
    test_table.fill_matrix()
    utils.print_table(test_table.table)
    test_table.backtrack()
    print(test_table.aligned1)
    print(test_table.aligned2)

def test_score():
    test_table = dp_table.DPTable("GCCCT", "GCGCA")
    test_table.build_table()
    test_table.base_cases()
    test_table.fill_matrix()
    test_table.get_score()
    print(test_table.score)

test_score()
