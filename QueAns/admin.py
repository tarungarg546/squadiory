from django.contrib import admin
from .models import Question, Meetings, Message, Voting, Satisfaction
# from datetime import date


class MeetingsAdmin(admin.ModelAdmin):
    list_display = ['meetings_text']

    def get_readonly_fields(self, request, obj=None):
        if request.user == obj.moderator:
            return ['moderator']
        else:
            return ['id','meetings_text', 'venue', 'moderator', 'start_time', 'end_time']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

    def has_delete_permission(self, request, obj=None):
        return False


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'anon_status', 'meeting_id','asker']
    list_filter = ['meeting_id', ]
    list_display = ['question_text']

    def get_fieldsets(self, request, obj=None):
        if obj is not None:
            if obj.anon_status == 1:
                return [(None, {'fields': ('question_text','meeting_id','anon_status',)})]

        return [(None, {'fields': ('question_text', 'anon_status', 'meeting_id','asker')})]


    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if not request.user == obj.asker:
                return ['question_text', 'anon_status', 'meeting_id','asker']
            else:
                return ['asker']
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        """
        List of parameters of save_model:
        :param request: to access the current user
        :param obj: to access the attributes of the model
        :param form: --
        :param change: --
        :return: super(function)
        """
        obj.asker = request.user
        return super(QuestionAdmin,self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False


class VotingAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'question_id', 'vote', ]
    fields = ['vote', ]

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        obj.save()

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Question, QuestionAdmin)
admin.site.register(Meetings, MeetingsAdmin)
admin.site.register(Message)
admin.site.register(Voting, VotingAdmin)
admin.site.register(Satisfaction)
