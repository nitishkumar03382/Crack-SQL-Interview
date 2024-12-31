from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
# Create your models here.
class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ]
    title = models.CharField(max_length=300, unique=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    category = models.CharField(max_length=100)
    doc_link = models.CharField(max_length=1000)
    sol_link = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserQuestionStatus(models.Model):
    STATUS = [
        ('Solved', 'Solved'),
        ('Unsolved', 'Unsolved')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        raise PermissionDenied("Deletion is not allowed")
class UserSolvedQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    updated_at = models.DateTimeField(auto_now=True)

