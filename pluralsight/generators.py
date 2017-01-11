'''Exploring generators.'''

from comprehensions import is_prime

def simple_generator():
    '''Shows when generator executes it\'s body and yields values.'''
    print('About to yield 1')
    yield 1
    print('About to yield 2')
    yield 2
    print('About to yield 3')
    yield 3
    print('About to return')

def take(count, iterable):
    '''Take items from the front of an iterable.

    Args:
        count: The maximum number of items to retrieve.
        iterable: The source series.

    Yields:
        A most 'count' items from 'iterable'.
    '''
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def run_take():
    '''Uses run() to print yielded values.'''
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)

def distinct(iterable):
    '''Return unique items by eliminating duplicates.

    Args:
        iterable: The sourse series.

    Yields:
        Unique elements in order from 'iterable'.
    '''
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    '''Uses distinct() to print yielded values.'''
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)

def run_pipeline():
    '''Take first specified number of items.'''
    items = [5, 7, 7, 6, 5, 5]
    for item in take(3, distinct(items)):
        print(item)

def lucas():
    '''Yields infinite series of lucas numbers.'''
    yield 2
    before_previos = 1
    previos = 2
    while True:
        yield previos
        before_previos, previos = previos, before_previos + previos

def run_lucas():
    '''Prints lucas values.'''
    for number in lucas():
        print(number)

def sum_of_prime_squares(max_number):
    '''Calculates sum of squares for prime numbers less then defined max number.'''
    # squares = (x*x for x in range(max_number) is is_prime(x))
    # squares are the generator and not evaluated yet
    # Created long list for million squares (all numbers but not only prime)
    # will be 10Mb in size: list(squares).
    #
    # Executing list(squares) one more time will return empty list because squares is a generator
    # and it already yielded all values after first call.
    return sum(x*x for x in range(1, max_number + 1) if is_prime(x))

if __name__ == '__main__':
    print('"run_take" says:')
    run_take()
    print('"run_distinct" says:')
    run_distinct()
