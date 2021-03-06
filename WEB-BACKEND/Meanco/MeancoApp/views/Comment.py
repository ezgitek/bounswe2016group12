"""@package Views
View documentation

"""
from django.shortcuts import render
from sys import platform as _platform
from MeancoApp.models import Topic, Comment, OfTopic, Relation, ViewedTopic,Profile, Tag, FollowedTopic
## Gets Topic Page
#
def get_page(request, id):
    followed = []
    topicId = id
    if request.user.is_authenticated:
        profileId=Profile.objects.get(user_id=request.user.id).id
        if(ViewedTopic.objects.filter(profile_id=profileId,topic_id=topicId).exists()):
            vt=ViewedTopic.objects.get(profile_id=profileId,topic_id=topicId)
            vt.visited()
            vt.save()
        else:
            vt=ViewedTopic(profile_id=profileId,topic_id=topicId)
            vt.save()
        followed = FollowedTopic.objects.filter(profile_id=profileId, topic_id=topicId)
    TrendingTopics=Topic.objects.order_by("-view_count")[:7]
    TrendingTags = Tag.objects.order_by("-topic_count")[:7]
    topic = Topic.objects.get(id=topicId )
    topic.viewed()
    topic.save()
    comments = Comment.objects.filter(topic=topicId)
    oftopic = OfTopic.objects.filter(topic=topicId)

    if _platform=="win32":
        return render(request, 'MeancoApp\CommentList.html', {'topic':topic,'TrendingTopics':TrendingTopics,'TrendingTags':TrendingTags, 'comments':comments, 'oftopic':oftopic, 'followed':followed})
    else:
        return render(request, 'MeancoApp/CommentList.html', {'topic':topic,'TrendingTopics':TrendingTopics,'TrendingTags':TrendingTags, 'comments':comments, 'oftopic':oftopic, 'followed':followed})