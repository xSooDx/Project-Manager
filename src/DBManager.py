import sqlite3

def DBstart(a):
	DB= sqlite3.connect(a+"Projects.db")