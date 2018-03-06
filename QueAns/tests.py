from datetime import timezone, timedelta
from unittest import TestCase

from QueAns.views import upvote, downvote, satisfied, disatisfied
from .models import Meetings,Question
from django.contrib.auth.models import User


def create_Meeting(meeting_text,venue,moderator,start_time,end_time):
    return Meetings.objects.create(meeting_text,venue,moderator,start_time,end_time)

def create_Question(question_text,meeting_id,asker,anon_status):
    return Question.objects.create(question_text,meeting_id,asker,anon_status)

def create_User(username,password):
    user = User.objects.create_user(username,password)
    user.is_staff = True
    return user

u1 = create_User('dummy','dummy')
u2 = create_User('dummy2','dummy2')
m1 = create_Meeting('dummy','homer','dummy',timezone.now(),timezone.now()+timedelta(days=1))
m2 = create_Meeting('dummy2','homer','dummy',timezone.now()-timedelta(days=1),timezone.now())
q1 = create_Question('dummyQ',m1.id,'dummy','no')
q2 = create_Question('dummyQ',m2.id,'dummy','yes')

class upvote_test(TestCase):
    def new_vote(self):
        response = upvote(u1.id,q1.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Upvoted')

    def re_vote(self):
        response = upvote(u1.id,q1.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Already Upvoted')

    def voting_closed_question(self):
        response = upvote(u1.id,q2.id)
        self.assertEqual(response.status_code, 400)

    def change_vote(self):
        response = downvote(u1.id,q1.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Vote Changed')

    def dummy_values(self):
        response = upvote(-1,q1.id)
        self.assertEqual(response.status_code, 403)

        response = upvote(u1.id,-1)
        self.assertEqual(response.status_code, 403)


class downvote_test(TestCase):
    def new_vote(self):
        response = downvote(u2.id, q1.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Downvoted')

    def re_vote(self):
        response = downvote(u2.id, q1.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Already Downvoted')

    def voting_closed_question(self):
        response = upvote(u2.id,q2.id)
        self.assertEqual(response.status_code, 400)

    def change_vote(self):
        response = upvote(u2.id, q1.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Voting Changed')

    def dummy_values(self):
        response = downvote(-1, q1.id)
        self.assertEqual(response.status_code, 403)

        response = downvote(u1.id, -1)
        self.assertEqual(response.status_code, 403)


class satisfaction_test(TestCase):
    def new_feedback(self):
        response = satisfied(u1.id, q2.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Feedback Recorded')

    def again_feedback(self):
        response = satisfied(u1.id, q2.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Feedback Already Recorded')

    def change_feedback(self):
        response = disatisfied(u1.id, q2.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Feedback Changed')

    def feedback_active_question(self):
        response = satisfied(u1.id,q1.id)
        self.assertEqual(response.status_code, 400)

    def dummy_values(self):
        response = satisfied(-1, q1.id)
        self.assertEqual(response.status_code, 403)

        response = satisfied(u1.id, -1)
        self.assertEqual(response.status_code, 403)


class disatisfaction_test(TestCase):
    def new_feedback(self):
        response = disatisfied(u2.id, q2.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Feedback Recorded')

    def again_feedback(self):
        response = disatisfied(u2.id, q2.id)
        self.assertEqual(response.content, 'Feedback Already Recorded')

    def change_feedback(self):
        response = satisfied(u2.id, q2.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Feedback Changed')

    def feedback_active_question(self):
        response = disatisfied(u2.id,q1.id)
        self.assertEqual(response.status_code, 400)

    def dummy_values(self):
        response = disatisfied(-1, q2.id)
        self.assertEqual(response.status_code, 403)

        response = disatisfied(u2.id, -1)
        self.assertEqual(response.status_code, 403)