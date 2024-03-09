from django.shortcuts import render, redirect
from .forms import PersonForm

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

def add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = Person(username=username, password=password)
            people.append(person)
            return redirect('list')
    else:
        form = PersonForm()
    return render(request, 'app424/add.html', {'form': form})

def list(request):
    return render(request, 'app424/list.html', {'people': people})