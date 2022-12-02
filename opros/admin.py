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

admin.site.register(UserInput)