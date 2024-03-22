import sqlite3

db=sqlite3.connect('op40.db')

c=db.cursor()
# c.execute('''DROP TABLE IF EXISTS user''')

c.execute('''CREATE TABLE IF NOT EXISTS user(
имя TEXT,
текст TEXT,
оценка INTEGER,
возраст DATE,
никнейм TEXT
)''')

# CREATE - INSERT INTO

c.execute('''INSERT INTO user VALUES ('бека', 'text',12,'2003-06-06','ogil')''')
c.execute('''INSERT INTO user (имя,возраст) VALUES ('beka',18)''')


# UPDATE - UPDATE
c.execute('''UPDATE user SET возраст=18 WHERE rowid<3 ''')


# delete - delete
c.execute('''DELETE FROM user WHERE rowid=2''')


# REED-SELECT return
c.execute('''SELECT rowid,* FROM user ORDER BY rowid DESC ''')
item=c.fetchall()
for i in item:
    print(i)




db.commit()
db.close()