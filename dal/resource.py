from . import base

import cherrypy


class resource(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def add(self, alias, domain, outerUserId):
        self.cur.callproc("addresource", [alias, domain, outerUserId])
        self.conn.commit()
        result = self.cur.fetchall()
        
        return result[0][0]
        
    def getuserall(self, outerUserId):
        self.cur.callproc("getresources", [outerUserId])
        
        return self.cur.fetchall()
        
    def get(self, resourceId):
        self.cur.callproc("getresource", [resourceId])
        
        return self.cur.fetchall()
        
    def remove(self, resourceId):
        self.cur.callproc("removeresource", [resourceId])
        self.conn.commit()
        
    def verify(self, resourceId):
        self.cur.callproc("verifyresource", [resourceId])
        self.conn.commit()