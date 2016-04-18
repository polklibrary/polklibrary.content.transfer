from Products.Five import BrowserView
from zope.component import getMultiAdapter
from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides

import json,urllib,ast

class ProcessView(BrowserView):

    data = {}
    
    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        
        url = self.request.form.get('url','')
       
        if url:
            response = urllib.urlopen(url + '/export_content_list')
            listing = ast.literal_eval(response.read())
            d = ast.literal_eval(listing)
            
            for u in d['urls']:
                response = urllib.urlopen(u + '/export_content_metadata')
                d = ast.literal_eval(response.read())
                self.process_meta(d)
       
       
        return json.dumps(self.data)

        
    def process_meta(self, meta):
    
        print "CREATE....."
        print "Title: " + meta['Title']
        print "Desc: " + meta['Description']
        print "portal_type: " + meta['portal_type']
        
        parent = meta['parent'] #.replace('/library/','/')
        print "parent: " + parent
        
        if meta['portal_type'] == 'LibraryLink' or meta['portal_type'] == 'Link' :
            obj = api.content.create(
                container = api.content.get(path=parent),
                type = 'Link',
                id = meta['id'],
                title = meta['Title'])
            obj.description = meta['Description']
            obj.remoteUrl = meta['getRemoteUrl']
        else:
            obj = api.content.create(
                container = api.content.get(path=parent),
                type = meta['portal_type'],
                id = meta['id'],
                title = meta['Title'])
            obj.description = meta['Description']
            obj.location = meta['location']
            
            
            