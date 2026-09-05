from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from myapp.models import User_Info
from django.forms import ModelForm
from django import forms

class User_login(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


# Create your views here.
def login(request):
    if request.method == "GET":
        form = User_login()
        return render(request, "login.html", {"form": form})
    form = User_login(request.POST)
    if not form.is_valid():
        return render(request, "login.html", {"form": form})
    obj = User_Info.objects.filter(**form.cleaned_data).first()
    if obj:
        request.session['info'] = {'id':obj.username, 'password':obj.password, 'is_login':True}
        return HttpResponseRedirect('/home')
    else:
        form.add_error('password', 'username or password is incorrect')
        return render(request, "login.html", {"form": form})


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')