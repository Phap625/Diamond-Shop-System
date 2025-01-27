from django.shortcuts import render
from accounts.models import Guest
from django.utils.crypto import get_random_string

def home_view(request):
    session_id = request.session.get('session_id')
    if not session_id:
        session_id = get_random_string(32)
        request.session['session_id'] = session_id

        Guest.objects.create(session_id=session_id)

    return render(request, 'Home/home.html')