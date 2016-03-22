from _winreg import *

aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged")
for i in range(1024):
    try:
        keyname = EnumKey(aKey, i)
        asubkey = OpenKey(aKey, keyname)
        val = QueryValueEx(asubkey, "Description")
        print val
    except WindowsError:
        break

