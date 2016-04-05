from Products.Five import BrowserView

import json

class ExportView(BrowserView):

    def __call__(self):
    
        
    
    
        return json.dumps({'test':'status'})
