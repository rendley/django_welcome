from django.contrib import admin

from .models import Question, Choice

# добавление полей Foreign Key в другую модель 
class Choiceline(admin.TabularInline):
    model = Choice
    extra = 3


# class Choiceline(admin.StackedInline):
#     model = Choice
#     extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # порядок полей в админке
    # fields = ['pub_date', 'question_text']

    # группировка полей по вертикали
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    # создание редактирования ответов на вопросы в админке
    inlines = [Choiceline]

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)
