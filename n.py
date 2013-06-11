#!/usr/bin/python

# Author: Nishad Trivedi

# TODO
# Use file w/out python in front [x]
# Create/write custom file [x]
# Read custom file          [x]
# Delete custom file        []
# Delete file       [x]
# implement colors?? []

# NOTES: http://stackoverflow.com/questions/1466000/python-open-built-in-function-difference-between-modes-a-a-w-w-and-r

import sys
import os


def main():
    if sys.argv[1] in ["-h", "help"]:
        help()
    elif sys.argv[1] in ["-v", "version"]:
        version()
    elif sys.argv[1] in ["-r", "read"]:
        read()
    elif sys.argv[1] in ["-d", "delete"]:
        delete()
    else:
        write()

def write():
    if sys.argv[1].endswith('.txt'):
        file_name = sys.argv[1]
        notes = sys.argv[2:]
        with open('{0}'.format(file_name), 'a+') as f:
            line = ' '.join(notes)
            f.write('%s\n' % line)
            f.close()
    else:
        notes = sys.argv[1:]
        with open('notes.txt', 'a+') as f:
            line = ' '.join(notes)
            f.write("%s\n" % line)
            f.close()

def read():
    try:
        if len(sys.argv) == 3:           # Implement this way by checking length!!!
            file_name = sys.argv[2]
            with open('{0}'.format(file_name), 'r') as f:
                print
                print f.read()
        else:
            with open('notes.txt', 'r') as f:
                print
                print f.read()
    except IOError:
        file_name = sys.argv[2]
        if file_name.endswith('txt'):
            print "%s hasn't been created yet. Should I create it? [y/n]" % file_name[:-4] #sub file_name for file
            create()
        else:
            print "Your notes don't exist. Should I create them? [y/n]"
            create()

def create():
    prompt = '> '
    print prompt,
    answer = raw_input().lower()
    if answer in ["yes", "y"]:
        with open('notes.txt', 'a+') as f:
            print "Write something otherwise press 'n'"
            print prompt,
            notes = raw_input()
            if notes in ["no", "n"]:
                pass
            else:
                f.write("%s\n" % notes)
                f.close()

def version():
    version = 0.2
    print "Using v%s" % version


def help():
    print """\n
               n.py [file] [notes]           Writes notes into file.txt (notes.txt by default)
               n.py [-r, read] [file]        Read notes from file (notes.txt by default)
               n.py [-d, delete] [file]      Deletes file (notes.txt by default)
               n.py [-h, help]               Opens help menu
               n.py [-v, version]            Version number
             \n
          """

def delete():
    if len(sys.argv) == 3:
        try:
            os.remove("%s" % sys.argv[2])
        except OSError:
            print "%s doesn't exist!" % sys.argv[2][:-4]
    else:
        try:
            os.remove("notes.txt")
        except OSError:
            pass

if __name__ == "__main__":
    main()
