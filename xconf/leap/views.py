from django.template import Context

from mezzanine.utils.views import render

from .models import Track


def index(request):
    templates = ["leap/index.html"]
    track1 = Track.objects.get(pk=1)
    track2 = Track.objects.get(pk=2)
    track3 = Track.objects.get(pk=3)
    c = Context({
            'slots': zip(track1.slots.all(), track2.slots.all(), track3.slots.all())
        })
    return render(request, templates, c)
