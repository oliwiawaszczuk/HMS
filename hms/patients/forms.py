from django import forms
from .models import Patient

GENDER_CHOICES = [
    ('male', 'Mężczyzna'),
    ('female', 'Kobieta'),
]

TERRAIN_CHOICES = [
    ('zachodnio-pomorskie', 'Zachodnio-Pomorskie'),
    ('pomorskie', 'Pomorskie'),
    ('warminsko-pomorskie', 'Warmińsko-Pomorskie'),
    ('podlaskie', 'Podlaskie'),
    ('lubelskie', 'Lubelskie'),
    ('mazowieckie', 'Mazowieckie'),
    ('kujawsko-pomorskie', 'Kujawsko-Pomorskie'),
    ('wielkopolskie', 'Wielkopolskie'),
    ('lubuskie', 'Lubuskie'),
    ('dolnoslaskie', 'Dolnośląskie'),
    ('slaskie', 'Śląskie'),
    ('opolskie', 'Opolskie'),
    ('lodzkie', 'Łódzkie'),
    ('swietokrzyskie', 'Świętokrzyskie'),
    ('malopolskie', 'Małopolskie'),
    ('podkarpackie', 'Podkarpackie'),
]


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'surname', 'pesel', 'phone_numer', 'gender', 'birthday', 'terrain', 'city', 'description']

    name = forms.CharField(label='Imię', max_length=50)
    surname = forms.CharField(label='Nazwisko',max_length=50)
    pesel = forms.CharField(label='Pesel',max_length=11)
    phone_numer = forms.CharField(label='Numer telefonu',max_length=9, required=False)
    gender = forms.ChoiceField(label='Płeć', choices=GENDER_CHOICES)
    terrain = forms.ChoiceField(label='Wojewódzctwo', choices=TERRAIN_CHOICES)
    city = forms.CharField(label='Miasto')
    birthday = forms.DateField(label='Data urodzenia', required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
