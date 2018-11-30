#printing a list of the full path to items in a directory
#printing a list of the full path to items in a directory (excluding directories)
#printing the list of all .jpg and .png files in a directory
#printing the number of spaces in a string
#removing vowels from a string and printing it
#printing all of the words in a string that have less than 4 letters
#printing length of each word in a sentence.

import os

def png_jpg():
    dir=input("Enter the directory:")
    inc_extensions=['jpg','png']
    file_names = [fn for fn in os.listdir(dir)
              if any(fn.endswith(ext) for ext in inc_extensions)]
    print(file_names)
    
def spaces():
    print("Enter the string:")
    str=input()
    w=[w for w in str]
    print("Spaces={}".format(w.count(" ")))
    
def rem_vowels():
    str=input("Enter the string:")
    v=["a","e","i","o","u","A","E","I","O","U"]
    cons=[k for k in str if k not in v]
    print(cons)
    
def print4():
    str=input("Enter the string:")
    str=str.split(" ")
    word=[i for i in str if len(i)==4]
    print(word)
    
def print_len():
    str=input("Enter the string:")
    str=str.split(" ")
    length=[len(k) for k in str]
    print(length)
    
def full_path():
    dir=input("Enter the directory:")
    fn=os.listdir(dir)
    full_paths=[os.path.abspath(i) for i in fn]
    print(full_paths)
    
def exc_dir():
    dir=input("Enter the directory:")
    fn=os.listdir(dir)
    exc_dirs=[i for i in fn if i.isfile()]
    print(exc_dirs)
def main(): 
    full_path()
    exc_dir()
    png_jpg()       
    spaces()
    rem_vowels()
    print4()
    print_len()
main()
