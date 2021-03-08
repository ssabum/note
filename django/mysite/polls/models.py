import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# 질문내용과 선택 날짜가 있는 question 모델(테이블)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# 선택지에 해당되는 질문, 선택지가 있는 choice 모델(테이블)
class Choice(models.Model):
    # Question을 참조하겠다는 코드
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text