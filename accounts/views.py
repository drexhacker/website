from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import RegistrationForm, ModalLoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate

# Create your views here.
def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password2'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            return redirect('/accounts/login')
    else:
        form = RegistrationForm(request.GET)
    return render(request, 'accounts/register.html', {'form':form})
