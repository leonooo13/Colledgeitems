import pymysql as sql
Host='x.x.x.x' #ip
User='root'
Pword='root' 
DBname='flask_chat'

def get_post():
    try:
        db=sql.connect(host=Host,user=User,password=Pword,database=DBname)
        print('db_success')
    except sql.Error as e:
        print('连接失败')
        print(str(e))
    cursor=db.cursor()
    cursor.execute("select content,time from posts order by time desc")
    posts=cursor.fetchall()
    db.close()
    return posts

def add_post(content):
    try:
        db=sql.connect(host=Host,user=User,password=Pword,database=DBname)
        print('post数据库连接成功')
    except sql.Error as e:
        print("post数据库连接失败"+str(e))
    c=db.cursor()
    sqlquery="insert into posts(content,time) value (%s,%s)"
    c.execute(sqlquery,content)
    db.commit()
    db.close()

def del_cnt():
    try:
        db=sql.connect(host=Host,user=User,password=Pword,database=DBname)
        print('post数据库连接成功')
    except sql.Error as e:
        print("post数据库连接失败"+str(e))
    c=db.cursor()
    sqlquery="delete from posts where id like (select * from (select max(id) from posts) tmp)"
    c.execute(sqlquery)
    db.commit()
    db.close()