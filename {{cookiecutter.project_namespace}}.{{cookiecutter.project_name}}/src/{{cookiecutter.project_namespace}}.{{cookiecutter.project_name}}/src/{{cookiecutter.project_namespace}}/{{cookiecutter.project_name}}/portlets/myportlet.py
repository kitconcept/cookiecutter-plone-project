# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.app.layout.navigation.root import getNavigationRootObject
from plone.app.portlets.cache import render_cachekey
from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.portlets import base
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform.directives import widget
from plone.memoize.compress import xhtml_compress
from plone.memoize import ram
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import ISiteSchema
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope import schema
from zope.interface import implementer


class IMyPortlet(IPortletDataProvider):

    count = schema.Int(
        title=_(u"Number of items to display"),
        description=_(u"How many items to list."),
        required=True,
        default=5,
        min=1,
    )

    widget(state=SelectFieldWidget)
    state = schema.Tuple(
        title=_(u"Workflow state"),
        description=_(u"Items in which workflow state to show."),
        default=("published",),
        required=True,
        value_type=schema.Choice(vocabulary="plone.app.vocabularies.WorkflowStates"),
    )

    thumb_scale = schema.TextLine(
        title=_(u"Override thumb scale"),
        description=_(
            u"Enter a valid scale name"
            u" (see 'Image Handling' control panel) to override"
            u" (e.g. icon, tile, thumb, mini, preview, ... )."
            u" Leave empty to use default (see 'Site' control panel)."
        ),
        required=False,
        default=u"",
    )

    no_thumbs = schema.Bool(
        title=_(u"Suppress thumbs"),
        description=_(u"If enabled, the portlet will not show thumbs"),
        required=True,
        default=False,
    )


@implementer(IMyPortlet)
class Assignment(base.Assignment):

    thumb_scale = None
    no_thumbs = False

    def __init__(
        self, count=5, state=("published",), thumb_scale=None, no_thumbs=False
    ):
        self.count = count
        self.state = state
        self.thumb_scale = thumb_scale
        self.no_thumbs = no_thumbs

    @property
    def title(self):
        return _(u"MyPortlet")


class Renderer(base.Renderer):

    _template = ViewPageTemplateFile("myportlet.pt")

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    @ram.cache(render_cachekey)
    def render(self):
        return xhtml_compress(self._template())

    @property
    def available(self):
        return self.data.count > 0 and len(self._data())

    def published_news_items(self):
        return self._data()

    def all_news_link(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter(
            (context, self.request), name="plone_portal_state"
        )
        portal = portal_state.portal()
        if "news" in getNavigationRootObject(context, portal).objectIds():
            return "%s/news" % portal_state.navigation_root_url()
        return None

    @memoize
    def _data(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, "portal_catalog")
        portal_state = getMultiAdapter(
            (context, self.request), name="plone_portal_state"
        )
        path = portal_state.navigation_root_path()
        limit = self.data.count
        state = self.data.state
        return catalog(
            portal_type="Events",
            review_state=state,
            path=path,
            sort_on="effective",
            sort_order="reverse",
            sort_limit=limit,
        )[:limit]

    def thumb_scale(self):
        """Use override value or read thumb_scale from registry.
        Image sizes must fit to value in allowed image sizes.
        None will suppress thumb.
        """
        if getattr(self.data, "no_thumbs", False):
            # Individual setting overrides ...
            return None
        thsize = getattr(self.data, "thumb_scale", "")
        if thsize:
            return thsize
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ISiteSchema, prefix="plone", check=False)
        if settings.no_thumbs_portlet:
            return None
        thumb_scale_portlet = settings.thumb_scale_portlet
        return thumb_scale_portlet


class AddForm(base.AddForm):
    schema = IMyPortlet
    label = _(u"Add 'MyPortlet' Portlet")
    description = _(u"This portlet displays recent News Items.")

    def create(self, data):
        return Assignment(
            count=data.get("count", 5), state=data.get("state", ("published",))
        )


class EditForm(base.EditForm):
    schema = IMyPortlet
    label = _(u"Edit 'MyPortlet' Portlet")
    description = _(u"This portlet displays recent News Items.")
