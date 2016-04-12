import os

text = raw_input("Enter your text to add: ")
file = raw_input("Enter name of a visible file to inject hidden text into- could be any file ext: ")
fileh = raw_input("Enter name of hidden file with ext: ")
f = open(file, "a")
os.popen("echo "+text + ">" + file+":"+fileh)

raw_input("Press any key to exit")
