from django.contrib.auth import authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .form import UserCreationForm, RegistrationForm

# def registration(request):
#     form = RegistrationForm()
#     context = {'form': form}
#     if form.is_valid():
#         form.save()
#
#         return redirect('list_view')
#     print('test')
#     return render(request, 'registration/register.html', context)

def registration(request):
    form = RegistrationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Ad user to staff
            form.save_as_staff()
            return redirect('list_view')
        else:
            return render(request, 'registration/register.html', context)
    else:
        return render(request, 'registration/register.html', context)


def login(request):
    context = {}
    return render(request, 'registration/login.html', context)

def logout(request):
    context = {}
    return render(request, 'upload/logout.html', context)
