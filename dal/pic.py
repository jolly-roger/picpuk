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
        self.cur.execute("select id_pic from pic order by id_pic desc limit %s;", (count,))
        return self.cur.fetchall()