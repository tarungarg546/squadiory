from django.db import models
from django.contrib.auth.models import User


class Meetings(models.Model):
    HOMER = 1
    PLATO = 2
    JARVIS = 3
    FRIDAY = 4
    VENUE_CHOICES = (
        (HOMER, 'homer'),
        (PLATO, 'plato'),
        (JARVIS, 'jarvis'),
        (FRIDAY, 'friday'),
    )

    meetings_text = models.CharField(max_length=100)
    venue = models.SmallIntegerField(choices=VENUE_CHOICES, default=HOMER)
    moderator = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(help_text="Start time of the meeting")
    end_time = models.DateTimeField(help_text="End time of the meeting")

    def __str__(self):
        return self.meetings_text


class Question(models.Model):
    YES = 1
    NO = 2
    ANON_CHOICES = (
        (YES, 'yes'),
        (NO, 'no'),
    )

    question_text = models.CharField(max_length=300)
    meeting_id = models.ForeignKey(Meetings, on_delete=models.CASCADE)
    asker = models.ForeignKey(User, on_delete=models.CASCADE)
    anon_status = models.SmallIntegerField(choices=ANON_CHOICES, default=NO)


class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)


class Voting(models.Model):
    UPVOTE = 1
    DOWNVOTE = 2
    NONE = 3
    VOTING_CHOICES = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
        (NONE, 'None'),
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=VOTING_CHOICES, default=NONE)


class Satisfaction(models.Model):
    YES = 1
    NO = 2
    SATISFACTION_CHOICES = (
        (YES, 'yes'),
        (NO, 'no'),
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    satisf_status = models.BooleanField(choices=SATISFACTION_CHOICES, default=YES)
