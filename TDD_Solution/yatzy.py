import random

def roll_one_dice():
    return random.randint(1,6)

def roll_multiple_dice(inp):
    for key, val in enumerate(inp):
        if val =='-':
            continue
        inp[key] = roll_one_dice()

def _get_int_list_for_number(inp, num=0):
    if num==0:
        return [int(i) for i in inp]
    else:
        return [int(i) for i in inp if i == num]

def eval_score_chance(inp, num=0):
    return sum(_get_int_list_for_number(inp, num))

def eval_score_yatzy(inp):
    if inp== ['1','1','1','1','1'] or inp == ['2','2','2','2','2'] or inp == ['3','3','3','3','3'] or inp == ['4','4','4','4','4'] or inp == ['5','5','5','5','5'] or inp == ['6','6','6','6','6']:
        return 50
    else:
        return 0

def eval_score_ones_to_sixes(inp, one_to_six):
    return eval_score_chance(inp,one_to_six)


def eval_score_pair(inp, no_chars_per_match=2, match_pair=1, first_match_ignore=-1):
    ctr=6
    pair_ctr=0
    res= []

    while (ctr>0):
        lst = _get_int_list_for_number(inp, str(ctr))
        if len(lst)>=no_chars_per_match:

            if first_match_ignore ==-1:
                pair_ctr += 1
                res.extend(lst[0:no_chars_per_match])
            else:
                first_match_ignore=-1
            if (pair_ctr == match_pair):
                return sum(res)
        ctr-=1
    return 0

def eval_score_small_large_straight(inp, mode='small'):
    if mode=='small':
        if len(set(['1','2','3','4','5']) - set(inp))==0:
            return 15
        else:
            return 0
    elif mode =='large':
        if len(set(['2','3','4','5', '6']) - set(inp))==0:
            return 20
        else:
            return 0

def eval_score_full_house(inp):
    if eval_score_pair(inp, 3, 1, -1) >0 and eval_score_pair(inp, 2, 1, 1)>0:
        return (eval_score_pair(inp, 3, 1, -1)+ eval_score_pair(inp, 2, 1, 1))
