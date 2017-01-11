'''Finds first element in iterable.'''

def first(iterable):
    '''Finds first element in iterable.'''
    iterator = iter(iterable)
    try:
        print(next(iterator))
    except StopIteration:
        raise ValueError('Iterable is empty')

if __name__ == '__main__':
    first(['Spring', 'Summer', 'Autemn', 'Winter'])
    first({'1st', '2nd', '3rd'})
    first({'a': 1, 'b': 2})
    first(set())

