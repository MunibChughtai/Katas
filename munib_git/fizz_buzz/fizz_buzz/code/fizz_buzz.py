def generate_fizz_buzz(numbers):
    fizz_buzz_series = []

    for number in range(1, numbers + 1):
        if number % 3 == 0 and number % 5 == 0:
            fizz_buzz_series.append('FizzBuzz')
        elif number % 3 == 0:
            fizz_buzz_series.append('Fizz')
        elif number % 5 == 0:
            fizz_buzz_series.append('Buzz')
        else:
            fizz_buzz_series.append(number)
    return fizz_buzz_series
