import dp_table
import utils
import sys


def parse_args():
    if len(sys.argv) < 3:
        print('Please enter two file names (absolute paths)\n'
              'of sequences for sequence alignment\n'
              'with double quotes around them (if they have spaces)')
        sys.exit()

    sequence_1 = utils.read_sequence(sys.argv[1])
    sequence_2 = utils.read_sequence(sys.argv[2])

    return sequence_1, sequence_2


def main():
    seq_1, seq_2 = parse_args()

    table = dp_table.DPTable(seq_1, seq_2)
    table.calculate_alignment()
    utils.print_table(table.table)
    
    print ("score:", table.score)
    utils.print_alignment(table.aligned1, table.aligned2)


if __name__ == "__main__":
    main()
