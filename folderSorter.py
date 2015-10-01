import os
import time
import shutil

def createFolders():
    if not os.path.exists("./CurrentFiles"):
        os.makedirs('CurrentFiles')
    if not os.path.exists("./OlderFiles"):
        os.makedirs('OlderFiles')

def folderSorter():
    timeSplitter = 60*60*24*30
    files = os.listdir('.')

    x = time.time() - os.path.getctime(files[1])
    for file in files:
        if file != 'CurrentFiles' or file != 'OlderFiles':
            fileSecondsExisted = time.time() - os.path.getctime(file)
            if fileSecondsExisted >= timeSplitter:
                shutil.move(file, 'OlderFiles')
            else if fileSecondsExisted < timeSplitter:
                shutil.move(file, 'NewerFiles')
            else:
                print "Error has occured"
                return
    


def main():
    folderSorter()

main()
