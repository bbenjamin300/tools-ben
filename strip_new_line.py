#!/tps/bin/python

'''
1. read in file given file location
2. strip new lines at end of short paragraphs
3. leave new line for spacing between paragraphs
4. save new file with '_clean' appended before file extension


USAGE:
    > strip_new_line.py <path-to-file>
'''

import os, sys

def main(argv):
    dirName = os.path.dirname(argv)
    fileName, fileExtension = os.path.splitext(argv)
    baseName = os.path.basename(fileName)
    with open(dirName+'/'+baseName+'_clean'+fileExtension, 'w+') as outfile:
        with open(argv, 'r') as infile:
            text = infile.readlines()
            cleantext = [line.replace('\n', ' ') for line in iter(text)]
            for line in cleantext:
                if line == ' ': outfile.write('\n\n')
                else: outfile.write(line)

if __name__ == '__main__':
    main(sys.argv[1])
