from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('pages/landing.html')
    return HttpResponse(template.render())

def jobHistoryView(request):
    template = loader.get_template('pages/job_history.html')
    return HttpResponse(template.render())
def portfolioView(request):
    template = loader.get_template('pages/portfolio.html')
    return HttpResponse(template.render())
def requestJobView(request):
    template = loader.get_template('pages/job_request.html')
    return HttpResponse(template.render())