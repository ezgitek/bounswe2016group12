"""@package Views
View documentation

"""
from django.shortcuts import render
from sys import platform as _platform
from MeancoApp.functions.relation import *
from MeancoApp.models import *
from .forms import UserCreateForm

## Gets Home view with topic map.
#
def get_page(request):
    topics = Topic.objects.all()
    id = request.user.id

    CommentedTopics=()
    ViewedTopics=()
    TrendingTopics=Topic.objects.order_by("-view_count")[:7]
    TrendingTags = Tag.objects.order_by("-topic_count")[:7]
    Relations=getRelations(1)
    if request.user.is_authenticated:
        profileId = Profile.objects.get(user_id=id).id
        FollowedTopics = FollowedTopic.objects.filter(profile_id=profileId)
        CommentedTopics = CommentedTopic.objects.filter(profile_id=profileId)
        ViewedTopics = ViewedTopic.objects.filter(profile_id=profileId)

    FollowedTopics = []
    if request.user.is_authenticated:
        profileId = Profile.objects.get(user_id=request.user.id).id
        fTopics = FollowedTopic.objects.filter(profile_id=profileId)
        for ft in fTopics:
            FollowedTopics.append(ft.topic)

    if _platform == "win32":
        return render(request, 'MeancoApp\TopicMap.html' , {'topics': topics,'Relations':Relations,'TrendingTopics':TrendingTopics,'TrendingTags':TrendingTags,'FollowedTopics':FollowedTopics,'CommentedTopics':CommentedTopics,'ViewedTopics':ViewedTopics, 'id': id})
    else:
        return render(request, 'MeancoApp/TopicMap.html', {'topics': topics,'Relations':Relations,'TrendingTopics':TrendingTopics,'TrendingTags':TrendingTags,'FollowedTopics':FollowedTopics,'CommentedTopics':CommentedTopics,'ViewedTopics':ViewedTopics, 'id': id})
## Gets Sign up page.
#
def get_signup_page(request):
    form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})