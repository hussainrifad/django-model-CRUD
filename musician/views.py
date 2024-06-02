from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

def add_musician(request):
    form = forms.MusicianForm(request.POST)
    if(request.method == 'POST'):
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('homepage')
    else:
        form = forms.MusicianForm()
        return render(request, 'musician.html', {'form': form})

def delete_musician(request):
    return HttpResponse('delete musician')

def update_musician(request):
    return HttpResponse('update musician')