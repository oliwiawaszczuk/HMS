from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PatientForm
from .models import Patient

access_to_editing_patients = ('farmaceuta', 'recepcjonista', 'pielegniarz', 'lekarz specjalista', 'ordynator', 'dyrektor', 'lekarz naczelny')

def is_access_to_editing_patients(request):
    if request.user.is_authenticated:
        if request.user.profession in access_to_editing_patients:
            return True
        else:
            return False
    else:
        return False


@login_required(login_url='login')
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            new_patient = Patient(
                name = form.cleaned_data['name'],
                surname = form.cleaned_data['surname'],
                pesel = form.cleaned_data['pesel'],
                phone_numer = form.cleaned_data['phone_numer'],
                gender = form.cleaned_data['gender'],
                terrain = form.cleaned_data['terrain'],
                city = form.cleaned_data['city'],
                birthday = form.cleaned_data['birthday'],
                description = form.cleaned_data['description'],
            )
            new_patient.save()
            return redirect('/display_patients/')
        else:
            print("Nie poprawne, błąd: ", form.errors)
    else:
        form = PatientForm()

    return render(request, 'register_new_patient.html', {'form': form}) if is_access_to_editing_patients(request) else redirect('/main/')


@login_required(login_url='login')
def edited_patient(request, id):
    if is_access_to_editing_patients(request):
        patient = get_object_or_404(Patient, id=id)
        if request.method == 'POST':
            form = PatientForm(request.POST, instance=patient)
            if form.is_valid():
                form.save()
                return redirect('/display_patients/')
            else:
                print(form.errors)
    else:
        return redirect('/main/')
    
