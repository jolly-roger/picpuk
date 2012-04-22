import cherrypy

from jinja2 import Environment, FileSystemLoader


env = None


def getenv():
    global env
    
    if env is None:
        env = Environment(loader = FileSystemLoader(cherrypy.request.app.config["hyperload"]["base_dir"] + \
            "layout/templates"))
        
    return env

def getIndex():
    tmpl = getenv().get_template("pages/index.html")
    return tmpl.render()
    
def getLogin():
    tmpl = getenv().get_template("pages/login.html")
    return tmpl.render()
    
def getHome():
    tmpl = getenv().get_template("pages/home.html")
    return tmpl.render()

def getJS():
    tmpl = getenv().get_template("js/common.js")
    return tmpl.render()