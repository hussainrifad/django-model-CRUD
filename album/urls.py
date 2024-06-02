from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_album, name='addalbum'),
    path('delete/<int:id>', views.delete_album, name='deletealbum'),
    path('update/<int:id>', views.update_album, name='updatealbum'),
]