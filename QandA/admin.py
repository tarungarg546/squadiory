from django.contrib import admin
from .models import Question,Meetings,Message,Voting,Satisfaction

admin.site.register(Question)
admin.site.register(Meetings)
admin.site.register(Message)
admin.site.register(Voting)
admin.site.register(Satisfaction)

