import os

#os.mkdir("/Users/ming/Desktop/Python_Basics/CleanedUp") # Make Directory

folder = "/Users/ming/Desktop/Python_Basics/"
entries = os.scandir(folder)  # List all the files

for entry in entries:
    if os.path.isfile(entry): # os.path.isfile checks if it is a file
        print('File', entry.name)
    elif os.path.isdir(entry): # os.path.isdir checks if it is a directory
        print('Directory:', entry.name)