import sqlite3

db=sqlite3.connect('student.db')

c=db.cursor()
# c.execute('''DROP TABLE IF EXISTS user''')
#
c.execute('''CREATE TABLE IF NOT EXISTS user(
хобби TEXT,
имя TEXT,
фамилия TEXT,
год рождения  DATE,
бал  INTEGER
)''')

c.execute('''INSERT INTO user VALUES('футбол','Кутман',',Басарбеков','1982',10)''')
c.execute('''INSERT INTO user VALUES('музыка','Арман',',Ногойбаев','1981',7)''')
c.execute('''INSERT INTO user VALUES('рисование','Айжан',',Курманова','1982',20)''')
c.execute('''INSERT INTO user VALUES('танцы','Алина',',Майрамова','2006',5)''')
c.execute('''INSERT INTO user VALUES('читать','Айбек',',Жаркынбекова','1985',6)''')
c.execute('''INSERT INTO user VALUES('петь','Камил',',Курбаналиева','2004',15)''')
c.execute('''INSERT INTO user VALUES('бокс','Карыбек',',Ноканов','2003',7)''')
c.execute('''INSERT INTO user VALUES('футбол','Наиль',',Бобеков','2011',12)''')
c.execute('''INSERT INTO user VALUES('мода','Аяна',',Токушева','2005',10)''')


c.execute('''SELECT rowid, * FROM user ORDER BY rowid''')
item = c.fetchall()
for i in item:
    print(i)

c.execute('''SELECT  фамилия FROM user''')
print(c.fetchall())
c.execute('''UPDATE user SET имя="genius" WHERE  бал>10''')
print(c.fetchall())
c.execute('''SELECT имя FROM user WHERE бал>10 ''')
print(c.fetchall())
c.execute('''DELETE FROM user WHERE rowid %2==0 ''')
print(c.fetchall())
# for i in item:
#     if len(фамилия)>10:
#         print(фамилия)
       

db.commit()
db.close()