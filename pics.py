import cherrypy
import json
import urllib.request
import subprocess
import os


import smtplib
from email.mime.text import MIMEText
import traceback


from .dal import pic as dal_pic
from .auth import user as auth_user
from .auth import isAuthorized as authorization


class pics(object):
    @cherrypy.expose
    @authorization.isAuthorized
    def add(self, fileContent = None, fileUrl = None):
        if fileContent is not None:
            p = dal_pic.pic()
            picId = p.add(auth_user.getUserId())
            p.close()
            
            srcFile = "/home/www/picpuk/" + "pics/" + str(picId) + ".jpg"
            
            srcFileObj = open(srcFile, "wb", 0)
            srcFileObj.write(fileContent.file.read())
            srcFileObj.flush()
            srcFileObj.close()
            
            resizeFile = "/home/www/picpuk/" + "pics/" + str(picId) + "_500x500.jpg"
            
            subprocess.call("convert " + srcFile + " -resize '500x500' " + resizeFile, shell=True)
            #subprocess.call(["convert", srcFile, "-resize", "'200x200'", resizeFile])
        
    @cherrypy.expose
    def getlast(self):
        p = dal_pic.pic()
        picIds = p.getLast(10)
        p.close()
        
        return  json.dumps(picIds)
       
    @cherrypy.expose 
    def get(self, fileName):
        cherrypy.response.headers['Content-Type'] = 'image/jpeg      '
        
        filePath = "/home/www/picpuk/" + "pics/" + fileName
        
        if os.path.exists(filePath):
            rd = open(filePath, "rb").read()
            return rd
        else:
            return ""
        
    @cherrypy.expose 
    def getbyid(self, id):
        cherrypy.response.headers['Content-Type'] = 'image/jpeg      '
        
        filePath = "/home/www/picpuk/" + "pics/" + id + ".jpg"
        
        if os.path.exists(filePath):
            return open(filePath, "rb").read()
        else:
            return ""
        
    @cherrypy.expose
    @authorization.isAuthorized
    def getuserpics(self):
        p = dal_pic.pic()
        userPics = p.getUserPics(auth_user.getUserId())
        p.close()
        
        return json.dumps(userPics)




def sendmail(d):
    sender = 'www@dig-dns.com (www)'
    recipient = 'roger@dig-dns.com'
    
    text = d
    
    msg = MIMEText(text)
    msg['Subject'] = 'uwsgi picpuc error'
    msg['From'] = sender
    msg['To'] = recipient

    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()
    
    return 'Error'