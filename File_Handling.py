# - file handling
# "a"  Append  Open file for Appending values , create file if not Exists
# "r"  Read    [Default value] Open file for read and give error if file is not exists
# "w"  Write   Open file for writing , create file if not exists
# "x"  Create  Create file , give error if file exists
import os
# print(os.getcwd())
# Main current diractory
# print(os.path.abspath(__file__)) 
#Directory for the opened file 
print(os.path.dirname(os.path.abspath(__file__))) 
file = open("aymane.text")