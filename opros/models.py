from django.db.models import *
from django.db import models
from django.urls import reverse

class Answer(models.Model):
    answer = CharField('ответ',max_length=150,)
    is_correct = BooleanField('правильный ответ',default=False,)
    comment = CharField('комментарий к ответу', max_length=200, blank=True,)
    question = ForeignKey('Question', on_delete=CASCADE, verbose_name='вопрос',)

    def __str__(self):
        return self.answer

    class Meta:
        db_table = 'answers'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'


class Question(models.Model):
    quiz = ForeignKey('Quiz', on_delete=CASCADE, verbose_name='тест',)
    question = CharField('вопрос', max_length=150,)

    def __str__(self):
        return self.question[:50]

    class Meta:
        db_table = 'questions'
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'



class Quiz(models.Model):
    title = CharField('название', max_length=150,)
    slug = SlugField('URL', unique=False,)
    description = TextField('описание', blank=True,)
    created = DateTimeField('создан', auto_now_add=True,)
    modified = DateTimeField('изменен', auto_now=True,)
    npp = PositiveSmallIntegerField('сортировка', default=0,)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'quiz'
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
        ordering = (
            'npp',
        )

    def get_absolute_url(self):
        return reverse(
            'quiz',
            kwargs={
                'quiz_slug': self.slug,
                }
        )

class UserInput(models.Model):
    user_name = CharField('ФИО', max_length=250,)
    random_list = CharField('random list', max_length=250, blank=True)
    user_number = IntegerField('Табельный номер', blank=True)
    result = BooleanField('Результат', default=False)

    def __str__(self):
        return self.user_name


class Results(models.Model):
    user_results = BooleanField('Результат', default=False)
    user_input = OneToOneField('UserInput', on_delete=CASCADE)
    
    def __str__(self):
        return self.user_input
