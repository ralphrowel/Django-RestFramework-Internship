from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Questions, Choices


def index(request):
    latest_Questions_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_Questions_list': latest_Questions_list}
    return render(request, 'polls/index.html', context)


def detail(request, Questions_id):
    try:
        question = Questions.objects.get(pk=Questions_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})


def results(request, Questions_id):
    question = get_object_or_404(Questions, pk=Questions_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, Questions_id):
    question = get_object_or_404(Questions, pk=Questions_id)
    try:
        selected_choice = question.choices_set.get(pk=request.POST['choice'])
    except (KeyError, Choices.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
