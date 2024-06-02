from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models

def add_album(request):
    # form = forms.AlbumForm(request.POST)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         return render(request, 'album.html', {'form' : form})
    # else:
    #     form = forms.AlbumForm()
    #     return render(request, 'album.html', {'form' : form})
    form = forms.AlbumForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.AlbumForm()
        return render(request, 'album.html', {'form' : form})

def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')

def update_album(request, id):
    album = models.Album.objects.get(pk=id)
    form = forms.AlbumForm(request.POST, instance=album)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.AlbumForm(instance=album)
        return render(request, 'album.html', {'form':form})