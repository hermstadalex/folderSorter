import os
import time
import shutil

def createFolders():
    if not os.path.exists("./CurrentFiles"):
        os.makedirs('CurrentFiles')
    if not os.path.exists("./OlderFiles"):
        os.makedirs('OlderFiles')

def folderSorter():
    timeSplitter = 60*60*24*30 # Time value at which files are separated
    createFolders()
    files = os.listdir('.')

    for file in files:
        if (file != 'CurrentFiles') and (file != 'OlderFiles') and (file !=
        '.git') and (file != 'folderSorter.py') and (file != 'README.md'):
            fileSecondsExisted = time.time() - os.path.getctime(file)
            if fileSecondsExisted >= timeSplitter:
                shutil.move(file, 'OlderFiles')
            elif fileSecondsExisted < timeSplitter:
                shutil.move(file, 'CurrentFiles')
            else:
                print "Error has occured"
                return
    


def main():
    folderSorter()

main()
