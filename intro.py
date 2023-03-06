# import my_module as mm
from my_module import find_index, test # If we want to just import our function
# from my_module import * # This * practice is frowned upon, hjard for debugging because we don't know where functions came frojm
import sys

courses = ['History','Math','Physics','CompSci']

# index = my_module.find_index(courses, 'Math') # When 'import my_module'
# index = mm.find_index(courses, 'Math') # When 'import my_module as mm'
index = find_index(courses, 'Math') # When 'from my_module import find_index'
# print(index)
# print(test)

print(sys.path)