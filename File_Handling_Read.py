# --------------------------------
# -- File Handling => Read File --
# --------------------------------
myFile = open('./aymane.text' , 'r' , encoding='utf-8')
 # Read all file Data 
# print(myFile.read())
# print(myFile.readline()) 
# print(myFile.readlines()) 

# next(myFile)

for line in myFile:
    print(line)
    if line.startswith('I olso'):
        break;

# Close The File 
myFile.close()