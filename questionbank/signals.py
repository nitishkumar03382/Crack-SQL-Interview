from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Question, UserQuestionStatus

@receiver(post_save, sender=User)
def add_unsolved_questions_to_user(sender, instance, created, **kwargs):
    if created:
        questions = Question.objects.all()
        user_stauses = [
            UserQuestionStatus(user=instance, question=question, status='Unsolved')
            for question in questions
        ]
        UserQuestionStatus.objects.bulk_create(user_stauses)
@receiver(post_save, sender=Question)
def add_new_questions_to_all_users(sender, instance, created, **kwargs):
    if created:
        users = User.objects.all()
        user_stauses = [
            UserQuestionStatus(user=user, question=instance, status='Unsolved')
            for user in users
        ]
        UserQuestionStatus.objects.bulk_create(user_stauses)
