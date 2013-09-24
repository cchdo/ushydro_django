from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class HydromapPlugin(CMSPluginBase):
    model = CMSPlugin
    name = "Hydromap"
    render_template = "hydromap/index.html"

plugin_pool.register_plugin(HydromapPlugin)
