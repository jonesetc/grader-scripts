import os
import shutil
import re

import sh

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
        os.mkdir(subdir)

        # List all of the files in the student directory
        files = getfiles()

        # Move all of the files into the new directory
        for file in files:
            shutil.move(file, subdir)

        # Get back into the beginning directory
        os.chdir('..')

def compile(lab):
    # sh doesn't like the ++ in g++, so this gets around that
    gpp = sh.Command('g++')
    gpp(lab + '.cpp', _err='compile.log')
    
def test():
    if not os.path.isfile('a.out'):
        sh.echo('No executable found', _out='results.txt')
        return
    
    result = sh.Command('./a.out')
    result(_out='results.txt')

def fix_names(lab):
    files = getfiles()

    for file in files:
        os.rename(file, file.lower())
        file = file.lower()
        if re.match(lab[:3]+'.*'+lab[3:]+'.*\.cpp', file):
            os.rename(file, lab+'.cpp')

