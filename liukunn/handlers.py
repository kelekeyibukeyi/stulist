# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from dbconn import db_cursor

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/main.html")


class CourseListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/stu_list.html", students = dal_list_students())


def dal_list_students():
    data = []
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT Sno, Sname, Ssex,Sclass, notes FROM student ORDER BY Sno 
        """
        cur.execute(s)      
        for r in cur.fetchall():
            stu = dict(Sno=r[0], Sname=r[1], Ssex=r[2],Sclass=r[3] ,notes=r[4])
            data.append(stu)
    print(data)
    return data

