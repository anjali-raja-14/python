# f=open("file_name","mode")

# f=open("create_file.txt","x") # create new file 

# f=open("create_file.txt") # read new file
# data=f.read()
# print(data)

f=open("create_file1.txt","w") # create new_file

f=open("create_file.txt","w") # erase all content
f.write("welcome!") # write welcome in the file 

print(f.tell()) #tell the position