from django import forms
from .models import Meet

class MeetForm(forms.Form):
    class Meta:
        model = Meet
        fields = ['worker', 'title', 'date', 'start', 'end', 'description']

    worker = forms.CharField(label='Doktor', max_length=50)
    title = forms.CharField(label='Tytuł', max_length=50)
    date = forms.DateField(label='Data:')
    start = forms.TimeField(label='Początek')
    end = forms.TimeField(label='Koniec')