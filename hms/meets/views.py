from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MeetForm
from .models import Meet


access_to_editing_workers = ('ordynator', 'dyrektor', 'lekarz naczelny')

def is_access_to_editing_workers(request):
    if request.user.is_authenticated:
        if request.user.profession in access_to_editing_workers:
            return True
        else:
            return False
    else:
        return False


@login_required(login_url='login')
def set_new_meet(request):
    if request.method == 'POST':
        form = MeetForm(request.POST)

        if form.is_valid():
            new_meet = Meet(
                title = form.cleaned_data['title'],
                date = form.cleaned_data['date'],
                start = form.cleaned_data['start'],
                end = form.cleaned_data['end'],
                room = form.cleaned_data['room'],
                description = form.cleaned_data['description'],
            )
            new_meet.save()
            new_meet.workers.set(form.cleaned_data['workers'])
            return redirect('/view_meets_schedule/')
        else:
            return HttpResponse("Nie poprawne, błąd: ", form.errors)
    else:
        form = MeetForm()

    return render(request, 'create_meet.html', {'form': form}) if is_access_to_editing_workers(request) else redirect('/main/')


@login_required(login_url='login')
def edited_meet(request, id):
    if is_access_to_editing_workers(request):
        meet = get_object_or_404(Meet, id=id)
        if request.method == 'POST':
            form = MeetForm(request.POST, instance=meet)
            if form.is_valid():
                form.save()
                return redirect('/view_meets_schedule/')
            else:
                return HttpResponse("Wypełnij wszystkie pola", status=400)
        else:
            return HttpResponse("To jest widok obsługujący tylko żądania POST.", status=400)
    else:
        return redirect('/main/')

