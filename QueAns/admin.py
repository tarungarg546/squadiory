from django.contrib import admin
from .models import Question,Meetings,Message,Voting,Satisfaction


class MeetingsAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return (request.method in ['GET', 'HEAD'] and
                super().has_change_permission(request, obj))
    def get_readonly_fields(self, request, obj=None):
        return ['id','venue','moderator','start_time','end_time']
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
    def has_delete_permission(self, request, obj=None):
        return False


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text','anon_status','meeting_id',]
    list_filter = ['meeting_id',]

    def save_model(self, request, obj, form, change):
        obj.asker = request.user
        obj.save()
    def has_delete_permission(self, request, obj=None):
        return False
""" 
Working here--- IGNORE THE COMMENT
class VotingAdmin(admin.ModelAdmin):
    list_display = ['user_id','question_id','vote',]
    fields = ['vote',]
    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        obj.save()
    def has_delete_permission(self, request, obj=None):
        return False
"""
admin.site.register(Question,QuestionAdmin)
admin.site.register(Meetings, MeetingsAdmin)
admin.site.register(Message)
admin.site.register(Voting)
admin.site.register(Satisfaction)

