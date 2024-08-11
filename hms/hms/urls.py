from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from website import views as website_views
from workers import views as workers_views
from patients import views as patients_views
from schedule import views as schedule_views
from meets import  views as meets_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    # website
    path('add_new_worker_page/', website_views.add_new_worker_page, name="add_new_worker_page"),
    path('main/', website_views.main, name="main"),

    # path('display_workers/', website_views.display_workers, name="display_workers"),
    path('display_block_workers/<str:profession>/', website_views.display_block_workers, name="display_block_workers"), 
    path('edit_worker/<int:id>/', website_views.edit_worker, name="edit_worker"),

    path('register_new_patient/', website_views.register_new_patient, name="register_new_patient"),
    path('display_patients/', website_views.display_patients, name="display_patients"),
    path('edit_patient/<int:id>/', website_views.edit_patient, name="edit_patient"),

    path('set_a_test/', website_views.set_a_test, name="set_a_test"),

    path('view_meets_schedule/', website_views.view_meets_schedule, name="view_meets_schedule"),
    path('all_meets/', website_views.all_meets, name="all_meets"),
    path('create_meet/', website_views.create_meet, name="create_meet"),
    path('edit_meet/<int:id>/', website_views.edit_meet, name="edit_meet"),

    path('make_an_appointment/', website_views.make_an_appointment, name="make_an_appointment"),

    path('work_hours/<str:year>/<str:month>/', website_views.work_hours, name="work_hours"),


    path('login/', website_views.login, name="login"),


    # workers
    path('add_new_worker/', workers_views.add_new_worker, name="add_new_worker"),
    path('edited_worker/<int:id>/', workers_views.edited_worker, name="edited_worker"),
    path('loging/', workers_views.loging, name="loging"),


    # patients
    path('add_patient/', patients_views.add_patient, name="add_patient"),
    path('edited_patient/<int:id>/', patients_views.edited_patient, name="edited_patient"),


    # meets
    path('set_new_meet/', meets_views.set_new_meet, name="set_new_meet"),
    path('edited_meet/<int:id>/', meets_views.edited_meet, name="edited_meet"),
]
