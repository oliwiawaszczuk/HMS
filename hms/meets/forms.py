from django import forms
from .models import Meet
from workers.models import Worker


class MeetForm(forms.ModelForm):
    class Meta:
        model = Meet
        fields = ['title', 'date', 'start', 'end', 'room', 'workers', 'description']

    title = forms.CharField(label='Tytuł', max_length=50)
    date = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    start = forms.TimeField(label='Od', widget=forms.TimeInput(attrs={'type': 'time'}))
    end = forms.TimeField(label='Do', widget=forms.TimeInput(attrs={'type': 'time'}))
    room = forms.CharField(label='Pokój', max_length=25)
    workers = forms.ModelMultipleChoiceField(
        label='Pracownicy',
        queryset=Worker.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    description = forms.CharField(label='', widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d']
        self.fields['start'].input_formats = ['%H:%M']
        self.fields['end'].input_formats = ['%H:%M']
