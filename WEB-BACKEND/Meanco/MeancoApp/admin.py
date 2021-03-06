from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(profile.Profile)
admin.site.register(profile.FollowedTopic)
admin.site.register(profile.ViewedTopic)
admin.site.register(profile.CommentedTopic)

admin.site.register(topic.Topic)
admin.site.register(topic.TopicRef)

admin.site.register(tag.Tag)
admin.site.register(tag.OfTopic)

admin.site.register(comment.Comment)
admin.site.register(comment.Version)
admin.site.register(comment.Voter)

admin.site.register(relation.Relation)
admin.site.register(relation.RelationVoter)