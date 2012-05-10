import cherrypy
import json
import urllib.request

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
        
        open(cherrypy.request.app.config["hyperload"]["base_dir"] + "pics/" + str(picId) + ".jpg", "wb").write(
            fileContent.file.read())
        
    @cherrypy.expose
    def getlast(self):
        p = dal.pic.pic()
        picIds = p.getLast(10)
        p.close()
        
        cherrypy.log.error(picIds)
        
        return  json.dumps(picIds)