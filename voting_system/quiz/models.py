from django.db import models
from django.core.exceptions import ValidationError

import polls.models


class Quiz(models.Model):
    questions = models.ManyToManyField(polls.models.Question, null=True)
    rounds = models.IntegerField(default=1)
    ques_in_round = models.IntegerField(default=5)

    def clean(self, *args, **kwargs):
        if self.questions.count() > self.ques_in_round:
            raise ValidationError('questions should be less than %d'
                                  % self.ques_in_round)

    def has_more_questions(self, question_no):
        return self.questions.count() >= question_no
