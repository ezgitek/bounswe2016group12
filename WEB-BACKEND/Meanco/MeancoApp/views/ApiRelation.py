"""@package API
API documentation

"""
from MeancoApp.models import *
from django.http import request
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
## Adds relation between given 2 topics. API call.
# Example API request:
# topic1 : 1
# topic2 : 2
# label : "asd"
# isBidirectional= 0    //False, 1=True
#
@csrf_exempt
def addRelation(request):
    topicStartPoint=request.POST.get("topic1")
    topicEndPoint = request.POST.get("topic2")
    label = request.POST.get("label")
    isBidirectional =  False
    if(request.POST.get("isBidirectional")=='1'):isBidirectional=True
    try:
        if(Relation.objects.filter(topic_a_id=topicStartPoint,topic_b_id=topicEndPoint,label=label,isBidirectional=isBidirectional).exists()):
            return HttpResponse("Relation Exists",status=400)
        else:
            relation = Relation(topic_a_id=topicStartPoint,topic_b_id=topicEndPoint,label=label,isBidirectional=isBidirectional)
            relation.save()
            if (isBidirectional):
                relation2 = Relation(topic_a_id=topicEndPoint, topic_b_id=topicStartPoint, label=label,isBidirectional=isBidirectional)
                relation2.save()
    except:
        return HttpResponse("Relation Couldn't be created", status=400)
    if(isBidirectional):
        return HttpResponse(json.dumps({
            "relationId": relation.id,
            "secondRelationId":relation2.id}),
            status=200,
            content_type="application/json")
    else:
        return HttpResponse(json.dumps({
            "relationId": relation.id}),
            status=200,
            content_type="application/json")

## Rates given relation.
#   userId : 1
#   relation : 5
#   direction : "upvote"
#
@csrf_exempt
def rateRelation(request):
    relation = request.POST.get("relation")

    if 'userId' not in request.POST:
        userId = request.user.id
    else:
        userId = request.POST.get("userId")
    profileId=Profile.objects.get(user_id=userId).id
    direction= request.POST.get("direction")
    if RelationVoter.objects.filter(relation_id=relation,profile_id=profileId):
        relationVoter=RelationVoter.objects.get(relation_id=relation,profile_id=profileId)
        relationVoter.toggle(direction)
        relationVoter.save()
    else:
        relationVoter=RelationVoter(relation_id=relation,profile_id=profileId)
        relationVoter.toggle(direction)
        relationVoter.save()
    return HttpResponse("Rated",status=200);