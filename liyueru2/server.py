# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

import reqs



handlers = [
    (r"/stulist", reqs.CourseListHandler),
    (r"/stuedit/(\d+|new)", reqs.StudentEditHandler),
    (r"/studel/(\d+)", reqs.StudentDelHandler),
    (r"/", reqs.MainHandler),
]
application = tornado.web.Application(handlers, debug=True)
application.listen(8888)

if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
