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
    list_filter = ['meeting_id', ]
    list_display = ['question_text', 'upvote_button', 'upvote_count', 'downvote_button', 'downvote_count',
                    'satisfied_button', 'satisfaction_count', 'disatisfied_button', 'disatisfaction_count']


    def upvote_count(self, obj):
        list = Voting.objects.filter(question_id=obj.id).values_list('vote')
        list = list.filter(vote=1)
        return len(list)

    upvote_count.short_description = 'Up Count'
    upvote_count.allow_tags = True

    def downvote_count(self, obj):
        list = Voting.objects.filter(question_id=obj.id).values_list('vote')
        list = list.filter(vote=2)
        return len(list)

    downvote_count.short_description = 'Down Count'
    downvote_count.allow_tags = True

    def satisfaction_count(self, obj):
        list = Satisfaction.objects.filter(question_id=obj.id).values_list('satisf_status')
        list = list.filter(satisf_status=True)
        return len(list)

    satisfaction_count.short_description = 'Satis_ Count'
    satisfaction_count.allow_tags = True

    def disatisfaction_count(self, obj):
        list = Satisfaction.objects.filter(question_id=obj.id).values_list('satisf_status')
        list = list.filter(satisf_status=False)
        return len(list)

    disatisfaction_count.short_description = 'Disatis_ Count'
    disatisfaction_count.allowed_tags = True

    def upvote_button(self, request):
        return mark_safe('<button type="button" onclick="upvote(request.user.id,obj.question_id)">Upvote</button>')

    upvote_button.short_description = 'Upvote'
    upvote_button.allow_tags = True

    def downvote_button(self, request):
        return mark_safe('<button type="button" onclick="downvote(request.user.id,obj.question_id)">Downvote</button>')

    downvote_button.short_description = 'Downvote'
    downvote_button.allow_tags = True

    def satisfied_button(self, request):
        return mark_safe(
            '<button type="button" onclick="satisfied(request.user.id,obj.question_id)">Satisfied</button>')

    satisfied_button.short_description = 'Satisfy'
    satisfied_button.allow_tags = True

    def disatisfied_button(self, request):
        return mark_safe(
            '<button type="button" onclick="disatisfied(request.user.id,obj.question_id)">Disatisfied</button>')

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
        Function to make currently logged is user as the person asking the question.

        List of parameters of save_model:
        :param request: parameter to access to currently logged in user
        :param obj: Used to access the attribute asker of Question table
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
        elif obj is not None and request.user.id != obj.id:
            return ['question_id','vote']
        else:
            return[]

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
        elif obj is not None and request.user.id != obj.id:
            return ['question_id', 'satisf_status']
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
