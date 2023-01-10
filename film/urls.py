from django.urls import path
from .views import FilmListView, FilmDetailView, FilmCreateView, FilmUpdateView, FilmDeleteView

urlpatterns = [
    path('', FilmListView.as_view(), name='home'),
    path('film/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('film/new/', FilmCreateView.as_view(), name='film_create'),
    path('film/<int:pk>/edit/', FilmUpdateView.as_view(), name = 'film_edit'),
    path('film/<int:pk>/delete/', FilmDeleteView.as_view(), name='film_delete')
]
