#coding=utf-8;

import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
import os

# 做一些设置
settings = {
    'template_path':'template',
    'static_path':'static',
    'cookie_secret':'alexander',
}

# 注册模块
class RegisterHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
       self.render('register.html');
       # self.write("welcome");




# 首页
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("welcome");

# 路由
application = tornado.web.Application([(r"/",IndexHandler),
                                       (r"/register", RegisterHandler),
                                       ],**settings);

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.current().start();


