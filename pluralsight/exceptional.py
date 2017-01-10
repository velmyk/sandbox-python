'''A module for demonstrating exceptions.'''

import sys
import os

def convert(value_to_convert):
    '''Convert to an integer.'''
    try:
        return int(value_to_convert)
    except (ValueError, TypeError) as error:
        print('Conversion error: {}!'\
            .format(str(error)),
              file=sys.stderr)
        raise

def make_at(path, dir_name):
    '''Creates a directory at required path.

    Args:
        path: Location of a new folder
        dir_name: Folder name to create
    '''
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as error:
        print(error, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)
