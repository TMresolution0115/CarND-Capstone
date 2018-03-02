import os
import re
import shutil

# get current directory
path = os.getcwd()

# list files in current dir
files = os.listdir(path)
counter = 0

for file in files:
    index = re.search('.jpg',file)  
    if index:
        counter += 1

print(counter)

files.sort()
new_folder = path+'_'+str(counter)+'_div4'
if not os.path.exists(new_folder):
    os.mkdir(new_folder)

for i in range(0,counter):
    # get every 5 file
    if i%4 == 0:
        shutil.copyfile(files[i],new_folder+'/'+files[i])

