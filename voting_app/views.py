# voting_app/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Candidate, Vote
from django.shortcuts import render, redirect, get_object_or_404



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('voting_app:vote')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('voting_app:login')


@login_required
def vote_view(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate_id')
        candidate = get_object_or_404(Candidate, pk=candidate_id)
        Vote.objects.create(user=request.user, candidate=candidate)
        messages.success(request, 'Vote submitted successfully')
        return redirect('voting_app:results')
    candidates = Candidate.objects.all()
    return render(request, 'pages/cast_vote.html', {'candidates': candidates})

@login_required
def results_view(request):
    candidates = Candidate.objects.all()
    results = {}
    for candidate in candidates:
        votes_count = Vote.objects.filter(candidate=candidate).count()
        results[candidate.name] = votes_count
    return render(request, 'pages/results.html', {'results': results})
