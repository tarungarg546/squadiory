from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)

class meetings(models.Model):
    meeting_id = models.IntegerField(primary_key=True)
    venue = models.CharField(max_length=50,)
    moderator_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=100)
    meeting_id = models.ForeignKey(meetings,on_delete=models.CASCADE)
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    anon_status = models.CharField(max_length=3)

class message(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    text = models.CharField(max_length = 1000)

class voting(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    question_id = models.ForeignKey(question,on_delete=models.CASCADE)
    vote = models.CharField(max_length=1)

class satisfaction(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    question_id = models.ForeignKey(question, on_delete=models.CASCADE)
    satisf_status = models.CharField(max_length=5)


