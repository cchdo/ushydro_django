from django.http import HttpResponseRedirect


def redirect_s4p(request):
    return HttpResponseRedirect('/outreach/content/tagged/S4P')
