# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

# class HomePage(Page):
#     body = RichTextField(blank=True, help_text=u'正文信息')
#
#     content_panels = Page.content_panels + [
#         FieldPanel('body', classname="full"),
#     ]
