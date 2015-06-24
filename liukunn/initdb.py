#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS student;

    CREATE TABLE IF NOT EXISTS student  (
        Sno      INTEGER,     --学号
        Sname   TEXT,        --姓名
        Ssex     TEXT,        --性别
        Sclass   TEXT,        --班级
        notes    TEXT,
        PRIMARY KEY(Sno)
    );
    -- CREATE UNIQUE INDEX idx_student_no ON student(Sno);

    CREATE SEQUENCE seq_Sno 
        START 1310650101 INCREMENT 1 OWNED BY student.Sno;

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句
    
def init_data():
    sqlstr = """
    DELETE FROM student;

    INSERT INTO student (Sno, Sname, Ssex,Sclass)  VALUES 
        (1310650101, '刘坤',  '女','1班'), 
        (1310650102, '李悦茹',  '男','1班'),
        (1310650103, '于洪庆',  '女','1班'),
        (1310650104, '高新宇',  '女','1班');
        
    """
    with db_cursor() as cur :
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')

