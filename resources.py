import cherrypy
import json
import urllib.request

import dal.resource
import auth.user


from auth import isAuthorized as authorization


class resources(object):
    @cherrypy.expose
    @authorization.isAuthorized
    def add(self, alias=None, domain=None):
        resourceId = -1
        
        if alias is not None and not alias == "" and domain is not None and not domain == "":
            r = dal.resource.resource()
            resourceId = r.add(alias, domain, auth.user.getUserId())
            r.close()

        return str(resourceId)
            
    @cherrypy.expose
    @authorization.isAuthorized
    def getuserall(self):
        r = dal.resource.resource()
        resources = r.getuserall(auth.user.getUserId())
        r.close()
        
        return  json.dumps(resources)
        
    @cherrypy.expose
    @authorization.isAuthorized
    def verify(self, resourceId):
        isVerified = False
        r = dal.resource.resource()
        resource = r.get(int(resourceId))
        
        verificationData = str(urllib.request.urlopen(resource[0][2] + "/hyperload.txt").read(), encoding="utf-8")
        
        if verificationData == resource[0][4]:
            r.verify(resourceId)
            isVerified = True
            
        r.close()
        
        if isVerified:
            return str(1)
        else:
            return str(0)
    
    @cherrypy.expose
    @authorization.isAuthorized
    def getverificationfile(self, resourceId):
        cherrypy.response.headers['Content-Disposition'] = "attachment; filename=hyperload.txt"
        
        r = dal.resource.resource()
        resource = r.get(int(resourceId))
        r.close()
        
        return resource[0][4]
        
    @cherrypy.expose
    @authorization.isAuthorized
    def remove(self, resourceId):
        r = dal.resource.resource()
        r.remove(resourceId)
        r.close()