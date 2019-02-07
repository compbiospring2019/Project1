from .. import utils


def test_blosum_symmetry():
    for row in range(1, len(utils.blosum_matrix)):
        for col in range(1, len(utils.blosum_matrix)):
            r = utils.blosum_matrix[row][0]
            c = utils.blosum_matrix[0][col]
            assert utils.blosum62[r, c] == utils.blosum62[c, r]
