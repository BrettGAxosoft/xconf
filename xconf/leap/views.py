from django.template import Context

from mezzanine.utils.views import render


def index(request):
    templates = ["leap/index.html"]
    c = Context()
    return render(request, templates, c)
