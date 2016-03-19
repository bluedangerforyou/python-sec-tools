import zipfile
zipperfile = raw_input("Please enter zip file to crack : ")
zFile = zipfile.ZipFile(zipperfile)
dicfile = raw_input("Please enter your dictionary file: ")
passFile = open(dicfile)
for line in passFile.readlines():
	password = line.strip('\n')
	print("Cracking zip...")
	try:
		zFile.extractall(pwd=password)
		print '[+] Password = ' + '\n'
		exit(0)
	except Exception, e:
		pass

