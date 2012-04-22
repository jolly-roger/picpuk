import psycopg2
import cherrypy


class base(object):
    def __init__(self):
        self.conn = psycopg2.connect(cherrypy.request.app.config["database"]["connection"])
        self.cur = self.conn.cursor()
    
    def close(self):
        self.cur.close()
        self.conn.close()