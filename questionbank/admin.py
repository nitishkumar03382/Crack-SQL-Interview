from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Question)
# admin.site.register(models.UserQuestionStatus)
admin.site.register(models.UserSolvedQuestion)
