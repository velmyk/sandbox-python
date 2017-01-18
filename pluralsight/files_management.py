'''Writes and reads the text file.'''

write_file = open('wasteland.txt', mode='wt', encoding='utf-8')
'''Writes to the text file.'''

write_file.write('My name is Bob.')
write_file.write('I am 30 yers old.')
write_file.write('I live in Kiev.\n')
write_file.write('Like traveling.')

write_file.close()

read_file = open('wasteland.txt', mode='rt', encoding='utf-8')
'''Reads from the text file.'''
read_file.read(4) # reads 4 characters from file
read_file.read()  # reads rest of the file
read_file.read()  # returns empty string because eof reached

read_file.seek(0) # moves pointer to the begining of the file

read_file.readline() # reads one line

print(read_file.readlines()) # reads all lines to the list

append_file = open('wasteland.txt', mode='at', encoding='utf-8')
'''Appends text to the file.'''
append_file.writelines([
    'One more line.\n',
    'And one more.\n'
])
append_file.close()
