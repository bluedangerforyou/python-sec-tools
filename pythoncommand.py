import os
print"""
This is a wifi Forensics tool to display saved Wireless passwords in Windows 7.
You will need to run this tool with Administrator rights to see passwords.
You can get the SSIDs by running this command in windows:
netsh wlan show profile name=* key=clear
NOTE: SSID is case sensitive! 
file is saved into a file called wifipasswords.txt

"""
print('\n' * 7)
ssid = raw_input('Enter the name of the SSID here to dump the password for wifi: ')
os.system("netsh wlan show profile name=" + ssid + " key=clear > wifipasswords.txt")


