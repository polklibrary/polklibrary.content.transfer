from Products.Five import BrowserView
from zope.component import getMultiAdapter

import json,urllib

class ProcessView(BrowserView):

    data = {}
    
    def __call__(self):
        url = self.request.params.get('url','')
       
        if url:
            u = urllib.urlopen(url + '/listing_content')
            listing = json.loads(response.read())
            
            print listing
       
       
       
       
        return json.dumps(self.data)

        