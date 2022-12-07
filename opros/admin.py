from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin, register
# from adminsortable2.admin import SortableAdminMixin

from opros.models import *



class AnswerTabularInline(TabularInline):
    model = Answer
    min_num = 4
    extra = 0

@register(Question)
class QuestionModelAdmin(ModelAdmin):
    inlines = (
        AnswerTabularInline,
    )
    list_display_links = ('id', 'question')
    list_display = ('id','question', 'quiz')
    list_filter = ( 'quiz',)
    save_on_top = True

@register(Quiz)
class QuizModelAdmin(ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    save_on_top = True

@register(Results)
class ResultsModelAdmin(ModelAdmin):
    list_display_links = ('id', 'user_input')
    list_display = ('id','user_input', 'user_results')
    list_filter = ( 'user_input', 'user_results' )
    save_on_top = True

@register(UserInput)
class UserInputModelAdmin(ModelAdmin):
    list_display_links = ('id', 'user_name')
    list_display = ('id', 'result','user_name', 'user_number')
    list_filter = ('result',)
    save_on_top = True
    