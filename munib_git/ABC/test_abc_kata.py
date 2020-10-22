import pytest
from abc_kata import *

@pytest.mark.parametrize("input, expected",
                         [
                           ("A", True),
                           ("BARK", True),
                           ("BOOK", False),
                           ("TREAT", True),
                           ("COMMON", False),
                           ("SQUAD", True),
                           ("CONFUSE", True)
                           ]
                        )
def test_can_make_word(input, expected):
  blocks_list = [('B', 'O'), ('X', 'K'), ('D', 'Q'), ('C', 'P'), ('N', 'A'), ('G', 'T'), ('R', 'E'), ('T', 'G'),
                 ('Q', 'D'), ('F', 'S'), ('J', 'W'), ('H', 'U'), ('V', 'I'), ('A', 'N'), ('O', 'B'), ('E', 'R'),
                 ('F', 'S'), ('L', 'Y'), ('P', 'C'), ('Z', 'M')]
  assert can_make_word_using_blocks(input, blocks_list) == expected
