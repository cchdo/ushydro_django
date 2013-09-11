from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class BibliographyPlugin(CMSPluginBase):
    model = CMSPlugin
    name = "Bibliography"
    render_template = "bibliography/index.html"

plugin_pool.register_plugin(BibliographyPlugin)
