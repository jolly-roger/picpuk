import cherrypy
import os.path
import smtplib
from email.mime.text import MIMEText

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
    sender = 'www@dig-dns.com (www)'
    recipient = 'roger@dig-dns.com'
    
    text = 'Request: ' + cherrypy.request.request_line + '\n\n' +\
        'Status: ' + status + '\n\n' + 'Message: ' + message + '\n\n' +\
        'Traceback: ' + traceback + '\n\n' + 'Version: ' + version
    
    msg = MIMEText(text)
    msg['Subject'] = 'Picpuk error'
    msg['From'] = sender
    msg['To'] = recipient

    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()
    
    return "Error"

cherrypy.tree.mount(picpuk())

cherrypy.config.update({'error_page.default': error_page_default})
cherrypy.config.update({'engine.autoreload_on':False})

#hyperloadconf = os.path.join(os.path.dirname(__file__), "picpuk.conf")
#
#cherrypy.quickstart(picpuk(), config=hyperloadconf)