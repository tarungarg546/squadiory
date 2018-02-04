from django.db import models
from django.contrib.auth.models import User


class Meetings(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    HOMER = 'H'
    PLATO = 'P'
    JARVIS = 'J'
    FRIDAY = 'F'
    VENUE_CHOICES = (
        (HOMER,'homer'),
        (PLATO,'plato'),
        (JARVIS,'jarvis'),
        (FRIDAY,'friday'),
    )
    venue = models.CharField(max_length=50,choices=VENUE_CHOICES,default=JARVIS)
    moderator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(help_text="Please use the following format: <em>YYYY-MM-DD</em>."
)


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=100)
    meeting_id = models.ForeignKey(Meetings,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    YES = 'Y'
    NO = 'N'
    ANON_CHOICES = (
        (YES,'yes'),
        (NO,'no'),
    )
    anon_status = models.CharField(max_length=3,choices=ANON_CHOICES,default=NO)

class Message(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length = 1000)

class Voting(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    UPVOTE = 'UP'
    DOWNVOTE = 'DN'
    ANON_CHOICES = (
        (UPVOTE,'up'),
        (DOWNVOTE,'dn'),
    )
    vote = models.CharField(max_length=1)

class Satisfaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    YES = 'Y'
    NO = 'N'
    SATIS_CHOICES = (
        (YES,'yes'),
        (NO,'no'),
    )
    satisf_status = models.CharField(max_length=5,choices=SATIS_CHOICES,default=YES)