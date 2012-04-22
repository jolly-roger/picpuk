from . import base

class user(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def add(self, userId):
        self.cur.callproc("adduser", [userId])
        self.conn.commit()