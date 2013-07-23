from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class HydroTableHook(CMSApp):
    name = _("Hydrotable")
    urls = ["hydrotable.urls"]

apphook_pool.register(HydroTableHook)
