from Products.Five import BrowserView

import json

class ExportView(BrowserView):

    data = {}


    def __call__(self):
        self.data = {}
    
        self._general()
        self._folder()
        self._page()
        self._image()
        
        
        return json.dumps(self.data)

        
    def _general(self):
        self.data['Title'] = self.context.Title
        self.data['Description'] = self.context.Description
        self.data['portal_type'] = self.context.portal_type
        self.data['Creator'] = self.context.Creator
        self.data['location'] = self.context.getLocation()
        self.data['getRemoteUrl'] = self.context.getRemoteUrl
        
        
    def _folder(self):
        if context.portal_type == 'Folder':
            return
    
    
    def _page(self):
        if context.portal_type == 'Document':
            return
    
        self.data['body_raw'] = self.context.getRawText()
        self.data['body'] = self.context.getText()
        
        
    def _image(self):
        if context.portal_type == 'Image':
            return
        
        
        
        
        
        
        
        
        