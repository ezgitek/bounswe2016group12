from django.db.models import Model, CASCADE, OneToOneField
from django.contrib.auth.models import User

### profile.Profile

class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)

    def __unicode__(self):
        return str(self.pk)

    def __str__(self):
        return str(self.pk)
