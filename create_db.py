import sqlite3

conn = sqlite3.connect('music.db') 
c = conn.cursor()
c.execute('''CREATE TABLE links
             ([link TEXT UNIQUE,[date_posted] TEXT, [author] TEXT, [jump_link] TEXT)''')

conn.commit()