import sys
sys.path.insert(0, '..')

import dp_table, utils

def test_base_cases():
    test_table = dp_table.DPTable("12345", "12345")
    test_table.build_table()
    test_table.base_cases()
    utils.print_table(test_table.table)

test_base_cases()
