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
        data['Title'] = self.context.Title
        data['Description'] = self.context.Description
        data['portal_type'] = self.context.portal_type
        data['Creator'] = self.context.Creator
        data['location'] = self.context.location
        data['getRemoteUrl'] = self.context.getRemoteUrl
        
        
    def _folder(self):
        if context.portal_type == 'Folder':
            return
    
    
    def _page(self):
        if context.portal_type == 'Document':
            return
    
        data['body_raw'] = self.context.getRawText()
        data['body'] = self.context.getText()
        
        
    def _image(self):
        if context.portal_type == 'Image':
            return
        
        
        
        
        
        
        
        
        