from django.shortcuts import render
from sys import platform as _platform
from MeancoApp.models import *

def get_page(request):

    id = request.user.id
    if Profile.objects.filter(user_id=id).exists():
        profileId = Profile.objects.get(user_id=id).id
        followed = FollowedTopic.objects.filter(profile_id=profileId)
        commented = CommentedTopic.objects.filter(profile_id=profileId)
        viewed = ViewedTopic.objects.filter(profile_id=profileId)
        TrendingTopics=Topic.objects.order_by("-view_count")[:7]
        TrendingTags = Tag.objects.order_by("-topic_count")[:7]
        comments = Comment.objects.filter(profile_id=profileId)
        if _platform == "win32":
            return render(request, 'MeancoApp\Profile.html', {'followed': followed,'TrendingTopics':TrendingTopics,'TrendingTags':TrendingTags, 'commented':commented, 'viewed':viewed, 'comments':comments})
        else:
            return render(request, 'MeancoApp/Profile.html', {'followed': followed,'TrendingTopics':TrendingTopics,'TrendingTags':TrendingTags, 'commented':commented, 'viewed':viewed, 'comments':comments})
    else :
        if _platform == "win32":
            return render(request, 'MeancoApp\Home.html')
        else:
            return render(request, 'MeancoApp/Home.html')