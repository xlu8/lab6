from os import system
readfile=raw_input("enter file to read:")
data=open("{0}".format(readfile),"rb").read()
writefile=raw_input("enter file to write: ")
f=open("./{0}".format(writefile),"wb")
f.write(data)
f.close()
print("executing the file...")
system("chmod 777 Q1Result.txt;")
