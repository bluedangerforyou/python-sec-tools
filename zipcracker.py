import zipfile
from threading import Thread
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found Password ' + password + '\n'
    except:
        pass
def main():
    zipperfile = raw_input("Please enter zip file to crack : ")
    zFile = zipfile.ZipFile(zipperfile)
    dicfile = raw_input("Please enter your dictionary file: ")
    passFile = open(dicfile)
    for line in passFile.readlines():
        password = line.strip('\n')
        print("Cracking zip...")
        try:
            zFile.extractall(pwd=password)
            print '[+] Password = ' + password + '\n'
            t = Thread(target=extractFile, args=(zFile, password))
            t.start()
            raw_input()
            exit(0)
        except Exception, e:
                pass
if __name__ == '__main__':
    main()
