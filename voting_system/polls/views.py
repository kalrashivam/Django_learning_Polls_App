from django.shortcuts import render
from django.http import HttpResponse

import polls.models as models


def index(request):
    five_latest_questions = models.Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': five_latest_questions,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s."
                        % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
