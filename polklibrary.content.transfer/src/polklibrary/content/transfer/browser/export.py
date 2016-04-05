from Products.Five import BrowserView
from zope.component import getMultiAdapter

import json

class ExportView(BrowserView):

    data = {}


    def __call__(self):
        self.data = {}
    
        context_state = getMultiAdapter((context, request), name=u'plone_context_state')
        canonical_object = context_state.canonical_object()
    
    
        self._general()
        self._folder()
        self._page()
        self._image()
        self._link()
        
        
        return json.dumps(self.data)

        
    def _general(self):
        self.data['Title'] = self.context.Title
        self.data['Description'] = self.context.Description
        self.data['portal_type'] = self.context.portal_type
        self.data['Creator'] = self.context.Creator
        self.data['location'] = self.context.getLocation()
        
        
    def _folder(self):
        if self.context.portal_type == 'Folder':
            return
    
    
    def _page(self):
        if self.context.portal_type == 'Document':
            return
    
        self.data['body_raw'] = self.context.getRawText()
        self.data['body'] = self.context.getText()
        
        
    def _image(self):
        if self.context.portal_type == 'Image':
            return
        
    def _link(self):
        if self.context.portal_type == 'Link':
            return
            
        self.data['getRemoteUrl'] = self.context.getRemoteUrl
        
        
        
        
        
        