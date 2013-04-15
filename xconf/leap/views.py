from django.template import Context

from mezzanine.utils.views import render

from .models import Track


def index(request):
    templates = ["leap/index.html"]
    c = Context({
            'tracks': Track.objects.all()
        })
    return render(request, templates, c)
