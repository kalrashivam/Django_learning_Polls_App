from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

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
    question = get_object_or_404(models.Question, pk=question_id)
    context = {
        'question': question
    }

    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes = F('selected_choice.votes') + 1
        selected_choice.save(update_fields=['votes'])
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,)))
