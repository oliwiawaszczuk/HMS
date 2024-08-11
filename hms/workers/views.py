from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Worker
import random
import string
import datetime

access_to_editing_workers = ('ordynator', 'dyrektor', 'lekarz naczelny')

def is_access_to_editing_workers(request):
    if request.user.is_authenticated:
        if request.user.profession in access_to_editing_workers:
            return True
        else:
            return False
    else:
        return False


def generate_username():
    random_number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    return random_number


def generate_password(length=10):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@login_required(login_url='login')
def add_new_worker(request):
    if is_access_to_editing_workers(request):
        if request.method == 'POST':
            name = request.POST.get('name', None)
            surname = request.POST.get('surname', None)
            email = request.POST.get('email', None)
            phone_number = request.POST.get('phone_number', None)
            profession = request.POST.get('profession', None)
            birthday = request.POST.get('birthday', None)
            family_city = request.POST.get('family_city', None)
            profession_description = request.POST.get('profession_description', None)

            username = generate_username()
            password = generate_password()

            while Worker.objects.filter(username=username).exists():
                username = generate_username()

            if birthday == '':
                birthday = datetime.date.today()

            hashed_password = make_password(password)

            worker = Worker(
                username = username,
                password=hashed_password,
                orginal_password=password,
                name=name,
                surname=surname,
                email=email,
                phone_number=phone_number,
                profession=profession,
                birthday=birthday,
                family_city=family_city,
                profession_description=profession_description
            )
            worker.save()

            return redirect(f'/display_block_workers/{profession}/')
        return render(request, 'add_new_worker.html')
    return redirect('/main/')


@login_required(login_url='login')
def edited_worker(request, id):
    worker = get_object_or_404(Worker, id=id)

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        name = request.POST.get('name', None)
        surname = request.POST.get('surname', None)
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone_number', None)
        profession = request.POST.get('profession', None)
        birthday = request.POST.get('birthday', None)
        family_city = request.POST.get('family_city', None)
        profession_description = request.POST.get('profession_description', None)

        if Worker.objects.filter(username=username).exists() and worker.username != username:
            return JsonResponse({'status': 'error', 'message': 'Login occupied'})

        if birthday == '':
            birthday = datetime.date.today()

        hashed_password = make_password(password)

        worker.username = username
        worker.password = hashed_password
        worker.orginal_password = password
        worker.name = name
        worker.surname = surname
        worker.email = email
        worker.phone_number = phone_number
        worker.profession = profession
        worker.birthday = birthday
        worker.family_city = family_city
        worker.profession_description = profession_description

        worker.save()

        return redirect(f'/display_block_workers/{profession}/')
    return render(request, 'add_new_worker.html')


def loging(request):
    if request.method == 'POST':
        username = request.POST.get('name_val', None)
        password = request.POST.get('password_val', None)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            print('Authentication failed!')
            return JsonResponse({'status': 'error'})
    else:
        return JsonResponse({'status': 'error'})



