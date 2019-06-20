import sqlite3

connection1 = sqlite3.connect('db\\sqlite3_lab1.sqlite')
print "open db success"
connection1.close()