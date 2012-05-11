import cherrypy
import json
import urllib.request
import subprocess

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
        
        open(srcFile, "wb").write(fileContent.file.read())
        
        resizeFile = cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + str(picId) + "_200x200.jpg"
        
        subprocess.call(["convert", srcFile, "-resize '200x200'", ])
        
    @cherrypy.expose
    def getlast(self):
        p = dal.pic.pic()
        picIds = p.getLast(10)
        p.close()
        
        return  json.dumps(picIds)
       
    @cherrypy.expose 
    def get(self, fileName):
        return open(cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + fileName, "rb").read()