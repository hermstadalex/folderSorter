import os
import time
import shutili

""" This program separates the files and folders in a directory into a folder for
    new files and a folder for old files. Both the number of days a file is to be
    considered old, and the names of the new and old folders are given by input
    from the user.
"""


# Mostly written for testing. Unpacks the oldFolder and newFolder and moves everything
# back out into the main directory.
def unpackFolders(newFolderName, oldFolderName):
    moveToLoc = os.getcwd()
    os.chdir(oldFolderName)
    files = os.listdir('.')
    for file in files:
        shutil.move(file, moveToLoc)
    os.chdir(moveToLoc)
    os.chdir(newFolderName)
    files = os.listdir('.')
    for file in files:
        shutil.move(file, moveToLoc)
    os.chdir(moveToLoc)

# Gets the user's input for either the folder names or the day count distnguisher.
# If the boolean argument folderMode is true, the day count distinguisher is not
# asked for.
def getUserInput(folderMode):
    if folderMode != True:
        timeSplitterDays = int(raw_input("Enter the number of days you want to" +
        " distinguish between current and old: "))
        return timeSplitterDays
    else:
        newFolderName = str(raw_input("Enter the name of the folder with new files:"
        " "))
        oldFolderName = str(raw_input("Enter the name of the folder with old files:"
        " "))
        return  (newFolderName, oldFolderName)

def folderSorter():
    timeSplitterDays = getUserInput(False)
    timeSplitter = 60 * 60 * 24 * timeSplitterDays # Time value at which files are separated
    newFolderName, oldFolderName = createFolders()
    files = os.listdir('.')

    for file in files:
        if (file != newFolderName) and (file != oldFolderName) and (file !=
        '.git') and (file != 'folderSorter.py') and (file != 'README.md'):
            fileSecondsExisted = time.time() - os.path.getctime(file)
            if fileSecondsExisted >= timeSplitter:
                shutil.move(file, oldFolderName)
            elif fileSecondsExisted < timeSplitter:
                shutil.move(file, newFolderName)
            else:
                print "Error has occured"
                return

def createFolders():
    newFolder, oldFolder = getUserInput(True)
    print newFolder
    print oldFolder
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)
    if not os.path.exists(oldFolder):
        os.makedirs(oldFolder)
    return newFolder, oldFolder


def main():
    folderSorter()

main()
