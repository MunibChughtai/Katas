from yatzy import *

def test_roll_dice():
    res =roll_one_dice()
    assert res >=1 and res <=6

def test_roll_multiple_dice():
    inp = ['', '', '-','-', '']
    roll_multiple_dice(inp)
    assert inp[0] >=1 and inp[0]<=6 and inp[1] >= 1 and inp[1] <= 6 and inp[4] >= 1 and inp[4] <= 6

def test1_eval_score_chance():
    inp=['1', '1', '3', '3', '6']
    assert eval_score_chance(inp) == 14

def test2_eval_score_chance():
    inp = ['4' , '5' , '5' , '6' , '1']
    assert eval_score_chance(inp) == 21

def test1_eval_score_yatzy():
    inp = ['4', '4', '4', '4', '4']
    assert eval_score_yatzy(inp) == 50

def test2_eval_score_yatzy():
    inp = ['1','1','1','2','1']
    assert eval_score_yatzy(inp) == 0

def test1_eval_score_ones():
    inp = ['3','3','3','4','5']
    assert eval_score_ones_to_sixes(inp,'1') == 0

def test1_eval_score_twos():
    inp = ['2','3','2','5','1']
    assert eval_score_ones_to_sixes(inp, '2') == 4

def test1_eval_score_threes():
    inp = ['3','3','3','4','5']
    assert eval_score_ones_to_sixes(inp,'3') == 9

def test1_eval_score_fours():
    inp = ['1','1','2','4','4']
    assert eval_score_ones_to_sixes(inp,'4') == 8

def test1_eval_score_fives():
    inp = ['3','3','3','4','5']
    assert eval_score_ones_to_sixes(inp,'5') == 5

def test1_eval_score_sixes():
    inp = ['6','6','6','6','6']
    assert eval_score_ones_to_sixes(inp,'6') == 30

def test1_eval_score_pair():
    inp = ['3', '3', '3', '4', '4']
    assert eval_score_pair(inp) == 8

def test2_eval_score_pair():
    inp = ['1','1','6','2','6']
    assert eval_score_pair(inp) == 12

def test3_eval_score_pair():
    inp = ['3','3','3','4','1']
    assert eval_score_pair(inp) == 6

def test4_eval_score_pair():
    inp = ['3','3','3','3','1']
    assert eval_score_pair(inp) == 6

def test1_eval_score_two_pair():
    inp = ['1', '1', '2', '3', '3']
    assert eval_score_pair(inp,2, 2, -1) == 8

def test2_eval_score_two_pair():
    inp = ['1', '1', '2', '3', '4']
    assert eval_score_pair(inp,2, 2, -1) == 0

def test3_eval_score_two_pair():
    inp = ['1', '1', '2', '2', '2']
    assert eval_score_pair(inp,2, 2, -1) == 6

def test1_eval_score_three_pair():
    inp = ['3', '3', '3', '4', '5']
    assert eval_score_pair(inp,3, 1, -1) == 9

def test2_eval_score_three_pair():
    inp = ['3', '3', '4', '5', '6']
    assert eval_score_pair(inp, 3, 1, -1) == 0

def test3_eval_score_three_pair():
    inp = ['3', '3', '3', '3', '1']
    assert eval_score_pair(inp, 3, 1, -1) == 9

def test1_eval_score_four_pair():
    inp = ['2', '2', '2', '2', '5']
    assert eval_score_pair(inp, 4, 1, -1) == 8

def test2_eval_score_four_pair():
    inp = ['2', '2', '2', '5', '5']
    assert eval_score_pair(inp, 4, 1, -1) == 0

def test3_eval_score_four_pair():
    inp = ['2', '2', '2', '2', '2']
    assert eval_score_pair(inp, 4, 1, -1) == 8

def test1_eval_score_small_straight():
    inp = ['1', '2', '3', '4', '5']
    assert eval_score_small_large_straight(inp, 'small')==15

def test2_eval_score_small_straight():
    inp = ['1', '2', '3', '4', '6']
    assert eval_score_small_large_straight(inp, 'small')==0

def test1_eval_score_large_straight():
    inp = ['2','3','4','5', '6']
    assert eval_score_small_large_straight(inp, 'large')==20

def test2_eval_score_large_straight():
    inp = ['1', '2', '3', '4', '6']
    assert eval_score_small_large_straight(inp, 'large')==0

def test1_eval_score_full_house():
    inp = ['1','1','2','2','2']
    assert eval_score_full_house(inp) == 8