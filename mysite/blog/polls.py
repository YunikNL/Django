from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # Of gebruik admin.StackedInline voor een andere weergave
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)