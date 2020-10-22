def can_make_word_using_blocks(input_word, blocks):
    input_word = input_word.upper()

    for alphabet in input_word:
        alphabet_found = False
        for index, block in enumerate(blocks):
            if alphabet in block:
                alphabet_found = True
                del blocks[index]
                break
        if not alphabet_found:
            return False
    return True


