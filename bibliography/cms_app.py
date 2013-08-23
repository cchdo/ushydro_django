from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class BiblioHook(CMSApp):
    name = _("Bibliography")
    urls = ["bibliography.urls"]

apphook_pool.register(BiblioHook)
