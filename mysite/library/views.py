from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def book(request):
    return render(request, 'library/index2.html')

def Genres(request):
    return render(request, 'library/autors.html')

def Authors(request):
    return render(request, 'library/Genres.html')