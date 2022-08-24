from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('new', views.person_new, name='create'),
    path('detail/<int:id>', views.personDetail),
    path('edit/<int:id>', views.person_edit, name='update'),
    path('delete/<int:id>', views.person_delete, name='delete'),
]