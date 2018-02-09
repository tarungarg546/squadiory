from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from .models import Voting,Satisfaction,Question,Meetings
from django.utils import timezone


def upvote(request,user_id,question_id):
    if request.user.is_authenticated():
        if request.method == "POST":
            meeting = Question.objects.filter(id=question_id).values_list('meeting_id')
            meets_end_time = Meetings.objects.filter(id=meeting).values_list('end_time')

            if meets_end_time < timezone.now():
                votes = Voting.objects.filter(user_id=user_id,question_id=question_id)
                count = votes.len()
                if count <1:
                    Voting.objects.create(user_id=user_id,question_id=question_id,vote=1)
                    return HttpResponse('Upvoted')
                elif count==1:
                    if votes.vote == 1:
                        return HttpResponse('Already Upvoted')
                    else:
                        votes.vote = 2
                        votes.save()
                        return HttpResponse('Vote Changed')
        return HttpResponseBadRequest()
    return HttpResponseForbidden()


def downvote(request,user_id,question_id):
    if request.user.is_authenticated():
        if request.method == "POST":
            meeting = Question.objects.filter(id=question_id).values_list('meeting_id')
            meets_end_time = Meetings.objects.filter(id=meeting).values_list('end_time')
            if meets_end_time < timezone.now():
                votes = Voting.objects.filter(user_id=user_id, question_id=question_id)
                count = votes.len()
                if count < 1:
                    Voting.objects.create(user_id=user_id, question_id=question_id, vote=1)
                    return HttpResponse('Downvoted')
                elif count == 1:
                    if votes.vote == 2:
                        return HttpResponse('Already Downvoted')
                    else:
                        votes.vote = 1
                        votes.save()
                        return HttpResponse('Vote Changed')
        return HttpResponseBadRequest()
    return HttpResponseForbidden()


def satisfied(request,user_id,question_id):
    if request.user.is_authenticated():
        if request.method == "POST":
            meeting = Question.objects.filter(id=question_id).values_list('meeting_id')
            meets_end_time = Meetings.objects.filter(id=meeting).values_list('end_time')
            if meets_end_time > timezone.now():
                satisfaction = Satisfaction.objects.filter(user_id=user_id, question_id=question_id)
                count = satisfaction.len()
                if count < 1:
                    Satisfaction.objects.create(user_id=user_id, question_id=question_id, satisf_status=1)
                    return HttpResponse('Feedback recorded')
                elif count == 1:
                    if satisfaction.satisf_status == 1:
                        return HttpResponse('Feedback Already Recorded')
                    else:
                        satisfaction.satisf_status = 2
                        satisfaction.save()
                        return HttpResponse('Feedback Changed')
        return HttpResponseBadRequest()
    return HttpResponseForbidden()

def disatisfied(request,user_id,question_id):
    if request.user.is_authenticated():
        if request.method == "POST":
            meeting = Question.objects.filter(id=question_id).values_list('meeting_id')
            meets_end_time = Meetings.objects.filter(id=meeting).values_list('end_time')
            if meets_end_time > timezone.now():
                satisfaction = Satisfaction.objects.filter(user_id=user_id, question_id=question_id)
                count = satisfaction.len()
                if count < 1:
                    Satisfaction.objects.create(user_id=user_id, question_id=question_id, satisf_status=1)
                    return HttpResponse('Feedback recorded')
                elif count == 1:
                    if satisfaction.satisf_status == 2:
                        return HttpResponse('Feedback Already Recorded')
                    else:
                        satisfaction.satisf_status = 1
                        satisfaction.save()
                        return HttpResponse('Feedback Changed')
        return HttpResponseBadRequest()
    return HttpResponseForbidden()
