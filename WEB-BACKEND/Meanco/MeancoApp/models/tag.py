from django.db.models import Model, IntegerField, ForeignKey, CharField, URLField, CASCADE, PROTECT, SET_NULL
from django.db.models.signals import post_init, pre_delete
from django.contrib.auth.models import User

from .profile import Profile
from .topic import Topic

### tag.Tag

class Tag(Model):
    label = CharField(max_length=20)
    context = CharField(max_length=20)
    url = URLField()

    view_count = IntegerField(default=0)
    topic_count = IntegerField(default=0)

    def viewed(self):
        self.view_count.value += 1
        self.save()

    def topic_tagged(self):
        self.topic_count.value += 1
        self.save()

    def topic_tag_removed(self):
        self.topic_count.value -= 1
        self.save()

    class Meta:
        unique_together = (('url', ), ('label', 'context'))

### tag.OfTopic

class OfTopic(Model):
    topic = ForeignKey(Topic, on_delete=CASCADE, related_name='tags')
    tag = ForeignKey(Tag, on_delete=PROTECT, related_name='topics')
    profile = ForeignKey(Profile, on_delete=SET_NULL, null=True, related_name='topictags')

    class Meta:
        unique_together = ('topic', 'tag')

def oftopic_post_init(**kwargs):
    oftopic = kwargs.get('instance')
    
    oftopic.topic.name().vote(oftopic.profile, skipifhasvoted=True)
    oftopic.tag.topic_tagged()

def oftopic_pre_delete(**kwargs):
    oftopic = kwargs.get('instance')
    
    oftopic.tag.topic_tag_removed()

post_init.connect(oftopic_post_init, OfTopic)
pre_delete.connect(oftopic_pre_delete, OfTopic)