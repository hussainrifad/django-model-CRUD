from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_musician, name='addmusician'),
    path('delete/<int:id>', views.delete_musician, name='deletemusician'),
    path('update/<int:id>', views.update_musician, name='updatemusician'),
]