# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from dbconn import db_cursor

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/main.html")


class StudentListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/stu_list.html", students = dal_list_students())

class StudentEditHandler(tornado.web.RequestHandler):
    def get(self, Sno):

        stu = None
        if Sno != 'new' :
            stu = dal_get_student(Sno)
        
        if stu is None:
            stu = dict(Sno='new', Sname='', Ssex='',Sclass='', notes='')

        self.render("pages/stu_edit.html", student = stu)

    def post(self, Sno):
        Sname = self.get_argument('Sname','')
        Ssex= self.get_argument('Ssex','')
        Scass= self.get_argument('Sclass','')
        notes = self.get_argument('notes', '')

        if Sno == 'new' :
            dal_create_student(Sname, Ssex,Sclass, notes)
        else:
            dal_update_student(Sname, Ssex,Sclass, notes)

        self.redirect('/stulist')

class StudentDelHandler(tornado.web.RequestHandler):
    def get(self, Sno):
        dal_del_student(Sno)
        self.redirect('/stulist')

# -------------------------------------------------------------------------

def dal_list_students():
    data = []
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT Sno, Snme, Ssex, Sclass, notes FROM student ORDER BY Sno 
        """
        cur.execute(s)      
        for r in cur.fetchall():
            stu = dict(Sno=r[0], Sname=r[1], Ssex=r[2],Sclass=r[3], notes=r[4])
            data.append(stu)
    return data


def dal_get_student(Sno):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT Sno, Sname, Ssex,Sclass, notes FROM student WHERE Sno=%s
        """
        cur.execute(s, (Sno, ))
        r = cur.fetchone()
        if r :
            return dict(Sno=r[0], Sname=r[1], Ssex=r[2],Sclass=r[3], notes=r[4])


def dal_create_student(Sname,Ssex,Sclass, notes):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        cur.execute("SELECT nextval('seq_Sno')")
        Sno = cur.fetchone()
        assert Sno is not None

        print('新学生内部序号%d: ' % Sno)

        s = """
        INSERT INTO student (Sno, Sname, Ssex,Sclass, notes) 
        VALUES (%(Sno)s, %(Sname)s, %(Ssex)s,%(Sclass)s, %(notes)s)
        """
        cur.execute(s, dict(Sno=Sno,  Sname=Sname,Ssex=Ssex, Sclass=Sclass,  notes=notes))


def dal_update_student(Sno,Sname,Ssex,Sclass, notes):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        UPDATE student SET 
          Sname=%(Sname)s,
          Ssex=%(Ssex)s,
          Sclass=%(Sclass)s, 
          notes=%(notes)s 
        WHERE Sno=%(Sno)s
        """
        cur.execute(s, dict(Sno=Sno,  Sname=Sname,Ssex=Ssex,Sclass=Sclass, notes=notes))


def dal_del_student(Sno):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        DELETE FROM student WHERE Sno=%(Sno)s
        """
        cur.execute(s, dict(Sno=Sno))
        print('删除%d条记录' % cur.rowcount)
