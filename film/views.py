from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Film
from django.urls import reverse_lazy
# Create your views here.
class FilmListView(ListView):
    model = Film
    template_name = 'home.html'
    
class FilmDetailView(DeleteView):
    model = Film
    template_name = 'film_detail.html'
    
class FilmCreateView(CreateView):
    model = Film
    template_name = 'film_create.html'
    fields = ['name', 'author','directed', 'cast', 'date', 'short_text', 'text', 'link']
    
class FilmUpdateView(UpdateView):
    model = Film
    template_name = 'film_edit.html'
    fields = ['name','directed', 'cast', 'date', 'short_text', 'text', 'link']
    
class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'film_delete.html'
    success_url = reverse_lazy('home')