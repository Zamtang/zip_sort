import tkinter
from tkinter import filedialog

def select_folder():
    root = tkinter.Tk()
    root.withdraw()
    dir_path = filedialog.askdirectory(parent=root,initialdir="./",title='Please select a directory')
    print("\ndir_path : ", dir_path)

    return dir_path