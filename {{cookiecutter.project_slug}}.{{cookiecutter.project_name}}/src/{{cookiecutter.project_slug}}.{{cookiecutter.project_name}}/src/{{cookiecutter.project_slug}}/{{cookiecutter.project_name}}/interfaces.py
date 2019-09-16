# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model

# from {{cookiecutter.project_slug}}.{{cookiecutter.project_name}} import _
# from zope import schema
# from plone.app.textfield import RichText
# from z3c.relationfield.schema import RelationChoice
# from z3c.relationfield.schema import RelationList
# from plone.directives import form
# from plone.autoform import directives
# from plone.namedfile.field import NamedBlobImage
# from plone.namedfile import field as namedfile


class I{{cookiecutter.project_slug.capitalize()}}{{cookiecutter.project_name}}Layer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IHomepage(model.Schema):
    """ Homepage content type interface
    """
