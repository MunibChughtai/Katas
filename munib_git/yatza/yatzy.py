import random

def roll_one_dice():
    return random.randint(1,6)

def subsequent_rolls(input):
    for key, dice in enumerate(input):
        if dice =='-':
            continue
        input[key] = roll_one_dice()

# this is the sum of all dices or it can be run for a specific dice
def eval_score_chance(input, specific_dice=0):
    #return sum(_get_int_list_for_dices(input, specific_dice))
    if specific_dice==0:
        return sum([int(dice) for dice in input])
    else:
        return sum([int(dice) for dice in input if dice == specific_dice])


# if all dices have same number, return 50, else return 0
def eval_score_yatzy(input):
    unique_numbers = set(input)
    return 50 if len(unique_numbers) == 1 else 0

# sum all dices occurances for a specific dice
def eval_score_for_dice_number(input, dice_number):
    return int(dice_number)* input.count(dice_number)

def _get_score_for_matches(input, no_of_matches, char_matched_or_to_ignore=[]):
    distinct_dices = list(sorted(set(input), reverse=True))

    if len(char_matched_or_to_ignore)!=0:
        distinct_dices.remove(char_matched_or_to_ignore[0])

    for dice in distinct_dices:
        if input.count(dice) >= no_of_matches:
            char_matched_or_to_ignore.append(dice)
            return int(dice)*no_of_matches
    return 0

#  sum (exactly) two highest matching dice
def evaluate_score_pair(input):
    return _get_score_for_matches(input, 2, [])

def evaluate_score_two_pairs(input):
    distinct_dices = set(input)
    dice_match=[]

    for dice in distinct_dices:
        if input.count(dice) >=4:
            dice_match.extend([dice, dice])
        elif input.count(dice) >=2:
            dice_match.append(dice)
        if (len(dice_match)==2):
            return (int(dice_match[0])*2) + (int(dice_match[1])*2)

    return 0

def evaluate_score_three_pairs(input):
    return _get_score_for_matches(input, 3, [])

def evaluate_score_four_pairs(input):
    return _get_score_for_matches(input, 4, [])

def eval_score_small_large_straight(inp, mode='small'):
    if mode=='small':
        if sorted(inp) == ['1','2','3','4','5']:
            return 15
    elif mode =='large':
        if sorted(inp) == ['2','3','4','5','6']:
            return 20
    return 0

def eval_score_full_house(input):
    char_matched_or_to_ignore=[]

    if _get_score_for_matches(input, 3, char_matched_or_to_ignore) and _get_score_for_matches(input, 2, char_matched_or_to_ignore):
        char_matched_or_to_ignore = []
        return _get_score_for_matches(input, 3, char_matched_or_to_ignore) + _get_score_for_matches(input, 2, char_matched_or_to_ignore)
    else:
        return 0