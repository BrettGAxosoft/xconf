from mezzanine.pages.page_processors import processor_for
from mezzanine.blog.models import BlogPost
from mezzanine.accounts.models import User
from .models import Vote


@processor_for("/")
def statistics(request, page):

    return {
        "statistics": {
            "proposals": BlogPost.objects.all().count(),
            "votes": Vote.objects.all().count(),
            "voters": User.objects.filter(votes__isnull=True).count()
        }
    }
