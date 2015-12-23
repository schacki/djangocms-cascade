# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import widgets
from django.forms.models import ModelForm
from django.utils.translation import ungettext_lazy, ugettext_lazy as _
from django.utils.text import Truncator
from django.utils.html import format_html
from django.forms.fields import IntegerField
from cms.plugin_pool import plugin_pool
from cmsplugin_cascade.forms import ManageChildrenFormMixin
from cmsplugin_cascade.fields import PartialFormField
from cmsplugin_cascade.widgets import NumberInputWidget
from cmsplugin_cascade.plugin_base import CascadePluginBase


class TabForm(ManageChildrenFormMixin, ModelForm):
    num_children = IntegerField(min_value=1, initial=1,
        widget=NumberInputWidget(attrs={'size': '3', 'style': 'width: 5em;'}),
        label=_("Tabs"),
        help_text=_("Number of tabs."))


class TabsPlugin(CascadePluginBase):
    name = _("Tabs")
    form = TabForm
    render_template = 'cascade/bootstrap3/tabs.html'
    parent_classes = ('BootstrapRowPlugin', 'BootstrapColumnPlugin',)
    require_parent = True
    allow_children = True

    @classmethod
    def get_identifier(cls, instance):
        identifier = super(TabsPlugin, cls).get_identifier(instance)
        num_cols = instance.get_children().count()
        content = ungettext_lazy('with {} tab', 'with {} tabs', num_cols).format(num_cols)
        return format_html('{0}{1}', identifier, content)

    def render(self, context, instance, placeholder):
        super(TabsPlugin, self).render(context, instance, placeholder)
        num_children = instance.get_children().count()
        if num_children > 0:
            context['step_css_width'] = '{:3.2f}%'.format(100. / num_children)
        return context

    def save_model(self, request, obj, form, change):
        wanted_children = int(form.cleaned_data.get('num_children'))
        super(TabsPlugin, self).save_model(request, obj, form, change)
        self.extend_children(obj, wanted_children, TabPanelPlugin)

plugin_pool.register_plugin(TabsPlugin)



class TabPanelPlugin(CascadePluginBase):
    name = _("Tab Panel")
    parent_classes = ('TabsPlugin',)
    require_parent = True
    allow_children = True
    alien_child_classes = True
    render_template = 'cascade/bootstrap3/tab_panel.html'
    glossary_fields = (
        PartialFormField('panel_title',
            widgets.TextInput(attrs={'size': 150}),
            label=_("Panel Title")
        ),
    )

    @classmethod
    def get_identifier(cls, obj):
        identifier = super(TabPanelPlugin, cls).get_identifier(obj)
        content = obj.glossary.get('panel_title', '')
        if content:
            content = unicode(Truncator(content).words(3, truncate=' ...'))
        return format_html('{0}{1}', identifier, content)

plugin_pool.register_plugin(TabPanelPlugin)