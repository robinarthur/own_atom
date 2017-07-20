#! C:\Users\tank\Anaconda3\python.exe

import os, sys, re


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

def main():
    path = "C:/Users/tank/Documents/GitHub/own_atom"
    path2 = "C:/Users/CKr/Documents/GitHub/own_atom"

    dirs = os.listdir(path)
    rmv_dirs = re.search('\.',str(dirs))
    dirs = remove_values_from_list(dirs, rmv_dirs)

    f = open("installed_packages.txt", "a")
    print(dirs)
    if f.mode == 'a':
        for file in dirs:
            print(str(file))
            f.write(str(file))

    f.close

if __name__== "__main__":
    main()
