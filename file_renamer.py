import os

os.chdir("C:\\Users\\97333\\Desktop\\NewFolder")

myName = input("Choose file name: ") #Takes user input to choose a new name for the files

count = 0 #To count the number of files in which that name change occurs

for files in os.listdir():
    file_names, file_ext = os.path.splitext(files)
    count += 1
    new_name = f"{myName} {count}{file_ext}"
    os.rename(files, new_name)
    
print(f"Succesfully changed names of {count} files!") #Prints out the number of file names succesfuly changed
