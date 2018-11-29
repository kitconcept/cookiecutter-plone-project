# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MyViewlet(ViewletBase):
    """ A simple viewlet """
    index = ViewPageTemplateFile('myviewlet.pt')

    def update(self):
        self.news_available = True

    def get_news(self):
        pc = api.portal.get_tool('portal_catalog')

        query = {}
        # if self.filter:
        #     query.update({'Subject': self.filter})

        return pc.searchResults(
                    portal_type=['News Item', ],
                    review_state='published',
                    sort_on='effective',
                    sort_order='reverse',
                    **query)[:6]
