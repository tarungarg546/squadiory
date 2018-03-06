from django.http import HttpResponse
from .models import Voting,Meetings,Satisfaction
from datetime import datetime


def upvote(request,user_id,question_id):
    if request.method == "POST":
        meeting = Meetings.objects.filter(question_id=question_id)
        if meeting.end_time < datetime.now():
            if Voting.objects.filter(user_id=user_id,question_id=question_id).count()<1:
                Voting.objects.create(user_id=user_id,question_id=question_id,vote=1)
                return HttpResponse('Upvoted')
            else:
                return HttpResponse('Already Voted')


def downvote(request,user_id,question_id):
    if request.method == "POST":
        meeting = Meetings.objects.filter(question_id=question_id)
        if meeting.end_time < datetime.now():
            if Voting.objects.filter(user_id=user_id,question_id=question_id).count()<1:
                Voting.objects.create(user_id=user_id,question_id=question_id,vote=2)
                return HttpResponse('Downvoted')
            else:
                return HttpResponse('Already Voted')


def satisfied(request,user_id,question_id):
    if request.method == "POST":
        meeting = Meetings.objects.filter(question_id=question_id)
        if meeting.end_time > datetime.now():
            if Satisfaction.objects.filter(user_id=user_id,question_id=question_id).count()<1:
                Satisfaction.objects.create(user_id=user_id, question_id=question_id, satisf_status=1)
                return HttpResponse('Feedback Noted')
            else:
                return HttpResponse('User has already given Feedback')


def disatisfied(request,user_id,question_id):
    if request.method == "POST":
        meeting = Meetings.objects.filter(question_id=question_id)
        if meeting.end_time > datetime.now():
            if Satisfaction.objects.filter(user_id=user_id,question_id=question_id).count()<1:
                Satisfaction.objects.create(user_id=user_id, question_id=question_id, satisf_status=2)
                return HttpResponse('Feedback Noted')
            else:
                return HttpResponse('User has already given Feedback')
