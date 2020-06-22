from django.contrib import admin

import polls.models as models


class ChoiceInline(admin.StackedInline):
    model = models.Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    ordering = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text', 'votes']
    list_display = ['choice_text', 'question']


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice, ChoiceAdmin)
