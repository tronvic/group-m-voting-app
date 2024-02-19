from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def candidates(request):
    template = loader.get_template('pages/candidates.html')
    return HttpResponse(template.render())

def castVote(request):
    template = loader.get_template('pages/cast_vote.html')
    return HttpResponse(template.render())
def results(request):
    template = loader.get_template('pages/results.html')
    return HttpResponse(template.render())