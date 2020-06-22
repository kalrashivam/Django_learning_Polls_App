from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import F
from django.utils import timezone

import quiz.models as models


class IndexView(generic.ListView):
    template_name = 'quiz/index.html'
    model = models.Quiz
    context_object_name = 'quizes'
