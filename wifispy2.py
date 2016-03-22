from __future__ import print_function
import itertools

try:
    from winreg import *
except ImportError: # Python 2
    from _winreg import *

KEY_READ_64 = KEY_READ | KEY_WOW64_64KEY
ERROR_NO_MORE_ITEMS = 259

def iterkeys(key):
    for i in itertools.count():
        try:
            yield EnumKey(key, i)
        except OSError as e:
            if e.winerror == ERROR_NO_MORE_ITEMS:
                break
            raise

def itervalues(key):
    for i in itertools.count():
        try:
            yield EnumValue(key, i)
        except OSError as e:
            if e.winerror == ERROR_NO_MORE_ITEMS:
                break
            raise

def val2addr(val):
    return ':'.join('%02x' % b for b in bytearray(val))

NET_UNMANAGED = (r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
                 r"\NetworkList\Signatures\Unmanaged")

def printNets(keystr=NET_UNMANAGED):
    key = OpenKey(HKEY_LOCAL_MACHINE, keystr, 0, KEY_READ_64)
    print('\n[*] Networks You Have Joined.')
    for guid in iterkeys(key):
        netKey = OpenKey(key, guid)
        netName, macAddr = '', ''
        for name, data, rtype in itervalues(netKey):
            if name == 'FirstNetwork':
                netName = data
            elif name == 'DefaultGatewayMac':
                macAddr = val2addr(data)
        if netName:
            print('[+]', netName, macAddr)
        CloseKey(netKey)
    CloseKey(key)