from django.contrib import admin
from .models import Question, Meetings, Voting, Satisfaction
from django.utils.safestring import mark_safe


class MeetingsAdmin(admin.ModelAdmin):
    list_display = ['meetings_text']

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            if request.user == obj.moderator:
                return ['moderator']
            else:
                return ['id', 'meetings_text', 'venue', 'moderator', 'start_time', 'end_time']
        else:
            return []

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'anon_status', 'meeting_id']
    list_filter = ['meeting_id',]
    list_display = ['question_text', 'upvote_button', 'downvote_button', 'satisfied_button', 'disatisfied_button']

    def upvote_button(self, request):
        return mark_safe('<button type="button" onclick="upvote(request.user.id,obj.question_id)">Upvote</button>')

    upvote_button.short_description = 'Upvote'
    upvote_button.allow_tags = True

    def downvote_button(self,request):
        return mark_safe('<button type="button" onclick="downvote(request.user.id,obj.question_id)">Downvote</button>')

    downvote_button.short_description = 'Downvote'
    downvote_button.allow_tags = True

    def satisfied_button(self, request):
        return mark_safe('<button type="button" onclick="satisfied(request.user.id,obj.question_id)">Satisfied</button>')

    satisfied_button.short_description = 'Satisfy'
    satisfied_button.allow_tags = True

    def disatisfied_button(self, request):
        return mark_safe('<button type="button" onclick="disatisfied(request.user.id,obj.question_id)">Disatisfied</button>')

    disatisfied_button.short_description = 'Disatisfied'
    disatisfied_button.allow_tags = True

    def get_fieldsets(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            if obj.anon_status == 1:
                return [(None, {'fields': ('question_text', 'meeting_id', 'anon_status',)})]

        return [(None, {'fields': ('question_text', 'anon_status', 'meeting_id', 'asker')})]

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            if request.user != obj.asker:
                return ['question_text', 'anon_status', 'meeting_id', 'asker']
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
        return super(QuestionAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False


class VotingAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'vote', ]
    fields = ['question_id', 'vote', ]

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return ['question_id']
        else:
            return []

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        obj.save()

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False


class SatisfactionAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'satisf_status', ]
    fields = ['question_id', 'satisf_status', ]

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return ['question_id']
        else:
            return []

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        obj.save()

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False


admin.site.register(Question, QuestionAdmin)
admin.site.register(Meetings, MeetingsAdmin)
admin.site.register(Voting, VotingAdmin)
admin.site.register(Satisfaction, SatisfactionAdmin)
