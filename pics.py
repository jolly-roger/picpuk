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
    def add(self, fileContent = None):
        if fileContent is not None:
            p = dal.pic.pic()
            picId = p.add(auth.user.getUserId())
            p.close()
            
            srcFile = cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + str(picId) + ".jpg"
            
            srcFileObj = open(srcFile, "wb", 0)
            srcFileObj.write(fileContent.file.read())
            srcFileObj.flush()
            srcFileObj.close()
            
            resizeFile = cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + str(picId) + "_500x500.jpg"
            
            subprocess.call("convert " + srcFile + " -resize '500x500' " + resizeFile, shell=True)
            #subprocess.call(["convert", srcFile, "-resize", "'200x200'", resizeFile])
            
            os.chown(srcFile, 1002, 100)
            os.chown(resizeFile, 1002, 100)
        
    @cherrypy.expose
    def getlast(self):
        p = dal.pic.pic()
        picIds = p.getLast(10)
        p.close()
        
        return  json.dumps(picIds)
       
    @cherrypy.expose 
    def get(self, fileName):
        cherrypy.response.headers['Content-Type'] = "image/jpeg"
        
        filePath = cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + fileName
        
        if os.path.exists(filePath):
            return open(filePath, "rb").read()
        else:
            return ""
        
    @cherrypy.expose 
    def getbyid(self, id):
        cherrypy.response.headers['Content-Type'] = "image/jpeg"
        
        filePath = cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + id + ".jpg"
        
        if os.path.exists(filePath):
            return open(filePath, "rb").read()
        else:
            return ""
        
    @cherrypy.expose
    @authorization.isAuthorized
    def getuserpics(self):
        p = dal.pic.pic()
        userPics = p.getUserPics(auth.user.getUserId())
        p.close()
        
        return json.dumps(userPics)