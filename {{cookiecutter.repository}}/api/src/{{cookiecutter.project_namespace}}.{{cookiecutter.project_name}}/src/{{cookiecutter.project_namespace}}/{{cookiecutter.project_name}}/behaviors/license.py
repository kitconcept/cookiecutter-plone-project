# -*- coding: utf-8 -*-
from {{cookiecutter.project_namespace}}.{{cookiecutter.project_name}} import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.interface import provider
from zope.schema import TextLine


@provider(IFormFieldProvider)
class ILicense(model.Schema):

    image_caption = TextLine(
        title=_(u"Legende zum Vorschaubild"),
        description=_(u"Bitte Lizenzinformationen in folgender Form angeben"),
        required=False,
    )
