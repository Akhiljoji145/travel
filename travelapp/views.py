from django.shortcuts import render,redirect
from .models import Team,Places
from django.contrib.auth.models import User
# Create your views here.

def main(request):
	team=Team.objects.all()
	places=Places.objects.all()
	return render(request,'index.html',{'team':team,'places':places})

def user_reg(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('pass')
        check_pass = request.POST.get('check_pass')
        if password == check_pass:
            user = User(first_name=fname, last_name=lname, email=email, username=name, password=password)
            user.save()
            return redirect('login')
    return render(request, 'register.html')


def login(request):
	return render(request,'login.html')

def user_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('pass')

        try:
        	team=Team.objects.all()
        	places=Places.objects.all()
        	user=User.objects.get(username=name)
        	if user.password == password and user.username == name:
        		return render(request, 'index.html', {'name': name,'team':team,'places':places})
        	else:
        		return render(request, 'login.html')
        except User.DoesNotExist:
        	return render(request, 'login.html')
    else:
    	return render(request, 'login.html')


