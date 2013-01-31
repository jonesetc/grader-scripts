import os
import sys
import shutil

def getdirs():
    files = os.listdir('.')
    files = [f for f in files if f[0] != '.']
    files = [f for f in files if os.path.isdir(f)]

    return files

def getfiles():
    files = os.listdir('.')
    files = [f for f in files if f[0] != '.']
    files = [f for f in files if os.path.isfile(f)]

    return files

def organize(subdir):
    # Since each student has a directory, we must list all directories
    students = getdirs()

    for student in students:
        # Go into each directory
        os.chdir(student)

        # Make the new directory in the student folder
        os.mkdir(sys.argv[1])

        # List all of the files in the student directory
        files = getfiles()

        # Move all of the files into the new directory
        for file in files:
            shutil.move(file, sys.argv[1])

        # Get back into the beginning directory
        os.chdir('..')
