importwebapp2
import os
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), "index.html")
        context = {}
        self.response.out.write(template.render(path, context))
        
        def post(self):
            pincode=self.request.get()