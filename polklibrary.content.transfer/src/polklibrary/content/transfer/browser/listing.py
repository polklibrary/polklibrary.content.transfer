from Products.Five import BrowserView
from zope.component import getMultiAdapter

import json,urllib

class ListingView(BrowserView):

    # http://www.uwosh.edu/library/emc

    data = {}
    
    def __call__(self):
    
        print self.context.absolute_url_path()
        print self.context.getPhysicalPath()
        print self.context.virtual_url_path()
        
       
        return json.dumps(self.data)

        