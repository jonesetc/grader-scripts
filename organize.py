import os
import sys
import shutil

from utilities import getdirs, getfiles

if __name__ == '__main__':
    # Make sure there are enough arguments
    if len(sys.argv) < 2:
        sys.exit('Correct usage "python organize <foldername>"')

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

