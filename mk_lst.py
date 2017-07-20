#! C:\Users\tank\Anaconda3\python.exe

import os, sys

def main():
    path = "C:/Users/tank/Documents/GitHub/own_atom"
    path2 = "C:/Users/CKr/Documents/GitHub/own_atom"
    dirs = os.listdir(path2)

    f = open("installed_packages.txt", "a")
    print(dirs)
    if f.mode == 'a':
        for file in dirs:
            print(str(file))
            f.write(str(file))

    f.close

if __name__== "__main__":
    main()
