import cherrypy
import json
import urllib.request
import subprocess
import os

import dal.pic
import auth.user


from auth import isAuthorized as authorization


class pics(object):
    @cherrypy.expose
    @authorization.isAuthorized
    def add(self, fileContent):
        p = dal.pic.pic()
        picId = p.add(auth.user.getUserId())
        p.close()
        
        srcFile = cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + str(picId) + ".jpg"
        
        srcFileObj = open(srcFile, "wb", 0)
        srcFileObj.write(fileContent.file.read())
        srcFileObj.flush()
        srcFileObj.close()
        
        resizeFile = cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + str(picId) + "_400x400.jpg"
        
        subprocess.call("convert " + srcFile + " -resize '400x400' " + resizeFile, shell=True)
        #subprocess.call(["convert", srcFile, "-resize", "'200x200'", resizeFile])
        
    @cherrypy.expose
    def getlast(self):
        p = dal.pic.pic()
        picIds = p.getLast(10)
        p.close()
        
        return  json.dumps(picIds)
       
    @cherrypy.expose 
    def get(self, fileName):
        return open(cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + fileName, "rb").read()