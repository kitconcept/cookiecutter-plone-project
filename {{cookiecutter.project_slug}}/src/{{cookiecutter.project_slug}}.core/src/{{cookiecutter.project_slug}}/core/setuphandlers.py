# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from DateTime import DateTime
from plone import api
from plone.app.event.dx.behaviors import IEventBasic
from plone.app.portlets.utils import assignment_mapping_from_key
from plone.app.textfield.value import RichTextValue
from plone.namedfile.file import NamedBlobImage
from plone.portlets.constants import CONTEXT_CATEGORY
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.component import queryUtility
from zope.component.interfaces import IFactory
from zope.container.interfaces import INameChooser
from zope.interface import implementer
from zope.interface import alsoProvides
from plone.dexterity.utils import createContentInContainer

import os
import pytz


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            '{{cookiecutter.project_slug}}.core:uninstall',
        ]


def create_content(portal, content):
    for obj in content:
        if obj.get('path') is None:
            # TODO: handle
            pass
        try:
            relative_path = obj.get('path').rstrip('/')
            relative_path = relative_path.split('/')[1:]
            container = portal.restrictedTraverse(relative_path)
        except:  # noqa
            # TODO: handle
            pass

        new = api.content.create(
            type=obj.get('type'),
            id=obj.get('id'),
            title=obj.get('title'),
            description=obj.get('description'),
            container=container,
        )
        try:
            api.content.transition(
                obj=new,
                to_state='published'
            )
        except WorkflowException:
            # TODO: handle
            pass

        # set workflow state (publish by default)
        # workflowTool = getToolByName(portal, "portal_workflow")
        # if workflowTool.getStatusOf("plone_workflow", obj):
        #     if not obj.get('workflow_state'):
        #         workflow_state = 'published'
        #     try:
        #         api.content.transition(
        #             obj=new,
        #             to_state=workflow_state
        #         )
        #     except WorkflowException:
        #         # TODO: handle
        #         import pdb; pdb.set_trace()
        #         pass

        new.text = RichTextValue(
            obj.get('text'),
            'text/html',
            'text/html'
        )
        new.effective_date = DateTime()
        new.image = obj.get('image')

        if obj.get('header_image'):
            new.header_image = obj.get('header_image')

        if obj.get('header_caption'):
            new.header_caption = obj.get('header_caption')

        if obj.get('header_caption_en'):
            new.header_caption_en = obj.get('header_caption_en')

        # collection
        from plone.app.contenttypes.behaviors.collection import ICollection as ICollection_behavior  # noqa
        if obj.get('type') == 'Collection' and obj.get('query'):
            wrapped = ICollection_behavior(new)
            wrapped.query = obj.get('query')

        if obj.get('title_en'):
            new.title_en = obj.get('title_en')
        if obj.get('description_en'):
            new.description_en = obj.get('description_en')

        # Pressemitteilung
        if obj.get('type') == 'Pressemitteilung':
            new.headertitel = obj.get('headertitel')
            new.headertitel_en = obj.get('headertitel_en')
            new.headerbeschreibung = obj.get('headerbeschreibung')
            new.headerbeschreibung_en = obj.get('headerbeschreibung_en')
            new.abbinder = RichTextValue(
                obj.get('abbinder'),
                'text/html',
                'text/html'
            )
            new.abbinder_en = RichTextValue(
                obj.get('abbinder_en'),
                'text/html',
                'text/html'
            )

        # leadimage behavior
        if obj.get('image_caption'):
            new.image_caption = obj.get('image_caption')

        # plone form gen
        if obj.get('type') == 'FormSelectionField' and obj.get('fgVocabulary'):
            new.fgVocabulary = obj.get('fgVocabulary')

        if obj.get('type') == 'FormMultiSelectionField' and obj.get('fgVocabulary'):  # noqa
            new.fgVocabulary = obj.get('fgVocabulary')

        # exclude from navigation
        if obj.get('exclude_from_nav'):
            new.exclude_from_nav = obj.get('exclude_from_nav')

        # set layout
        if obj.get('layout'):
            new.setLayout(obj.get('layout'))

        # set uid
        if obj.get('uid'):
            setattr(new, '_plone.uuid', obj.get('uid'))
            new.reindexObject(idxs=['UID'])

        # set call_to_action
        if obj.get('call_to_action'):
            new.call_to_action = obj.get('call_to_action')

        # reindex object
        new.reindexObject()


def change_content_type_title(portal, old_name, new_name):
    portal_types = getToolByName(portal, 'portal_types')
    news_item_fti = getattr(portal_types, old_name)
    news_item_fti.title = new_name


def disable_content_type(portal, fti_id):
    portal_types = getToolByName(portal, 'portal_types')
    document_fti = getattr(portal_types, fti_id)
    document_fti.global_allow = False


def copy_content_type(portal, name, newid, newname):
    """Create a new content type by copying an existing one
    """
    portal_types = getToolByName(portal, 'portal_types')
    tmp_obj = portal_types.manage_copyObjects([name])
    tmp_obj = portal_types.manage_pasteObjects(tmp_obj)
    tmp_id = tmp_obj[0]['new_id']
    new_type_fti = getattr(portal_types, tmp_id)
    new_type_fti.title = newname
    portal_types.manage_renameObjects([tmp_id], [newid])


def post_install(context):
    """Post install script"""

    portal = api.portal.get()

    # Rename 'News Item' -> 'Aktuelles'
    # change_content_type_title(portal, 'News Item', 'Meldung')

    # indexes (dropdown navigation / leadimage)
    # wanted_indexes = (
    #     ('exclude_from_nav', 'BooleanIndex'),
    # )
    # add_catalog_indexes(context, wanted=wanted_indexes)

    # Remove front-page from nav
    if 'front-page' in portal:
        portal['front-page'].exclude_from_nav = True
        portal['front-page'].reindexObject()


def import_content(context):
    """Import example content"""

    portal = api.portal.get()

    # run only on fresh portals
    if 'news' in portal.objectIds():
        return

    # users

    api.user.create(
        email='stollenwerk@kitconcept.com',
        username='timo',
        password='welcome',
        roles=('Manager', ),
        properties=None
    )

    users = []
    for user in users:
        api.user.create(
            email='no-reply@example.com',
            username=user,
            password='welcome',
            roles=('Site Administrator', ),
            properties=None
        )

    # content

    content = [
        # /beispiele
        {
            'type': 'Folder',
            'title': 'Beispiele',
            'path': '/',
            'exclude_from_nav': True
        },
    ]

    create_content(portal, content)

    # Portlets at Vereinigung
    # setupPortletAt(portal, 'portlets.Events', 'plone.rightcolumn', '/vereinigungen/fachliche-vereinigungen/sektion-kondensierte-materie/halbleiterphysik') # noqa
    # setupPortletAt(portal, 'portlets.Events', 'plone.rightcolumn', '/vereinigungen/fachliche-vereinigungen/fachliche-vereinigungen/sektion-materie-und-kosmos/gravitation-und-relativitaetstheorie') # noqa
    # setupNavigationPortlet(portal['vereinigungen']['fachliche-vereinigungen']['sektion-materie-und-kosmos']['gravitation-und-relativitaetstheorie']) # noqa

    # Delete Plone content

    if 'Members' in portal.objectIds():
        api.content.delete(obj=portal['Members'])
    if 'news' in portal.objectIds():
        api.content.delete(obj=portal['news'])
    if 'events' in portal.objectIds():
        api.content.delete(obj=portal['events'])
    # if 'front-page' in portal.objectIds():
    #     api.content.delete(obj=portal['front-page'])

    setupNavigationPortlet(portal['beispiele']['seite'])

    # Set permissions for Intranet folder
    # portal['interner-bereich'].manage_setLocalRoles('Authenticated Users', ['Reader', ]) # noqa


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def add_catalog_indexes(context, wanted=None):
    """Method to add our wanted indexes to the portal_catalog.
    """
    catalog = api.portal.get_tool('portal_catalog')
    indexes = catalog.indexes()
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
    if len(indexables) > 0:
        catalog.manage_reindexIndex(ids=indexables)


def setupNavigationPortlet(context, name="", root=None, includeTop=False,
                           currentFolderOnly=False, bottomLevel=0, topLevel=0):
    from plone.app.portlets.portlets.navigation import Assignment as NavAssignment  # noqa
    target_manager = queryUtility(
        IPortletManager, name='plone.leftcolumn', context=context)
    target_manager_assignments = getMultiAdapter(
        (context, target_manager), IPortletAssignmentMapping)

    navtree = NavAssignment(
        includeTop=includeTop,
        currentFolderOnly=currentFolderOnly,
        bottomLevel=bottomLevel,
        topLevel=topLevel)

    if 'navigation' not in target_manager_assignments.keys():
        target_manager_assignments['navigation'] = navtree


def setupPortletAt(portal, portlet_type, manager, path, name="", **kw):
    portlet_factory = getUtility(IFactory, name=portlet_type)
    assignment = portlet_factory(**kw)
    mapping = assignment_mapping_from_key(
        portal, manager, CONTEXT_CATEGORY, path, create=True)

    if not name:
        chooser = INameChooser(mapping)
        name = chooser.chooseName(None, assignment)

    mapping[name] = assignment
