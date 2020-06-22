from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.utils import timezone

import polls.models as models


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def head(self, *args, **kwargs):
        last_ques = self.get_queryset()[0]

        response = HttpResponse()

        response['Last-Modified'] = last_ques.pub_date\
                                        .strftime('%a, %d %b %Y %H:%M:%S GMT')

        return response

    def get_queryset(self):
        """Return the last five published questions."""
        return models.Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = models.Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = models.Question
    template_name = 'polls/results.html'


class Vote(generic.View):

    def post(self, request, *args, **kwargs):
        question = models.Question.objects.get(id=kwargs.pop('pk'))
        try:
            selected_choice = question.choice_set\
                .get(pk=request.POST['choice'])
        except (KeyError, models.Choice.DoesNotExist):
            context = {
                'question': question,
                'error_message': "You didn't select a choice.",
            }
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', context)
        else:
            selected_choice.votes = F('votes') + 1
            selected_choice.save(update_fields=['votes'])
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(
                reverse('polls:results', args=(question.id,)))
