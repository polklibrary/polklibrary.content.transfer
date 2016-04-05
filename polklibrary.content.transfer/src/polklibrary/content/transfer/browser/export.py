from Products.Five import BrowserView
from zope.component import getMultiAdapter

import json

class ExportView(BrowserView):

    data = {}


    def __call__(self):
        self.data = {}
    
        context_state = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        canonical_object = context_state.canonical_object()
        
        print '-------------------------'
        print self.context.portal_type
        print canonical_object.portal_type
    
        self._general(canonical_object)
        self._folder(canonical_object)
        self._page(canonical_object)
        self._image(canonical_object)
        self._link(canonical_object)
        
        
        return json.dumps(self.data)

        
    def _general(self, obj):
        self.data['Title'] = self.context.Title
        self.data['Description'] = self.context.Description
        self.data['portal_type'] = self.context.portal_type
        self.data['Creator'] = self.context.Creator
        self.data['location'] = self.context.getLocation()
        
        
    def _folder(self, obj):
        if obj.portal_type != 'Folder':
            return
    
    
    def _page(self, obj):
        if obj.portal_type != 'Document':
            return
    
        self.data['body_raw'] = obj.getRawText()
        self.data['body'] = obj.getText()
        
        
    def _image(self, obj):
        if obj.portal_type != 'Image':
            return
        
    def _link(self, obj):
        if obj.portal_type != 'Link':
            return
            
        self.data['getRemoteUrl'] = obj.getRemoteUrl
        
        
        
        
        
        