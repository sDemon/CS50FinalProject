from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.forms import UserCreationForm

@requires_csrf_token
def login(request):
    args = {}
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "User not found"
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')

@requires_csrf_token
def register(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.method == "POST":
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', args)
