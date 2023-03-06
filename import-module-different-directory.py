"""What happens when the module we want to import is not 
in the same direcotry as the script we're running?

I'm going to take my_module.py and put it on the desktop"""
# We can add the new directory to sys.path, not the best approach
import sys
sys.path.append('C:\\Users\\edgar\\OneDrive\\Desktop')
# We can add a new environment variable called "PYTHONPATH"
# and the value is 'C:\Users\edgar\OneDrive\Desktop'

from my_module import find_index, test
import os

courses = ['History','Math','Physics','CompSci']

index = find_index(courses, 'Math')

print(sys.path)
print(os.getcwd())