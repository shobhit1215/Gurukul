from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('notes',views.notes,name="notes"),
    path('delete-note/<int:pk>',views.delete_note,name="delete-note"),
    path('notes-detail/<int:pk>',views.NotesDetailView.as_view(),name="notes-detail"),
    path('homework',views.homework,name="homework"),
    path('delete-homework/<int:pk>',views.delete_homework,name="delete-homework"),
    path('update-homework/<int:pk>',views.update_homework,name="update-homework"),




    
]