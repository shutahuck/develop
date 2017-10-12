import datetime

from django.db import models
from django.utils import timezone

class User_Info_Py(models.Model):
    user_id = models.IntegerField
    user_login = models.CharField(max_length=20,default=None, blank=True, null=True)
    user_first_name = models.CharField(max_length=100,default=None, blank=True, null=True)
    user_last_name = models.CharField(max_length=100,default=None, blank=True, null=True)
    user_password = models.CharField(max_length=15,default=None, blank=True, null=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text