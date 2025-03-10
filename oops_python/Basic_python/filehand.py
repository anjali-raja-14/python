f=open("file.txt","w+")
f.write("Hey Ritesh! We are discussing python file hadling! ")
f.seek(0) # move cursor at first
read1=f.read()
print(read1) # move cursor at last
f.close()