#!/usr/bin/python

# Author: Nishad Trivedi

# TODO
# Use file w/out python in front []
# Specify file name []
# Delete file       []

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
    notes = sys.argv[1:]
    with open('notes.txt', 'w+') as f:
        line = ' '.join(notes)
        f.write("%s\n" % notes)
        f.close()

def read():
    try:
        with open('notes.txt', 'r') as f:
            print
            print f.read()
    except IOError:
        prompt = '> '
        print "The file hasn't been created yet. Should I create it? [y/n]" # sub file_name for file
        print prompt,
        answer = raw_input().lower()
        if answer in ["yes", "y"]:
            with open('notes.txt', 'w+') as f:
                print "Write something otherwise press 'n'"
                print prompt,
                notes = raw_input()
                if notes in ["no", "n"]:
                    pass
                else:
                    f.write("%s\n" % notes)
                    f.close()
        else:
            pass

def version():
    version = 0.1
    print "Using v%s" % version


def help():
    print """\n
               n.py [notes]        Writes notes into notes.txt
               n.py [-r, read]     Read notes from notes.txt
               n.py [-d, delete]   Deletes file
               n.py [-h, help]     Opens help menu
               n.py [-v, version]  Version number
             \n
          """

def delete():
    os.remove("notes.txt")

if __name__ == "__main__":
    main()
