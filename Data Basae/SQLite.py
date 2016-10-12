import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")


def insert_data():
    c.execute("INSERT INTO example VALUES('python' , 2.7 , 'Blabla' )")
    conn.commit()


def insert_dynamic_data():
    lang = input("What language: ")
    version = float(input("What is the version: "))
    skill = input("What skill level: ")

    c.execute("INSERT INTO example(Language, Version, Skill) VALUES(?,?,?)", (lang, version, skill))
    conn.commit()


def read_from_database():

    what_skill = input("What skill you are searching for: ")
    what_language = input("What language you are Searching for: ")

    sql = "SELECT * FROM example WHERE Skill = ? AND Language = ?"

    for row in c.execute(sql, [(what_skill), (what_language)]):
        print(row)


def read_limited_data():
    sql = "SELECT * FROM example LIMIT 2"

    for row in c.execute(sql):
        print(row)

def read_all():
    sql = "SELECT * FROM example"

    for row in c.execute(sql):
        print(row)



def update_in_database():
    sql = "UPDATE example SET Skill = 'Intermediate' where Skill = 'Expert'"

    for row in c.execute(sql):
        print(row)
        conn.commit()



def delete_fromm_database():
    sql = "DELETE FROM example WHERE Skill = 'Blabla' "

    c.execute(sql)




delete_fromm_database()
read_all()


conn.close()