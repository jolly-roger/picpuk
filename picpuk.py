import cherrypy
import json
import os.path
import urllib.request
import urllib.parse

from layout import layout

from auth import isAuthorized as authorization
from auth import access as webAuth

import pics
import largefileupload


class picpuk(object):
    pics = pics.pics()
    access = webAuth.access()
    largefileupload = largefileupload.largeFileUpload()
    
    @cherrypy.expose
    def index(self, statusid = 0, *args, **kwargs):
        return layout.getIndex()
        
    @cherrypy.expose
    @authorization.isAuthorized
    def home(self):
        return layout.getHome()
        
    @cherrypy.expose
    def js(self):
        cherrypy.response.headers['Content-Type'] = "text/javascript"
        
        return layout.getJS()
    
    @cherrypy.expose
    @authorization.isAuthorized
    def upload(self):
        return layout.getUpload()


def error_page_default(status, message, traceback, version):
    d = urllib.parse.urlencode({'status': status, 'message': message, 'traceback': traceback, 'version': version,
        'data': json.dumps({'subject': 'Picpuk error',
            'base': cherrypy.request.base, 'request_line': cherrypy.request.request_line})})
    d = d.encode('utf-8')
    req = urllib.request.Request('http://localhost:18404/sendmail')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=utf-8')
    res = urllib.request.urlopen(req, d)
    return res.read().decode()

cherrypy.tree.mount(picpuk())

cherrypy.config.update({'error_page.default': error_page_default})
cherrypy.config.update({'engine.autoreload_on':False})

from cherrypy.process import servers

def fake_wait_for_occupied_port(host, port): return

servers.wait_for_occupied_port = fake_wait_for_occupied_port

#hyperloadconf = os.path.join(os.path.dirname(__file__), "picpuk.conf")
#
#cherrypy.quickstart(picpuk(), config=hyperloadconf)