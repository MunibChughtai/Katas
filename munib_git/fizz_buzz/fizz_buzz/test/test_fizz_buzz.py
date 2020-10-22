from fizz_buzz.code.fizz_buzz import generate_fizz_buzz


def test_n_numbers_fizz_buzz():
    assert generate_fizz_buzz(10) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz',
                                      7, 8, 'Fizz', 'Buzz'
                                      ]
