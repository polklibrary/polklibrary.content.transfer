from Products.Five import BrowserView
from zope.component import getMultiAdapter

import json,urllib

class ListingView(BrowserView):

    # http://www.uwosh.edu/library/emc

    data = {}
    
    def __call__(self):
        self.data = {
            'urls' : []
        }
        
        start_path = self.context.absolute_url_path()
        brains = self.context.portal_catalog.searchResults(path={'query' : start_path})
        
        for brain in brains:
            self.data['urls'].append( brain.getURL() )
        
        return json.dumps(self.data)

        