'''Generates sequens of numbers and writes them to file one per line.'''
import sys
from itertools import islice, count

def sequence():
    '''Generates Raceman's sequense of numbers given length.'''
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c

def write_sequence(filename, num):
    '''Writes num members of sequence to file.'''
    with open(filename, mode='wt', encoding='utf-8') as write_file:
        write_file.writelines("{}\n".format(r) for r in islice(sequence(), num + 1))

if __name__ == '__main__':
    write_sequence(filename=sys.argv[1], num=int(sys.argv[2]))
