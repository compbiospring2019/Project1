import dp_table
import smith_waterman
import utils
import sys

err_msg = '''
Please enter two file names (absolute paths)
of sequences for sequence alignment
with double quotes around them (if they have spaces)'''


def parse_args():
    if len(sys.argv) < 3:
        print(err_msg)
        sys.exit()

    try:
        sequence_1 = utils.read_sequence(sys.argv[1])
        sequence_2 = utils.read_sequence(sys.argv[2])
    except:
        # File parsing has failed. Oops.
        print(err_msg)
        sys.exit()

    return sequence_1, sequence_2


def main():
    seq_1, seq_2 = parse_args()

    # Calculate and display Needleman-Wunsch
    print('Needleman-Wunsch alignment:\n')
    nw_table = dp_table.DPTable(seq_1, seq_2)
    nw_table.calculate_alignment()
    # utils.print_table(nw_table.table)

    print ('Score: {}'.format(nw_table.score))
    utils.print_alignment(nw_table.aligned1, nw_table.aligned2)

    # Calculate and display Smith-Waterman
    print('\n\nSmith-Waterman alignment:\n')
    sw_table = smith_waterman.SmithWaterman(seq_1, seq_2)
    sw_table.calculate_alignment()
    # utils.print_table(sw_table.table)

    print('Score: {}'.format(sw_table.score))
    print('Local alignment:')
    utils.print_alignment(sw_table.alignment_1, sw_table.alignment_2)


if __name__ == "__main__":
    main()
