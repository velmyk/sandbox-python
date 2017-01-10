import sys

def sqrt(input_number):
    '''Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed.abs

    Returns:
        The square root of x.

    Raises:
        ValueError if argument is a negative number.
    '''

    if input_number < 0:
        raise ValueError("Cannot compute squarre root "
                         "of negative number {}".format(input_number))

    guess = input_number
    i = 0
    while guess * guess != input_number and i < 20:
        guess = (guess + input_number / guess) / 2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as error:
        print(error, file=sys.stderr)

    print('Program execution continues normaly here.')

if __name__ == '__main__':
    main()