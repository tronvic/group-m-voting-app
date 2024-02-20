from django import forms
from .models import Candidate


class VoteForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name']