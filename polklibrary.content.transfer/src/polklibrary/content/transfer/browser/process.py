from Products.Five import BrowserView
from zope.component import getMultiAdapter

import json,urllib

class ProcessView(BrowserView):

    data = {}
    
    def __call__(self):
       
        return json.dumps(self.data)

        