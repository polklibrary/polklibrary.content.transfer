from Products.Five import BrowserView
from zope.component import getMultiAdapter

import json,urllib

class ExportView(BrowserView):

    data = {}


    def __call__(self):
        self.data = {}
   
        self._general()
        self._folder()
        self._page()
        self._image()
        self._link()
        self._liblink()
        
        return json.dumps(self.data)

        
    def _general(self):
        self.data['Title'] = self.context.Title()
        self.data['Description'] = self.context.Description()
        self.data['portal_type'] = self.context.portal_type
        self.data['Creator'] = self.context.Creator()
        self.data['location'] = self.context.getLocation()
        
        
    def _folder(self):
        if self.context.portal_type != 'Folder':
            return
    
    
    def _page(self):
        if self.context.portal_type != 'Document':
            return
    
        self.data['body_raw'] = urllib.quote(self.context.getRawText())
        self.data['body'] = urllib.quote(self.context.getText())
        
        
    def _image(self):
        if self.context.portal_type != 'Image':
            return
        
    def _liblink(self):
        if self.context.portal_type != 'LibraryLink':
            return
            
        self.data['getRemoteUrl'] = self.context.getRemoteUrl()
        
        
    def _link(self):
        if self.context.portal_type != 'Link':
            return
            
        self.data['getRemoteUrl'] = self.context.getRemoteUrl()
        
        
        
        
        
        