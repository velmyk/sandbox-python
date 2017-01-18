'''Reads and prints a integer series.'''
import sys

def read_series(file_path):
    '''Retrieves numbers from text file in a list.'''
    # with block controls to close file if it wasn't
    with open(file_path, mode='rt', encoding='utf-8') as read_file:
        return [int(line.strip()) for line in read_file]
    # try:
    #    read_file = open(file_path, mode='rt', encoding='utf-8')
    #     return [int(line.strip()) for line in read_file]
    # finally:
    #     read_file.close()

def main(filename):
    '''Runs main things.'''
    series = read_series(filename)
    print(series)

if __name__ == '__main__':
    main(sys.argv[1])
