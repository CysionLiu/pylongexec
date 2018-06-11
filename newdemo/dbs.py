import sqlite3

con = sqlite3.connect("./my.db")
print(sqlite3.version)
s1 = "create table IF NOT EXISTS Qitem ('Rid' INTEGER PRIMARY KEY DEFAULT 1000,'iname' varchar(100),'icount' int DEFAULT 0,address VARCHAR (200))"
s2 = "insert into Qitem (iname,icount,address) VALUES ('phone',1200,'Hanghou')"
con.execute(s1)
re = con.execute(s2)
con.commit()
cur = con.execute("SELECT * FROM Qitem")
result = cur.fetchall()
for r in result:
    print(r)
