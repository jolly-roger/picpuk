import cherrypy
import os.path
from cherrypy import _cperror

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


def error_page_default(status, message, traceback, version):
    return "Error"

cherrypy.config.update({'error_page.default': error_page_default})



hyperloadconf = os.path.join(os.path.dirname(__file__), "picpuk.conf")

cherrypy.quickstart(picpuk(), config=hyperloadconf)