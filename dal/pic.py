from . import base

import cherrypy


class pic(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def add(self, userId):
        self.cur.callproc("addpic", [userId])
        self.conn.commit()
        result = self.cur.fetchall()
        
        return result[0][0]
        
    def getLast(self, count):
        self.cur.callproc("getlastpics", [count])
        return self.cur.fetchall()
        
    def getUserPics(self):
        self.cur.callproc("getuserpics", [userId])
        self.conn.commit()
        return self.cur.fetchall()