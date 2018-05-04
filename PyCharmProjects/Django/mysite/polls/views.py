from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

from django.urls import reverse
import sys

from .models import Question,Choice

def index(request):
    qlist = Question.objects.all()[:5]
    context = { 'qlist':qlist}
    return HttpResponse(render(request,'polls/index.html',context))


def details(request,qid):
    q = get_object_or_404(Question,pk=qid)
    return HttpResponse( render(request,'polls/details.html',{'q':q}))


def votes(request,qid):
    q = get_object_or_404(Question, pk=qid)
    return HttpResponse(render(request,'polls/results.html',{'q':q }))

def results(request,qid):
    q = get_object_or_404(Question, pk=qid)
    try:
        choices = q.choice_set.get(pk= request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request,'polls/details.html',{'q':qid,'msg':"error try again"})
    else:
        choices.num_votes += 1
        choices.save()
        return HttpResponseRedirect(reverse('polls:votes',args={qid,}))