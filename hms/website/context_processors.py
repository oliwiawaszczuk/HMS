from django.utils import timezone

def add_now(request):
    return {'now': timezone.now()}