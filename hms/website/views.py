import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.serializers import serialize
from collections import defaultdict
from workers.models import Worker, WorkHours
from meets.models import Meet
from meets.forms import MeetForm
from patients.models import Patient
from patients.forms import PatientForm
from tests.models import Test

access_to_editing_workers = ('ordynator', 'dyrektor', 'lekarz naczelny')
access_to_editing_patients = ('farmaceuta', 'recepcjonista', 'pielegniarz', 'lekarz specjalista', 'ordynator', 'dyrektor', 'lekarz naczelny')

def is_access_to_editing_workers(request):
    if request.user.is_authenticated:
        if request.user.profession in access_to_editing_workers:
            return True
        else:
            return False
    else:
        return False
    
def is_access_to_editing_patients(request):
    if request.user.is_authenticated:
        if request.user.profession in access_to_editing_patients:
            return True
        else:
            return False
    else:
        return False

# Strona główna
def main(request):
    return render(request, 'entry.html')


# strona logowania
def login(request):
    return render(request, 'login.html')


# strona z dodawaniem nowego pracownika
@login_required(login_url='login')
def add_new_worker_page(request):
    return render(request, 'add_new_worker.html') if is_access_to_editing_workers(request) else redirect('/main/')


# stara strona z wyswietlaniem pracownikow
# @login_required(login_url='login')
# def display_workers(request):
#     if request.user.is_authenticated:
#         if request.user.profession in access_to_editing_workers:
#             workers = Worker.objects.all()
#             return render(request, 'display_workers.html', {'workers': workers})
#         else:
#             return redirect('/main/')
#     else:
#         return redirect('/main/')


# strona z wyswietlaniem pracownikow
@login_required(login_url='login')
def display_block_workers(request, profession):
    if is_access_to_editing_workers(request):
        workers = Worker.objects.all()

        count_workers = defaultdict(int)
        for worker in workers:
            count_workers[worker.profession] += 1

        count_workers = {key.replace(" ", "_"): value for key, value in count_workers.items()}

        context = {
            'workers': workers,
            'profession': profession,
            'count_workers': count_workers,
        }   
        return render(request, 'display_block_workers.html', context) 
    return redirect('/main/')
        

# strona z edytowaniem pracownikow
@login_required(login_url='login')
def edit_worker(request, id):
    if is_access_to_editing_workers(request):
        worker = Worker.objects.get(id=id)
        return render(request, 'edit_worker.html', {'worker': worker})
    return redirect('/main/')


# strona z rejestrowaniem nowych pacjentow
@login_required(login_url='login')
def register_new_patient(request):
    if is_access_to_editing_patients(request):
        form = PatientForm()
        return render(request, 'register_new_patient.html', {'form': form})
    return redirect('/main/')


# strona z wyswietlaniem pacjentow
@login_required(login_url='login')
def display_patients(request):
    if is_access_to_editing_patients(request):
        patients = Patient.objects.all()
        return render(request, 'display_patients.html', {'patients': patients})
    return redirect('/main/')


# strona z edytowaniem pacjenta
@login_required(login_url='login')
def edit_patient(request, id):
    if is_access_to_editing_patients(request):
        patient = Patient.objects.get(id=id)
        form = PatientForm(instance=patient)
        return render(request, 'edit_patient.html', {'patient': patient, 'form': form})
    return redirect('/main/')


# strona z tworzeniem wizyt
@login_required(login_url='login')
def make_an_appointment(request):
    if is_access_to_editing_patients(request):
        patients = Patient.objects.all()
        proffesions = ['ordynator', 'lekarz naczelny', 'lekarz specjalista']
        doctors = Worker.objects.filter(profession__in=proffesions)
        return render(request, 'make_an_appointment.html', {'patients': patients, 'doctors': doctors})
    return redirect('/main/')


# strona z umawianiem badan
@login_required(login_url='login')
def set_a_test(request):
    return render(request, 'set_a_test.html')


# strona z godzinami pracy
@login_required(login_url='login')
def work_hours(request, year, month):
    user = Worker.objects.get(id=request.user.id)
    work_hours = WorkHours.objects.filter(worker=user)
    context = {
        'user': user,
        'work_hours': work_hours,
        'year': year,
        'month': month,
    }
    return render(request, 'work_hours.html', context)


# strona z grafikiem
@login_required(login_url='login')
def view_meets_schedule(request):
    if is_access_to_editing_workers(request):
        meets = Meet.objects.all().order_by('date')
        today = datetime.date.today()

        context = {
            'meets': meets,
            'today': today,
        }   
        return render(request, 'view_schedule.html', context) 
    return redirect('/main/')


# archiwum spotkań
@login_required(login_url='login')
def all_meets(request):
    if is_access_to_editing_workers(request):
        meets = Meet.objects.all().order_by('date')
        today = datetime.date.today()

        context = {
            'meets': meets,
            'today': today,
        }
        return render(request, 'all_meets.html', context)
    return redirect('/main/')


# tworzenie nowego spotkania
@login_required(login_url='login')
def create_meet(request):
    if is_access_to_editing_workers(request):
        workers = Worker.objects.all()
        form = MeetForm()

        context = {
            'workers': workers,
            'form': form,
        }   
        return render(request, 'create_meet.html', context) 
    return redirect('/main/')


# edytowanie spotkania
@login_required(login_url='login')
def edit_meet(request, id):
    if is_access_to_editing_workers(request):
        meet = Meet.objects.get(id=id)
        form = MeetForm(instance=meet)
        return render(request, 'edit_meet.html', {'meet': meet, 'form': form})
    return redirect('/main/')