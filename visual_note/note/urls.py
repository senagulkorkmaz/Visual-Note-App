from note import views
from django.urls import path

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='note-create'),
    path('list/', views.ListView.as_view(), name='note-list'),
    path('update/<str:pk>/', views.UpdateView.as_view(), name='note-update'),
    path('delete/<str:pk>/', views.DeleteView.as_view(), name='note-delete'),
]
