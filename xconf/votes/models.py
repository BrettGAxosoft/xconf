from django.db import models

from mezzanine.accounts.models import User
from mezzanine.blog.models import BlogPost

class Vote(models.Model):
    user = models.ForeignKey(User)
    talk = models.ForeignKey(BlogPost)