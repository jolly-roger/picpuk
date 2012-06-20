import os
import cherrypy


class largeFileUpload(object):
    @cherrypy.expose
    def index(self):
        return """
        <html><body>
            <h2>Upload a file</h2>
            <form action="upload" method="post" enctype="multipart/form-data">
            filename: <input type="file" name="sourceData" /><br />
            <input type="submit" />
            </form>
            <h2>Download a file</h2>
            <a href='download'>This one</a>
        </body></html>
        """
    
    @cherrypy.expose
    def upload(self, sourceData):
        cherrypy.response.timeout = 3600
        
        out = """<html>
        <body>
            myFile length: %s<br />
            myFile filename: %s<br />
            myFile mime-type: %s
        </body>
        </html>"""

        # Although this just counts the file length, it demonstrates
        # how to read large files in chunks instead of all at once.
        # CherryPy reads the uploaded file into a temporary file;
        # myFile.file.read reads from that.
        size = 0
        while True:
            data = sourceData.file.read(8192)
            if not data:
                break
            size += len(data)

        return out % (size, sourceData.filename, sourceData.content_type)