from django.shortcuts import render
from .models import Question, Choice
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'polls/index.html', {
        'greeting' : 'Hello! These are some questions',
        'questions': Question.objects.all()
    })

def question(request, id):
    return render(request, 'polls/question.html', {
        'question': Question.objects.get(pk=id)
    })

def vote(request, id):
    q = Question.objects.get(pk=id)
    selected_choice = q.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(id,)))

def results(request, id):
    return render(request, 'polls/results.html', {
        'question': Question.objects.get(pk=id)
    })