from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404

import polls.models as models


def index(request):
    five_latest_questions = models.Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': five_latest_questions,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(models.Question ,pk=question_id)
    context = {
        'question': question
    }

    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s."
                        % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
